import sqlite3 as sql
import numpy as np
from pulp import *
from timeit import default_timer as timer

from person import Person
from nutrient import Nutrient
from optimizier import *
import req_data
import basic_foods
import query
import random

def main():
    josh = Person(24, 'm', 'light')
    
    # Add random foods
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT food_id FROM food_des")
    food_list = cur.fetchall()
    food_list = random.sample(food_list, 950)

    food_ids = [f[0] for f in food_list]

    food_ids = basic_foods.food
    query.list_foods(food_ids)
    josh.add_foods(food_ids)

    josh.remove_nut(['fl'])

    josh.add_nut(Nutrient('DHA', 631, lower_req= 0.3))
    josh.add_nut(Nutrient('EPA', 629, lower_req= 0.3))
    josh.add_nut(Nutrient('energy', 208, lower_req=2000, upper_req= 2200))
    josh.add_nut(Nutrient('sat', 606, upper_req=27))

    prices =  1 * np.ones(len(josh.food_ids))

    unformatted_data = query_database(josh)
    formatted_data = shape_data(unformatted_data, josh)
    prob = optimize_diet(formatted_data, josh, prices)

    describe_solution(prob, josh)


'''
Structure I'm thinking of

    input = get_user_input()
    user = Person()
    user.name = input.name
    user.lifestage = user.lifestage 
    user.select_nutrients
        user.calculate_req()
    
    groc_store = GroceryStore('stater_bros')
    fridge = Fridge(Person)
    groc_store.groceries = input.groceries
    fridge.groceries = GroceryStore.groceries

    unformatted_data = query_nutritional_database(fridge, user)  //
    formatted_data = format_data(unformatted_data, fridge, user)
    optimize_diet(formatted_data, fridge, user)
'''

if __name__ == '__main__':
    main()