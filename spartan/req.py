import sqlite3
import math
import sqlite3 as sql
from datetime import date

import spartan


DAYS_IN_YEAR = 365.2425

life_stages = [(0, 'm'), (0.5, 'm'), (1, 'm'), (4, 'm'), (9, 'm'), (14, 'm'),
               (19, 'm'), (31, 'm'), (51, 'm'), (71, 'm'), (0, 'f'), (0.5, 'f'),
               (1, 'f'), (4, 'f'), (9, 'f'), (14, 'f'), (19, 'f'), (31, 'f'), (51, 'f'),
               (71, 'f'), (14, 'p'), (19, 'p'), (31, 'p'), (14, 'l'), (19, 'l'), (31, 'l')]

display_name_to_id = {
    'Protein': 203,
    'Fat': 204,
    'Carbohydrates': 205,
    'Energy': 208,
    'Water': 255,
    'Sugar': 269,
    'Fiber': 291,
    'Calcium (Ca)': 301,
    'Iron (Fe)': 303,
    'Magnesium (Mg)': 304,
    'Phosphorus (P)': 305,
    'Potassium (K)': 306,
    'Sodium (Na)': 307,
    'Zinc (Zn)': 309,
    'Copper (Cu)': 312,
    'Manganese (Mn)': 315,
    'Selenium (Se)': 317,
    'A': 320,
    'E (Alpha-tocopherol)': 323,
    'D': 328,
    'C (Ascorbic acid)': 401,
    'B1 (Thiamin)': 404,
    'B2 (Riboflavin)': 405,
    'B3 (Niacin)': 406,
    'B5 (Pantothenic acid)': 410,
    'B6': 415,
    'B9 (Folate)': 417,
    'B12 (Cobalamin)': 418,
    'Choline': 421,
    'K (Phylloquinone)': 430,
    'Omega-6 fatty acids': 618,
    'Omega-3 fatty acids': 619,
    'Monounsaturated fat': 645,
    'Polyunsaturated fat': 646,
    'Trans fat': 605,
    'Saturated fat': 606,
    'Cholesterol': 601,
    'Caffeine': 262,
    'Alcohol (Ethanol)': 221
}

macro_names = ['Energy', 'Carbohydrates', 'Sugar', 'Fiber', 'Protein', 'Fat', 'Saturated fat', 'Monounsaturated fat',
               'Polyunsaturated fat', 'Omega-3 fatty acids', 'Omega-6 fatty acids', 'Trans fat', 'Cholesterol', 'Water', 'Caffeine', 'Alcohol (Ethanol)']
vit_names = ['A', 'B1 (Thiamin)', 'B2 (Riboflavin)', 'B3 (Niacin)', 'B5 (Pantothenic acid)', 'B6', 'B9 (Folate)', 'B12 (Cobalamin)', 'C (Ascorbic acid)', 'D', 'E (Alpha-tocopherol)', 'K (Phylloquinone)', 'Choline']
mineral_names = ['Calcium (Ca)', 'Copper (Cu)', 'Iron (Fe)', 'Magnesium (Mg)', 'Manganese (Mn)', 'Phosphorus (P)', 'Potassium (K)', 'Selenium (Se)', 'Sodium (Na)', 'Zinc (Zn)']

nut_names = macro_names + vit_names + mineral_names

min_macro = {
    ( 0, 'm') : [None,60,None,None,9.1,31,None,None,None,0.5,4.4,None,None,None,None,None],
    (0.5, 'm'): [None,95,None,None,11,30,None,None,None,0.5,4.6,None,None,None,None,None],
    ( 1, 'm') : [1000,130,None,19,13,33,None,None,None,0.7,7,None,None,None,None,None],
    ( 4, 'm') : [1400,130,None,25,19,38,None,None,None,0.9,10,None,None,None,None,None],
    ( 9, 'm') : [1800,130,None,31,34,50,None,None,None,1.2,12,None,None,None,None,None],
    (14, 'm') : [2200,130,None,38,52,61,None,None,None,1.6,16,None,None,None,None,None],
    (19, 'm') : [2400,130,None,38,56,66,None,None,None,1.6,17,None,None,None,None,None],
    (31, 'm') : [2200,130,None,38,56,48,None,None,None,1.6,17,None,None,None,None,None],
    (51, 'm') : [2000,130,None,30,56,44,None,None,None,1.6,14,None,None,None,None,None],
    (71, 'm') : [2000,130,None,30,56,44,None,None,None,1.6,14,None,None,None,None,None],
    ( 0, 'f') : [None,60,None,None,9.1,31,None,None,None,0.5,4.4,None,None,None,None,None],
    (0.5, 'f'): [None,95,None,None,11,30,None,None,None,0.5,4.6,None,None,None,None,None],
    ( 1, 'f') : [1000,130,None,19,13,33,None,None,None,0.7,7,None,None,None,None,None],
    ( 4, 'f') : [1200,130,None,25,19,33,None,None,None,0.9,10,None,None,None,None,None],
    ( 9, 'f') : [1600,130,None,26,34,44,None,None,None,1,10,None,None,None,None,None],
    (14, 'f') : [1800,130,None,26,46,50,None,None,None,1.1,11,None,None,None,None,None],
    (19, 'f') : [2000,130,None,25,46,55,None,None,None,1.1,12,None,None,None,None,None],
    (31, 'f') : [1800,130,None,25,46,40,None,None,None,1.1,12,None,None,None,None,None],
    (51, 'f') : [1600,130,None,21,46,35,None,None,None,1.1,11,None,None,None,None,None],
    (71, 'f') : [1600,130,None,21,46,35,None,None,None,1,11,None,None,None,None,None],
    (14, 'p') : [1800,175,None,28,71,50,None,None,None,1,13,None,None,None,None,None],
    (19, 'p') : [2000,175,None,28,71,55,None,None,None,1.4,13,None,None,None,None,None],
    (31, 'p') : [1800,175,None,28,71,40,None,None,None,1.4,13,None,None,None,None,None],
    (14, 'l') : [1800,210,None,29,71,50,None,None,None,1.3,13,None,None,None,None,None],
    (19, 'l') : [2000,210,None,29,71,55,None,None,None,1.3,13,None,None,None,None,None],
    (31, 'l') : [1800,210,None,29,71,40,None,None,None,1.3,13,None,None,None,None,None]
}

