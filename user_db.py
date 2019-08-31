import os
import sqlite3 as sql

def create_user_db():
    if not os.path.isfile('spartan.db'):
        con = sql.connect("spartan.db")
        cur = con.cursor()
        
        users_stmt = (
            'CREATE TABLE users ( '
            'name	TEXT, '
            'age	REAL, '
            'sex    TEXT)'
        )

        foods_stmt = (
            'CREATE TABLE foods ( '
            'user_id	        INTEGER, '
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
            'PRIMARY KEY(user_id, food_id) '
            'FOREIGN KEY(user_id) REFERENCES users(rowid))'
        )

        cur.execute(users_stmt)
        cur.execute(foods_stmt)
        con.commit()
        con.close()
    else:
        print("spartan.db already exists")

def add_user_to_db(person):
    con = sql.connect("spartan.db")
    cur = con.cursor()

    sql_stmt = (
        'INSERT INTO users(name, age, sex) '
        'VALUES (?, ?, ?)'
    )

    cur.execute(sql_stmt, [person.name] + [person.age] + [person.sex])
    con.commit()
    con.close()