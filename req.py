import sqlite3
import math
from datetime import date
DAYS_IN_YEAR = 365.2425


nuts = {
    203: 'Protein',
    204: 'Fat',
    205: 'Carbohydrates',
    208: 'Energy',
    255: 'Water',
    269: 'Sugar',
    291: 'Fiber',
    301: 'Calcium (Ca)',
    303: 'Iron (Fe)',
    304: 'Magnesium (Mg)',
    305: 'Phosphorus (P)',
    306: 'Potassium (K)',
    307: 'Sodium (Na)',
    309: 'Zinc (Zn)',
    312: 'Copper (Cu)',
    313: 'Fluoride (F)',
    315: 'Manganese (Mn)',
    317: 'Selenium (Se)',
    320: 'A',
    323: 'E (Alpha-tocopherol)',
    324: 'D',
    401: 'C (Ascorbic acid)',
    404: 'B₁ (Thiamin)',
    405: 'B₂ (Riboflavin)',
    406: 'B₃ (Niacin)',
    410: 'B₅ (Pantothenic acid)',
    415: 'B₆',
    417: 'B₉ (Folate)',
    418: 'B₁₂ (Cobalamin)',
    421: 'Choline',
    430: 'K (Phylloquinone)',
    618: 'Omega-6',
    619: 'Omega-3',
    645: 'Monounsaturated',
    646: 'Polyunsaturated',
    605: 'Trans',
    606: 'Saturated'
}

# Nutritional requirements. Rows correspond to life stages and cols to nutrients
# TODO: Handle folate, dfe, total, in food
# TODO: Add "added" nutrients like vitamin b12 and vitamin e, as well as adjusted protein and kcal.
# TODO: Resort to match db order or sort when adding nut.
# Replace nut ordered dict with something else, like a list of tuples
# (list of tuples like nut = (name, id, req) ?)
req_macro = {
    ( 0, 'm') : [700.0,60,None,None,9.1,31,None,None,None,0.5,4.4,None],
    (0.5, 'm'): [800.0,95,None,None,11,30,None,None,None,0.5,4.6,None],
    ( 1, 'm') : [1300.0,130,None,19,13,None,None,None,None,0.7,7,None],
    ( 4, 'm') : [1700.0,130,None,25,19,None,None,None,None,0.9,10,None],
    ( 9, 'm') : [2400.0,130,None,31,34,None,None,None,None,1.2,12,None],
    (14, 'm') : [3300.0,130,None,38,52,None,None,None,None,1.6,16,None],
    (19, 'm') : [3700.0,130,None,38,56,None,None,None,None,1.6,17,None],
    (31, 'm') : [3700.0,130,None,38,56,None,None,None,None,1.6,17,None],
    (51, 'm') : [3700.0,130,None,30,56,None,None,None,None,1.6,14,None],
    (71, 'm') : [3700.0,130,None,30,56,None,None,None,None,1.6,14,None],
    ( 0, 'f') : [700.0,60,None,None,9.1,31,None,None,None,0.5,4.4,None],
    (0.5, 'f'): [800.0,95,None,None,11,30,None,None,None,0.5,4.6,None],
    ( 1, 'f') : [1300.0,130,None,19,13,None,None,None,None,0.7,7,None],
    ( 4, 'f') : [1700.0,130,None,25,19,None,None,None,None,0.9,10,None],
    ( 9, 'f') : [2100.0,130,None,26,34,None,None,None,None,1,10,None],
    (14, 'f') : [2300.0,130,None,26,46,None,None,None,None,1.1,11,None],
    (19, 'f') : [2700.0,130,None,25,46,None,None,None,None,1.1,12,None],
    (31, 'f') : [2700.0,130,None,25,46,None,None,None,None,1.1,12,None],
    (51, 'f') : [2700.0,130,None,21,46,None,None,None,None,1.1,11,None],
    (71, 'f') : [2700.0,130,None,21,46,None,None,None,None,1,11,None],
    (14, 'p') : [3000.0,175,None,28,71,None,None,None,None,1,13,None],
    (19, 'p') : [3000.0,175,None,28,71,None,None,None,None,1.4,13,None],
    (31, 'p') : [3000.0,175,None,28,71,None,None,None,None,1.4,13,None],
    (14, 'l') : [3800.0,210,None,29,71,None,None,None,None,1.3,13,None],
    (19, 'l') : [3800.0,210,None,29,71,None,None,None,None,1.3,13,None],
    (31, 'l') : [3800.0,210,None,29,71,None,None,None,None,1.3,13,None]
}

