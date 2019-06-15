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
import time

MAX_FOOD_ID_LEN = 5

def main():
    josh = Person(25, 'm', 'light')
    
    # Add random foods
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT food_id FROM food_des")
    food_list = cur.fetchall()
    food_list = random.sample(food_list, 300)

    food_ids = [f[0] for f in food_list]

    food_ids = basic_foods.food
    food_ids.sort()
    '''for f in food_ids:
        print( str(format(f).zfill(MAX_FOOD_ID_LEN)) + " - " + query.get_food_name(f) )'''

    with open('fridge.txt', 'w') as file:
        for f in food_ids:
            file.write(str(format(f).zfill(MAX_FOOD_ID_LEN)) + " - " + query.get_food_name(f) + '\n')

    josh.add_foods(food_ids)

    josh.remove_nut(['fl'])

    josh.add_nut(Nutrient('DHA', 631, lower_req = 0.3))
    josh.add_nut(Nutrient('EPA', 629, lower_req = 0.3))
    josh.add_nut(Nutrient('energy', 208, lower_req=2000, upper_req= 2200))
    josh.add_nut(Nutrient('sat', 606, upper_req=27))

    prices =  1 * np.ones(len(josh.food_ids))

    query_time = time.time()
    unformatted_data = query_database(josh)
    print("--- %s seconds query ---" % (time.time() - query_time))
    
    formatted_data = shape_data(unformatted_data, josh)

    opt_time = time.time()
    prob = optimize_diet(formatted_data, josh, prices)
    print("--- %s seconds opt ---" % (time.time() - opt_time))

    describe_solution(prob, josh)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

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
