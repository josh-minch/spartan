'''
Search database for food, get a food's nutrients, get food name from its id
'''

import sqlite3 as sql
import time
import pprint


def search_food(food_name):
    con = sql.connect('sr28.db')
    cur = con.cursor()

    # Split search term for multi-word searches like eg, 'chocolate milk'
    split_food_names = food_name.split()
    wildcard_padded_split_food_names = ['%' + name + '%' for name in split_food_names]
    
    # We need to call UPPER because INSTR is not case-sensitive.
    # Order by the sum of how early each term appears in the search result strings.
    if (len(split_food_names) > 0):
        sql_statement = ('SELECT food_name FROM food_des '
                         'WHERE food_name LIKE ?'
                         + (len(wildcard_padded_split_food_names)-1) * ' AND food_name LIKE ?' +
                         ' ORDER BY INSTR(UPPER(food_name), (?))'
                         + (len(split_food_names)-1) * ' + INSTR(UPPER(food_name), UPPER(?))' + ' ASC')

        cur.execute(sql_statement, wildcard_padded_split_food_names + split_food_names)
        
    food_data=cur.fetchall()

    food_data=[food[0] for food in food_data]
    return food_data

def describe_food(food_id):
    con=sql.connect('sr28.db')
    cur=con.cursor()
    cur.execute("SELECT nut_value FROM nut_data where food_id = ?", [food_id])
    nut_values=cur.fetchall()

    for i in range(len(nut_values)):
        nut_values[i]=nut_values[i][0]

    return nut_values


def get_food_id(food_name):
    con=sql.connect('sr28.db')
    cur=con.cursor()
    cur.execute(
        "SELECT food_id FROM food_des where food_name = ?", [food_name])
    food_id=cur.fetchall()

    for i in range(len(food_id)):
        food_id=food_id[i][0]

    return food_id

def get_food_name(food_id):
    con=sql.connect('sr28.db')
    cur=con.cursor()
    cur.execute(
        "SELECT food_name FROM food_des where food_id = ?", [food_id])
    food_name=cur.fetchall()

    for i in range(len(food_name)):
        food_name=food_name[i][0]

    return food_name


def main():

    start_time=time.time()
    results=search_food('a')
    end_time=time.time()

    pp=pprint.PrettyPrinter(indent=4)
    pp.pprint(results)
    pp.pprint(len(results))
    print("--- %s seconds     ---" % (end_time - start_time))


if __name__ == '__main__':
    main()
