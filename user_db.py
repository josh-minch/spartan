import os

def create_user_db():
    if not os.path.isfile('spartan.db'):
        con = sql.connect("spartan.db")
        cur = con.cursor()
        
        users_stmt = (
            'CREATE TABLE users ( '
            'rowid	INTEGER NOT NULL, '
            'name	TEXT, '
            'age	INTEGER, '
            'sex    INTEGER, '
            'PRIMARY KEY(rowid))'
        )

        foods_stmt = (
            'CREATE TABLE foods ( '
            'user	    INTEGER, '
            'id         INTEGER, '
            'name	    TEXT, '
            'price	    INTEGER, '
            'min	    INTEGER, '
            'max	    INTEGER, '
            'target	    INTEGER, '
            'PRIMARY KEY(id), '
            'FOREIGN KEY(user) REFERENCES users(rowid))'
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