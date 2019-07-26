import sqlite3 as sql

con = sql.connect('sr_legacy/sr_legacy.db')
cur = con.cursor()

cur.execute('select long_desc from food_des')
food_names = cur.fetchall()
food_names = [name[0] for name in food_names]

print(len(max(food_names, key=len)))