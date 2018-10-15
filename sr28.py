import sqlite3 as sql
import numpy as np

def create_db(name):
    con = sql.connect(name)
    cur = con.cursor()

    cur.execute("CREATE TABLE nutr_def (nut_id INT, unit INT, nut_tag TEXT, nut_name text)")
    data = extract_data('NUTR_DEF.txt', 4)
    cur.executemany("INSERT INTO nutr_def (nut_id, unit, nut_tag, nut_name) VALUES (?, ?, ?, ?);", data)

    cur.execute("CREATE TABLE nut_data (food_id INT, nut_id INT, nut_value INT)")
    data = extract_data('NUT_DATA.txt', 3)
    cur.executemany("INSERT INTO nut_data (food_id, nut_id, nut_value) VALUES (?, ?, ?);", data)

    cur.execute("CREATE TABLE food_des(food_id INT, food_cat INT, food_name TEXT)")
    data = extract_data('FOOD_DES.txt', 3)
    cur.executemany("INSERT INTO food_des (food_id, food_cat, food_name) VALUES (?, ?, ?);", data)

    con.commit()
    con.close()

def extract_data(filename, cols):
    data = np.array([row.split('^') for row in open(filename, 'r').readlines()])
    data = np.char.strip(data[:,:cols], '~')
    return data

def add_missing_nut_ids():
    
    con = sql.connect('sr28.db')
    cur = con.cursor()

    cur.execute('select food_id from food_des')
    food_ids = cur.fetchall()

    for food_id in food_ids:

        cur.execute('CREATE TEMPORARY TABLE temptable(food_id INT, nut_id INT, nut_value INT)')

        cur.execute('''
        insert into temptable (nut_id) 
        select nut_id from nutr_def
        except
        select (nut_id) from nut_data where food_id = ? ''', food_id)

        cur.execute('update temptable set food_id = ?', food_id)
        cur.execute('update temptable set nut_value = 0')
        
        cur.execute('''
        insert into nut_data (food_id, nut_id, nut_value) 
        select food_id, nut_id, nut_value from temptable ''')

        cur.execute('drop table temptable')

    con.commit()
    con.close()

