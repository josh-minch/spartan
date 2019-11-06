import os
import sqlite3 as sql
import csv

import database
import req

def create_spartan_db():
    if os.path.isfile(database.resource_path('spartan.db')):
        return

    con = sql.connect(database.resource_path('spartan.db'))
    cur = con.cursor()

    person_stmt = (
        'CREATE TABLE person ( '
        'sex     TEXT, '
        'bd_year INTEGER,'
        'bd_mon  INTEGER,'
        'bd_day  INTEGER)'
    )

    nuts_stmt = (
        'CREATE TABLE nuts ( '
        'name        TEXT, '
        'min         REAL, '
        'max         REAL, '
        'target      REAL )'
    )

    foods_stmt = (
        'CREATE TABLE foods ( '
        'food_id            INTEGER, '
        'name	            TEXT, '
        'price	            REAL, '
        'price_quantity	    REAL, '
        'price_unit 	    TEXT, '
        'min	            REAL, '
        'min_unit 	        TEXT, '
        'max	            REAL, '
        'max_unit 	        TEXT, '
        'target	            REAL, '
        'target_unit 	    TEXT, '
        'nut_quantity       REAL, '
        'nut_quantity_unit  REAL )'
    )

    cur.execute(person_stmt)
    cur.execute(nuts_stmt)
    cur.execute(foods_stmt)
    insert_nuts()
    insert_default_person()
    con.commit()
    con.close()

def insert_nuts():
    con = sql.connect(database.resource_path('spartan.db'))
    cur = con.cursor()

    sql_stmt = (
        'INSERT INTO nuts '
        'VALUES (?,?,?,?)'
    )
    for nut_name in req.nut_names:
        parameters = [nut_name, None, None, None]
        cur.execute(sql_stmt, parameters)

    con.commit()
    con.close()

def insert_default_person():
    con = sql.connect(database.resource_path('spartan.db'))
    cur = con.cursor()

    sql_stmt = (
        'INSERT INTO person '
        'VALUES (?,?,?,?) '
    )
    cur.execute(sql_stmt, [None, None, None, None])

    con.commit()
    con.close()

def write_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows([data])

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            return {int(data) for data in row}
        return set()

if __name__ == "__main__":
    fd_grps = []
    write_csv('example.csv', fd_grps)
    print(read_csv('example.csv'))