macro_names = ["Water", "Carbohydrates", "Sugar", "Fiber", "Protein", "Fat", "Saturated", "Monounsaturated", "Polyunsaturated", "Omega-3", "Omega-6", "Trans"]
req_vit = {
    ( 0, 'm') : [400,0.2,0.3,2,1.7,0.1,65,0.4,40,10,4,2,125],
    (0.5, 'm'): [500,0.3,0.4,4,1.8,0.3,80,0.5,50,10,5,2.5,150],
    ( 1, 'm') : [300,0.5,0.5,6,2,0.5,150,0.9,15,15,6,30,200],
    ( 4, 'm') : [400,0.6,0.6,8,3,0.6,200,1.2,25,15,7,55,250],
    ( 9, 'm') : [600,0.9,0.9,12,4,1,300,1.8,45,15,11,60,375],
    (14, 'm') : [900,1.2,1.3,16,5,1.3,400,2.4,75,15,15,75,550],
    (19, 'm') : [900,1.2,1.3,16,5,1.3,400,2.4,90,15,15,120,550],
    (31, 'm') : [900,1.2,1.3,16,5,1.3,400,2.4,90,15,15,120,550],
    (51, 'm') : [900,1.2,1.3,16,5,1.7,400,2.4,90,15,15,120,550],
    (71, 'm') : [900,1.2,1.3,16,5,1.7,400,2.4,90,20,15,120,550],
    ( 0, 'f') : [400,0.2,0.3,2,1.7,0.1,65,0.4,40,10,4,2,125],
    (0.5, 'f'): [500,0.3,0.4,4,1.8,0.3,80,0.5,50,10,5,2.5,150],
    ( 1, 'f') : [300,0.5,0.5,6,2,0.5,150,0.9,15,15,6,30,200],
    ( 4, 'f') : [400,0.6,0.6,8,3,0.6,200,1.2,25,15,7,55,250],
    ( 9, 'f') : [600,0.9,0.9,12,4,1,300,1.8,45,15,11,60,375],
    (14, 'f') : [700,1,1,14,5,1.2,400,2.4,65,15,15,75,400],
    (19, 'f') : [700,1.1,1.1,14,5,1.3,400,2.4,75,15,15,90,425],
    (31, 'f') : [700,1.1,1.1,14,5,1.3,400,2.4,75,15,15,90,425],
    (51, 'f') : [700,1.1,1.1,14,5,1.5,400,2.4,75,15,15,90,425],
    (71, 'f') : [700,1.1,1.1,14,5,1.5,400,2.4,75,20,15,90,425],
    (14, 'p') : [750,1.4,1.4,18,6,1.9,600,2.6,80,15,15,75,450],
    (19, 'p') : [770,1.4,1.4,18,6,1.9,600,2.6,85,15,15,90,450],
    (31, 'p') : [770,1.4,1.4,18,6,1.9,600,2.6,85,15,15,90,450],
    (14, 'l') : [1200,1.4,1.6,17,7,2,500,2.8,115,15,19,75,550],
    (19, 'l') : [1300,1.4,1.6,17,7,2,500,2.8,120,15,19,90,550],
    (31, 'l') : [1300,1.4,1.6,17,7,2,500,2.8,120,15,19,90,550]
}

