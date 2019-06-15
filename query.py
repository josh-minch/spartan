'''
Search database for food, get a food's nutrients, get food name from its id
'''

import sqlite3 as sql
import re
import time
import pprint

def search_food(food_name):
    con = sql.connect('sr28.db')
    cur = con.cursor()

    cur.execute("SELECT food_name FROM food_des WHERE food_name LIKE ? \
                    ORDER BY INSTR(UPPER(food_name), UPPER(?)) ASC", 
                    ['%' + food_name + '%', food_name])


    '''
    SELECT food_name FROM food_des 
    WHERE food_name LIKE '%chocolate%' AND food_name LIKE '%milk%'
    ORDER BY INSTR(UPPER(food_name), ("chocolate")) + INSTR(UPPER(food_name), UPPER('milk')) ASC 
    '''
    food_data = cur.fetchall()

    food_data = [food[0] for food in food_data]

    return food_data


def describe_food(food_id):
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT nut_value FROM nut_data where food_id = ?", [food_id])
    nut_values = cur.fetchall()

    for i in range(len(nut_values)):
        nut_values[i] = nut_values[i][0]

    return nut_values


def get_food_id(food_name):
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute(
        "SELECT food_id FROM food_des where food_name = ?", [food_name])
    food_name = cur.fetchall()

    for i in range(len(food_name)):
        food_name = food_name[i][0]

    return food_name


def main():

    start_time = time.time()
    results = search_food('milk')
    end_time = time.time()

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(results)
    pp.pprint(len(results))
    print("--- %s seconds     ---" % (end_time - start_time))


if __name__ == '__main__':
    main()