min_vit = {
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

min_mineral = {
    ( 0, 'm') : [200,0.2,0.27,30,0.003,100,400,15,110,2],
    (0.5, 'm'): [260,0.22,11,75,0.6,275,860,20,370,3],
    ( 1, 'm') : [700,0.34,7,80,1.2,460,2000,20,800,3],
    ( 4, 'm') : [1000,0.44,10,130,1.5,500,2300,30,1000,5],
    ( 9, 'm') : [1300,0.7,8,240,1.9,1250,2500,40,1200,8],
    (14, 'm') : [1300,0.89,11,410,2.2,1250,3000,55,1500,11],
    (19, 'm') : [1000,0.9,8,400,2.3,700,3400,55,1500,11],
    (31, 'm') : [1000,0.9,8,420,2.3,700,3400,55,1500,11],
    (51, 'm') : [1000,0.9,8,420,2.3,700,3400,55,1500,11],
    (71, 'm') : [1200,0.9,8,420,2.3,700,3400,55,1500,11],
    ( 0, 'f') : [200,0.2,0.27,30,0.003,100,400,15,110,2],
    (0.5, 'f'): [260,0.22,11,75,0.6,275,860,20,370,3],
    ( 1, 'f') : [700,0.34,7,80,1.2,460,2000,20,800,3],
    ( 4, 'f') : [1000,0.44,10,130,1.5,500,2300,30,1000,5],
    ( 9, 'f') : [1300,0.7,8,240,1.6,1250,2300,40,1200,8],
    (14, 'f') : [1300,0.89,15,360,1.6,1250,2300,55,1500,9],
    (19, 'f') : [1000,0.9,18,310,1.8,700,2600,55,1500,8],
    (31, 'f') : [1000,0.9,18,320,1.8,700,2600,55,1500,8],
    (51, 'f') : [1200,0.9,8,320,1.8,700,2600,55,1500,8],
    (71, 'f') : [1200,0.9,8,320,1.8,700,2600,55,1500,8],
    (14, 'p') : [1300,1,27,400,2,1250,2600,60,1500,12],
    (19, 'p') : [1000,1,27,350,2,700,2900,60,1500,11],
    (31, 'p') : [1000,1,27,360,2,700,2900,60,1500,11],
    (14, 'l') : [1300,1.3,10,360,2.6,1250,2500,70,1500,13],
    (19, 'l') : [1000,1.3,9,310,2.6,700,2800,70,1500,12],
    (31, 'l') : [1000,1.3,9,320,2.6,700,2800,70,1500,12]
}

max_macro = dict()
for life_stage in life_stages:
    max_macro[life_stage] = len(nut_names)* [None]

max_vit = {
    ( 0, 'm') : [600,None,None,None,None,None,None,None,None,25,None,None,None],
    (0.5, 'm'): [600,None,None,None,None,None,None,None,None,38,None,None,None],
    ( 1, 'm') : [600,None,None,10,None,30,300,None,400,63,200,None,1000],
    ( 4, 'm') : [900,None,None,15,None,40,400,None,650,75,300,None,1000],
    ( 9, 'm') : [1700,None,None,20,None,60,600,None,1200,100,600,None,2000],
    (14, 'm') : [2800,None,None,30,None,80,800,None,1800,100,800,None,3000],
    (19, 'm') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    (31, 'm') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    (51, 'm') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    (71, 'm') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    ( 0, 'f') : [600,None,None,None,None,None,None,None,None,25,None,None,None],
    (0.5, 'f'): [600,None,None,None,None,None,None,None,None,38,None,None,None],
    ( 1, 'f') : [600,None,None,10,None,30,300,None,400,63,200,None,1000],
    ( 4, 'f') : [900,None,None,15,None,40,400,None,650,75,300,None,1000],
    ( 9, 'f') : [1700,None,None,20,None,60,600,None,1200,100,600,None,2000],
    (14, 'f') : [2800,None,None,30,None,80,800,None,1800,100,800,None,3000],
    (19, 'f') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    (31, 'f') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    (51, 'f') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    (71, 'f') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    (14, 'p') : [2800,None,None,30,None,80,800,None,1800,100,800,None,3000],
    (19, 'p') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    (31, 'p') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    (14, 'l') : [2800,None,None,30,None,80,800,None,1800,100,800,None,3000],
    (19, 'l') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500],
    (31, 'l') : [3000,None,None,35,None,100,1000,None,2000,100,1000,None,3500]
}

