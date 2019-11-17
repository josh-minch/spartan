import os
import csv
import sqlite3 as sql

import sql_stmts


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

    cur.executescript(sql_stmts.create_food_des)
    cur.executescript(sql_stmts.create_fd_group)
    cur.executescript(sql_stmts.create_nut_data)
    cur.executescript(sql_stmts.create_nutr_def)
    cur.executescript(sql_stmts.create_weight)

    for file_name in sql_stmts.file_name_to_insert.keys():
        with open(os.getcwd() + '\\data\\' + file_name) as csvfile:
            file_reader = csv.reader(csvfile, delimiter='^', quotechar='~')
            for row in file_reader:
                cur.execute(sql_stmts.file_name_to_insert[file_name], row)

    con.commit()
    con.close()

    add_missing_nut_ids()
    remove_zero_weights()

if __name__ == "__main__":
    main()
