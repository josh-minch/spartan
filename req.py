import sqlite3

mac_nut_names = ["Water", "Carbohydrate, by difference", "Fiber, total dietary", "Total lipid (fat)", "18:2 undifferentiated", "18:3 undifferentiated", "Protein"]
min_nut_names = ["Calcium, Ca", "Copper, Cu", "Fluoride, F", "Iron, Fe", "Magnesium, Mg", "Manganese, Mn", "Phosphorus, P", "Selenium, Se", "Zinc, Zn", "Potassium, K", "Sodium, Na"]
vit_nut_names = ["Vitamin A, RAE", "Vitamin C, total ascorbic acid", "Vitamin D", "Vitamin E (alpha-tocopherol)", "Vitamin K (phylloquinone)", "Thiamin", "Riboflavin", "Niacin", "Vitamin B-6", "Folate, total", "Vitamin B-12", "Pantothenic acid", "Choline, total" ]

mac_nut_ids = [255, 205, 291, 204, 618, 619, 203]
min_nut_ids = [301, 312, 313, 303, 304, 315, 305, 317, 309, 306, 307]
vit_nut_ids = [320, 401, 324, 323, 430, 404, 405, 406, 415, 417, 418, 410, 421]

nuts = {
    203: 'Protein',
    204: 'Total lipid (fat)',
    205: 'Carbohydrate, by difference',
    208: 'Energy',
    255: 'Water',
    269: 'Sugars, total',
    291: 'Fiber, total dietary',
    301: 'Calcium, Ca',
    303: 'Iron, Fe',
    304: 'Magnesium, Mg',
    305: 'Phosphorus, P',
    306: 'Potassium, K',
    307: 'Sodium, Na',
    309: 'Zinc, Zn',
    312: 'Copper, Cu',
    313: 'Fluoride, F',
    315: 'Manganese, Mn',
    317: 'Selenium, Se',
    320: 'Vitamin A, RAE',
    323: 'Vitamin E (alpha-tocopherol)',
    324: 'Vitamin D',
    401: 'Vitamin C, total ascorbic acid',
    404: 'Thiamin',
    405: 'Riboflavin',
    406: 'Niacin',
    410: 'Pantothenic acid',
    415: 'Vitamin B-6',
    417: 'Folate, total',
    418: 'Vitamin B-12',
    421: 'Choline, total',
    430: 'Vitamin K (phylloquinone)',
    618: '18:2 undifferentiated',
    619: '18:3 undifferentiated'
}

nut_names = mac_nut_names + min_nut_names + vit_nut_names
nut_ids = mac_nut_ids + min_nut_ids + vit_nut_ids

# Possible life stages, a combination of age, sex, and whether or not a person is pregnant or lactating.
life_stage = [
'0-6 mo', '6–12 mo', '1–3', '4–8', 
'9–13 m', '14–18 m', '19–30 m', '31–50 m', '51–70 m', '>70 m',
'9–13 f', '14–18 f', '19–30 f', '31–50 f', '51–70 f', '>70 f',
'14–18 p', '19–30 p','31–50 p',
'14–18 l', '19–30 l','31–50 l' 
]

age_range = [
0, 0.5, 1, 4, 9,
14, 19, 31, 51, 70
]