req_mineral = {
    ( 0, 'm') : [200,0.2,10,0.27,30,0.003,100,400,15,110,2],
    (0.5, 'm'): [260,0.22,500,11,75,0.6,275,860,20,370,3],
    ( 1, 'm') : [700,0.34,700,7,80,1.2,460,2000,20,800,3],
    ( 4, 'm') : [1000,0.44,1000,10,130,1.5,500,2300,30,1000,5],
    ( 9, 'm') : [1300,0.7,2000,8,240,1.9,1250,2500,40,1200,8],
    (14, 'm') : [1300,0.89,3000,11,410,2.2,1250,3000,55,1500,11],
    (19, 'm') : [1000,0.9,4000,8,400,2.3,700,3400,55,1500,11],
    (31, 'm') : [1000,0.9,4000,8,420,2.3,700,3400,55,1500,11],
    (51, 'm') : [1000,0.9,4000,8,420,2.3,700,3400,55,1500,11],
    (71, 'm') : [1200,0.9,4000,8,420,2.3,700,3400,55,1500,11],
    ( 0, 'f') : [200,0.2,10,0.27,30,0.003,100,400,15,110,2],
    (0.5, 'f'): [260,0.22,500,11,75,0.6,275,860,20,370,3],
    ( 1, 'f') : [700,0.34,700,7,80,1.2,460,2000,20,800,3],
    ( 4, 'f') : [1000,0.44,1000,10,130,1.5,500,2300,30,1000,5],
    ( 9, 'f') : [1300,0.7,2000,8,240,1.6,1250,2300,40,1200,8],
    (14, 'f') : [1300,0.89,3000,15,360,1.6,1250,2300,55,1500,9],
    (19, 'f') : [1000,0.9,3000,18,310,1.8,700,2600,55,1500,8],
    (31, 'f') : [1000,0.9,3000,18,320,1.8,700,2600,55,1500,8],
    (51, 'f') : [1200,0.9,3000,8,320,1.8,700,2600,55,1500,8],
    (71, 'f') : [1200,0.9,3000,8,320,1.8,700,2600,55,1500,8],
    (14, 'p') : [1300,1,3000,27,400,2,1250,2600,60,1500,12],
    (19, 'p') : [1000,1,3000,27,350,2,700,2900,60,1500,11],
    (31, 'p') : [1000,1,3000,27,360,2,700,2900,60,1500,11],
    (14, 'l') : [1300,1.3,3000,10,360,2.6,1250,2500,70,1500,13],
    (19, 'l') : [1000,1.3,3000,9,310,2.6,700,2800,70,1500,12],
    (31, 'l') : [1000,1.3,3000,9,320,2.6,700,2800,70,1500,12]
}

ul_vit = {
    ( 0, 'm') : [600,None,None,None,None,None,None,None,None,25,None,None,None],
    (0.5, 'm'): [600,None,None,None,None,None,None,None,None,38,None,None,None],
    ( 1, 'm') : [600,None,None,10,None,30,300,None,400,63,200,None,1],
    ( 4, 'm') : [900,None,None,15,None,40,400,None,650,75,300,None,1],
    ( 9, 'm') : [1700,None,None,20,None,60,600,None,1200,100,600,None,2],
    (14, 'm') : [2800,None,None,30,None,80,800,None,1800,100,800,None,3],
    (19, 'm') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    (31, 'm') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    (51, 'm') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    (71, 'm') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    ( 0, 'f') : [600,None,None,None,None,None,None,None,None,25,None,None,None],
    (0.5, 'f'): [600,None,None,None,None,None,None,None,None,38,None,None,None],
    ( 1, 'f') : [600,None,None,10,None,30,300,None,400,63,200,None,1],
    ( 4, 'f') : [900,None,None,15,None,40,400,None,650,75,300,None,1],
    ( 9, 'f') : [1700,None,None,20,None,60,600,None,1200,100,600,None,2],
    (14, 'f') : [2800,None,None,30,None,80,800,None,1800,100,800,None,3],
    (19, 'f') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    (31, 'f') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    (51, 'f') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    (71, 'f') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    (14, 'p') : [2800,None,None,30,None,80,800,None,1800,100,800,None,3],
    (19, 'p') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    (31, 'p') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    (14, 'l') : [2800,None,None,30,None,80,800,None,1800,100,800,None,3],
    (19, 'l') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5],
    (31, 'l') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3.5]
}