max_mineral = {
   ( 0, 'm') : [1000,None,40,None,None,None,None,45,None,4],
   (0.5, 'm'): [1500,None,40,None,None,None,None,60,None,5],
   ( 1, 'm') : [2500,1,40,None,2,3000,None,90,1500,7],
   ( 4, 'm') : [2500,3,40,None,3,3000,None,150,1900,12],
   ( 9, 'm') : [3000,5,40,None,6,4000,None,280,2200,23],
   (14, 'm') : [3000,8,45,None,9,4000,None,400,2300,34],
   (19, 'm') : [2500,10,45,None,11,4000,None,400,2300,40],
   (31, 'm') : [2500,10,45,None,11,4000,None,400,2300,40],
   (51, 'm') : [2000,10,45,None,11,4000,None,400,2300,40],
   (71, 'm') : [2000,10,45,None,11,3000,None,400,2300,40],
   ( 0, 'f') : [1000,None,40,None,None,None,None,45,None,4],
   (0.5, 'f'): [1500,None,40,None,None,None,None,60,None,5],
   ( 1, 'f') : [2500,1,40,None,2,3000,None,90,1500,7],
   ( 4, 'f') : [2500,3,40,None,3,3000,None,150,1900,12],
   ( 9, 'f') : [3000,5,40,None,6,4000,None,280,2200,23],
   (14, 'f') : [3000,8,45,None,9,4000,None,400,2300,34],
   (19, 'f') : [2500,10,45,None,11,4000,None,400,2300,40],
   (31, 'f') : [2500,10,45,None,11,4000,None,400,2300,40],
   (51, 'f') : [2000,10,45,None,11,4000,None,400,2300,40],
   (71, 'f') : [2000,10,45,None,11,3000,None,400,2300,40],
   (14, 'p') : [3000,8,45,None,9,3500,None,400,2300,34],
   (19, 'p') : [2500,10,45,None,11,3500,None,400,2300,40],
   (31, 'p') : [2500,10,45,None,11,3500,None,400,2300,40],
   (14, 'l') : [3000,8,45,None,9,4000,None,400,2300,34],
   (19, 'l') : [2500,10,45,None,11,4000,None,400,2300,40],
   (31, 'l') : [2500,10,45,None,11,0.004,None,400,2300,40]
}

age_ranges = [
    (0, 0.5), (0.5, 1), (1, 4), (4, 9), (9, 14), (14, 19), (19, 31), (31, 51), (51, 71), (71, math.inf)
]

def get_empty_reqs():
    macro = extract_empty_req(macro_names)
    vit = extract_empty_req(vit_names)
    mineral = extract_empty_req(mineral_names)

    return (macro, vit, mineral)

def extract_empty_req(nut_names):
    nuts = []
    for name in nut_names:
        nuts.append(spartan.Nutrient(name=name, min=None, max=None, target=None))
    return nuts

def get_reqs(age_range, sex):
    if (age_range, sex) not in life_stages:
        return

    macro = extract_req(age_range, sex, macro_names, min_macro, max_macro)
    vit = extract_req(age_range, sex, vit_names, min_vit, max_vit)
    mineral = extract_req(age_range, sex, mineral_names, min_mineral, max_mineral)

    return (macro, vit, mineral)

def extract_req(age_range, sex, nut_names, min_reqs, max_reqs):
    nuts = []
    for (name, min, max) in zip(nut_names, min_reqs[(age_range, sex)], max_reqs[(age_range, sex)]):
        nuts.append(spartan.Nutrient(name=name, min=min, max=max, target=None))
    return nuts

def calculate_age_range(bd_year, bd_month, bd_day):
    age = calculate_age(bd_year, bd_month, bd_day)
    for age_range in age_ranges:
        lower, upper = age_range
        if lower <= age < upper:
            return lower

def calculate_age(bd_year, bd_month, bd_day):
    age = date.today() - date(bd_year, bd_month, bd_day)
    return age.days / DAYS_IN_YEAR

def calculate_age_months(bd_month, bd_day):
    return date.today().month - bd_month - (date.today().day < bd_day)

if __name__ == '__main__':
    pass
