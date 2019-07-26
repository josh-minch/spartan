import csv
import sqlite3 as sql

from sql_stmnts import *

con = sql.connect('sr_legacy.db')
cur = con.cursor()

cur.executescript(create_food_des_stmt)
cur.executescript(create_fd_group_stmnt)
cur.executescript(create_nut_data_stmt)
cur.executescript(create_nutr_def_stmnt)
cur.executescript(create_weight_stmnt)

for file_name in file_names:
    with open('C:/Users/joshm/Misc/Projects/python/frugal-nutrition/sr_legacy/data/' + file_name) as csvfile:
        file_reader = csv.reader(csvfile, delimiter='^', quotechar='~')
        for row in file_reader:
            cur.execute(file_name_to_insert[file_name], row)

con.commit()
con.close()

add_missing_nut_ids()