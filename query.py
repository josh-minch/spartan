import sqlite3 as sql
MAX_FOOD_ID_LEN = 5

def search_food(food_name):
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT food_name FROM food_des where food_name LIKE ? ", [food_name + '%'])
    food_list = cur.fetchall()
    cur.execute("SELECT food_name FROM food_des where food_name LIKE ? ", ['%' + food_name])
    food_list += cur.fetchall()
    cur.execute("SELECT food_name FROM food_des where food_name LIKE ? ", ['%' + food_name + '%'])
    food_list += cur.fetchall()

    for i in range(len(food_list)):
        food_list[i] = food_list[i][0]

    return food_list

def describe_food(food_id):
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT nut_value FROM nut_data where food_id = ?", [food_id])
    nut_values = cur.fetchall()

    for i in range(len(nut_values)):
        nut_values[i] = nut_values[i][0]

    return nut_values

def get_food_name(food_id):
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT food_name FROM food_des where food_id = ?", [food_id])
    food_name = cur.fetchall()

    for i in range(len(food_name)):
        food_name = food_name[i][0]

    return food_name
    
def get_food_id(food_name):
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT food_id FROM food_des where food_name = ?", [food_id])
    food_name = cur.fetchall()

    for i in range(len(food_name)):
        food_name = food_name[i][0]

    return food_name

def list_foods(food_ids):
    for f in food_ids:
        print( str(format(f).zfill(MAX_FOOD_ID_LEN)) + " - " + name_food(f) )

'''

def get_food_nutrient_amount(food_name, nutrient_name):
con = sql.connect('usda.sql3')
cur = con.cursor()

cur.execute(
select amount 
from nutrition
where food_id = (select id 
				from food
				where long_desc = "?")
and
nutrient_id = (select id 
				from nutrient
				where name = "?")
, food_name, nutrient)

data = cur.fetchall()
return data[0]
'''
