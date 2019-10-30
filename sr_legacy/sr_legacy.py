import csv
import sqlite3 as sql

from sql_stmts import *

def add_missing_nut_ids():
    con = sql.connect('sr_legacy.db')
    cur = con.cursor()

    cur.execute('select id from food_des')
    food_ids = cur.fetchall()
    for food_id in food_ids:

        cur.execute(
            'CREATE TEMPORARY TABLE temptable(food_id INT, nut_id INT, amount FLOAT)')

        cur.execute('''
        insert into temptable (nut_id)
        select id from nutr_def
        except
        select (nut_id) from nut_data where food_id = ? ''', food_id)

        cur.execute('update temptable set food_id = ?', food_id)
        cur.execute('update temptable set amount = NULL')

        cur.execute('''
        insert into nut_data (food_id, nut_id, amount)
        select food_id, nut_id, amount from temptable ''')

        cur.execute('drop table temptable')

    con.commit()
    con.close()

def remove_zero_weights():
    con = sql.connect('sr_legacy.db')
    cur = con.cursor()

    sql_stmt = '''
        DELETE FROM weight WHERE amount = 0.0
    '''
    cur.execute(sql_stmt)

    con.commit()
    con.close()

def main():
    con = sql.connect('sr_legacy.db')
    cur = con.cursor()

    cur.executescript(create_food_des_stmt)
    cur.executescript(create_fd_group_stmnt)
    cur.executescript(create_nut_data_stmt)
    cur.executescript(create_nutr_def_stmnt)
    cur.executescript(create_weight_stmnt)

    for file_name in file_name_to_insert.keys():
        with open('C:/Users/joshm/Misc/Projects/python/frugal-nutrition/sr_legacy/data/' + file_name) as csvfile:
            file_reader = csv.reader(csvfile, delimiter='^', quotechar='~')
            for row in file_reader:
                cur.execute(file_name_to_insert[file_name], row)

    con.commit()
    con.close()

    add_missing_nut_ids()
    remove_zero_weights()

if __name__ == "__main__":
    main()