# Nutritional requirements. Rows correspond to life stages and cols to nutrients
# TODO: Add "added" nutrients like vitamin b12 and vitamin e, as well as adjusted protein and kcal.
# TODO: Resort to match db order or sort when adding nut.  
# Replace nut ordered dict with something else, like a list of tuples 
# (list of tuples like nut = (name, id, req) ?)
min = {
( 0, 'c') : [0.7,60,None,31,4.4,0.5,9.1,200,0.2,10,0.27,30,0.003,100,15,2,400,120,400,40,10,4,2,0.2,0.3,2,0.1,65,0.4,1.7,125],
(0.5, 'c'): [0.8,95,None,30,4.6,0.5,11,260,0.22,500,11,75,0.6,275,20,3,700,370,500,50,10,5,3,0.3,0.4,4,0.3,80,0.5,1.8,150],
( 1, 'c') : [1.3,130,19,None,7,0.7,13,700,0.34,700,7,80,1.2,460,20,3,3000,1000,300,15,15,6,30,1,0.5,6,0.5,150,0.9,2,200],
( 4, 'c') : [1.7,130,25,None,10,0.9,19,1000,0.44,1000,10,130,1.5,500,30,5,3800,1200,400,25,15,7,55,1,0.6,8,0.6,200,1.2,3,250],
( 9, 'm') : [2.4,130,31,None,12,1.2,34,1300,0.7,2000,8,240,1.9,1250,40,8,4500,1500,600,45,15,11,60,0.9,0.9,12,1,300,1.8,4,375],
(14, 'm') : [3.3,130,38,None,16,1.6,52,1300,0.89,3000,11,410,2.2,1250,55,11,4700,1500,900,75,15,15,75,1.2,1.3,16,1.3,400,2.4,5,550],
(19, 'm') : [3.7,130,38,None,17,1.6,56,1000,0.9,4000,8,400,2.3,700,55,11,4700,1500,900,90,15,15,120,1.2,1.3,16,1.3,400,2.4,5,550],
(31, 'm') : [3.7,130,38,None,17,1.6,56,1000,0.9,4000,8,420,2.3,700,55,11,4700,1500,900,90,15,15,120,1,1.3,16,1.3,400,2.4,5,550],
(51, 'm') : [3.7,130,30,None,14,1.6,56,1000,0.9,4000,8,420,2.3,700,55,11,4700,1300,900,90,15,15,120,1,1.3,16,1.7,400,2.4,5,550],
(70, 'm') : [3.7,130,30,None,14,1.6,56,1200,0.9,4000,8,420,2.3,700,55,11,4700,1200,900,90,20,15,120,1.2,1.3,16,1.7,400,2.4,5,550],
( 9, 'f') : [2.1,130,26,None,10,1,34,1300,0.7,2000,8,240,1.6,1250,40,8,4500,1500,600,45,15,11,60,0.9,0.9,12,1,300,1.8,4,375],
(14, 'f') : [2.3,130,26,None,11,1.1,46,1300,0.89,3000,15,360,1.6,1250,55,9,4700,1500,700,65,15,15,75,1,1,14,1.2,400,2.4,5,400],
(19, 'f') : [2.7,130,25,None,12,1.1,46,1000,1,3000,18,310,1.8,700,55,8,4700,1500,700,75,15,15,90,1,1.1,14,1.3,400,2.4,5,425],
(31, 'f') : [2.7,130,25,None,12,1.1,46,1000,1,3000,18,320,1.8,700,55,8,4700,1500,700,75,15,15,90,1.1,1.1,14,1.3,400,2.4,5,425],
(51, 'f') : [3,130,21,None,11,1,46,1200,1,3000,8,320,1.8,700,55,8,4700,1300,700,75,15,15,90,1.1,1.1,14,1.5,400,2.4,5,425],
(70, 'f') : [3,130,21,None,11,1,46,1200,1,3000,8,320,1.8,700,55,8,4700,1200,700,75,20,15,90,1,1.1,14,1.5,400,2.4,5,425],
(14, 'p') : [3,175,28,None,13,1,71,1300,1,3000,27,400,2,1250,60,12,4700,1500,750,80,15,15,75,1.4,1.4,18,1.9,600,2.6,6,450],
(19, 'p') : [3,175,28,None,13,1.4,71,1000,1,3000,27,350,2,700,60,11,4700,1500,770,85,15,15,90,1.4,1.4,18,1.9,600,2.6,6,450],
(31, 'p') : [3,175,28,None,13,1.4,71,1000,1,3000,27,360,2,700,60,11,4700,1500,770,85,15,15,90,1.4,1.4,18,1.9,600,2.6,6,450],
(14, 'l') : [3.8,210,29,None,13,1.3,71,1300,1,3000,10,360,2.6,1250,70,13,5100,1500,1200,115,15,19,75,1.4,1.6,17,2,500,2.8,7,550],
(19, 'l') : [3.8,210,29,None,13,1.3,71,1000,1,3000,9,310,2.6,700,70,12,5100,1500,1300,120,15,19,90,1.4,1.6,17,2,500,2.8,7,550],
(31, 'l') : [3.8,210,29,None,13,1.3,71,1000,1,3000,9,320,2.6,700,70,12,5100,1500,1300,120,15,19,90,1.4,1.6,17,2,500,2.8,7,550]
}
   
if __name__ == '__main__':
    db = sqlite3.connect('dri.db')
    db.execute('DROP table if exists requirements')
    db.execute('''
    CREATE table requirements (lifestage text, \
    water int, carbs int, fiber int, fat int, lin int, alphalin int, prote int, \
    ca int, cu int, fl int, fe int, mg int, mn int, p int, se int, zn int, k int, na int, \
    vita int, vitc int, vitd int, vite int, vitk int, thia int, ribo int, nia int, vitb6 int, fol int, vitb12 int, pant int, chol int)''')
    db.close()
