import os
import sqlite3 as sql
import csv


def create_spartan_db():
    if os.path.isfile('spartan.db'):
        print("spartan.db already exists")
        return

    con = sql.connect("spartan.db")
    cur = con.cursor()

    person_stmt = (
        'CREATE TABLE person ( '
        'sex     TEXT'
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