ul_mineral = {
   ( 0, 'm') : [1000,None,0.7,40,None,None,None,45,4,None],
   (0.5, 'm'): [1500,None,0.9,40,None,None,None,60,5,None],
   ( 1, 'm') : [2500,1000,1.3,40,65,2,3,90,7,1.5],
   ( 4, 'm') : [2500,3000,2.2,40,110,3,3,150,12,1.9],
   ( 9, 'm') : [3000,5000,10,40,350,6,4,280,23,2.2],
   (14, 'm') : [3000,8000,10,45,350,9,4,400,34,2.3],
   (19, 'm') : [2500,10000,10,45,350,11,4,400,40,2.3],
   (31, 'm') : [2500,10000,10,45,350,11,4,400,40,2.3],
   (51, 'm') : [2000,10000,10,45,350,11,4,400,40,2.3],
   (71, 'm') : [2000,10000,10,45,350,11,3,400,40,2.3],
   ( 0, 'f') : [1000,None,0.7,40,None,None,None,45,4,None],
   (0.5, 'f'): [1500,None,0.9,40,None,None,None,60,5,None],
   ( 1, 'f') : [2500,1000,1.3,40,65,2,3,90,7,1.5],
   ( 4, 'f') : [2500,3000,2.2,40,110,3,3,150,12,1.9],
   ( 9, 'f') : [3000,5000,10,40,350,6,4,280,23,2.2],
   (14, 'f') : [3000,8000,10,45,350,9,4,400,34,2.3],
   (19, 'f') : [2500,10000,10,45,350,11,4,400,40,2.3],
   (31, 'f') : [2500,10000,10,45,350,11,4,400,40,2.3],
   (51, 'f') : [2000,10000,10,45,350,11,4,400,40,2.3],
   (71, 'f') : [2000,10000,10,45,350,11,3,400,40,2.3],
   (14, 'p') : [3000,8000,10,45,350,9,3.5,400,34,2.3],
   (19, 'p') : [2500,10000,10,45,350,11,3.5,400,40,2.3],
   (31, 'p') : [2500,10000,10,45,350,11,3.5,400,40,2.3],
   (14, 'l') : [3000,8000,10,45,350,9,4,400,34,2.3],
   (19, 'l') : [2500,10000,10,45,350,11,4,400,40,2.3],
   (31, 'l') : [2500,10000,10,45,350,11,4,400,40,2.3]
}

macro_names = ["Water", "Carbohydrates", "Sugar", "Fiber", "Protein", "Fat", "Saturated", "Monounsaturated", "Polyunsaturated", "Omega-3", "Omega-6", "Trans"]
vit_names = ['A', 'B₁ (Thiamin)', 'B₂ (Riboflavin)', 'B₃ (Niacin)', 'B₅ (Pantothenic acid)', 'B₆', 'B₉ (Folate)', 'B₁₂ (Cobalamin)', 'C (Ascorbic acid)', 'D', 'E (Alpha-tocopherol)', 'K (Phylloquinone)', 'Choline']
mineral_names = ["Calcium (Ca)", "Copper (Cu)", "Fluoride (F)", "Iron (Fe)", "Magnesium (Mg)", "Manganese (Mn)", "Phosphorus (P)", "Potassium (K)", "Selenium (Se)", "Sodium (Na)", "Zinc (Zn)", ]

age_ranges = [
    (0, 0.5), (0.5, 1), (1, 4), (4, 9), (9, 14), (14, 19), (19, 31), (31, 51), (51, 71), (71, math.inf)
]

def get_req(age_range, sex):
    macro = [{'name': name, 'min': value} for (name, value) in zip(macro_names, req_macro[(age_range, sex)])]
    vit = [{'name': name, 'min': value} for (name, value) in zip(vit_names, req_vit[(age_range, sex)])]
    mineral = [{'name': name, 'min': value} for (name, value) in zip(mineral_names, req_mineral[(age_range, sex)])]

    return (macro, vit, mineral)

def get_ul(age_range, sex):
    vit = [{'name': name, 'min': value} for (name, value) in zip(vit_names, ul_vit[(age_range, sex)])]
    mineral = [{'name': name, 'min': value} for (name, value) in zip(mineral_names, ul_mineral[(age_range, sex)])]

    return (vit, mineral)

def calculate_age_range(bd_year, bd_month, bd_day):
    age = calculate_age(bd_year, bd_month, bd_day)
    for age_range in age_ranges:
        lower, upper = age_range
        if lower <= age < upper:
            return lower

def calculate_age(bd_year, bd_month, bd_day):
    age = date.today() - date(bd_year, bd_month, bd_day)
    return age.days / DAYS_IN_YEAR

if __name__ == '__main__':
    pass