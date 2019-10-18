'''
Functions related to querying food database sr_legacy.db
'''
import sqlite3 as sql

from gui_constants import Res

def search_food(food_name, person, type_res, fd_res):
    if Res.SEARCH_RESTRICT in type_res.res:
        fd_grps = list(fd_res.res)
        fd_grps_tuple = '(?'+(len(fd_grps)-1)*',?'+')'
    else:
        fd_grps = []
        fd_grps_tuple = '()'

    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()

    # Split search term for multi-word searches like eg, 'chocolate milk'
    split_food_names = food_name.split()
    wildcard_padded_split_food_names = ['%' + name + '%' for name in split_food_names]

    # We need to call UPPER because INSTR is not case-sensitive.
    # Order by the sum of how early each term appears in the search result strings.
    if (len(split_food_names) > 0):
        sql_statement = (
            'SELECT food_group_id, long_desc FROM food_des '
            'WHERE long_desc LIKE ?'
            + (len(wildcard_padded_split_food_names)-1) * ' AND long_desc LIKE ?' +
            'AND food_group_id not in ' + fd_grps_tuple +
            ' ORDER BY INSTR(UPPER(long_desc), UPPER(?))'
            + (len(split_food_names)-1) * ' + INSTR(UPPER(long_desc), UPPER(?))' + ' ASC')

        cur.execute(sql_statement, wildcard_padded_split_food_names + fd_grps + split_food_names)

    return cur.fetchall()

def describe_food(food_id):
    con=sql.connect('sr_legacy/sr_legacy.db')
    cur=con.cursor()
    cur.execute("SELECT amount FROM nut_data where food_id = ?", [food_id])
    nut_values=cur.fetchall()

    for i in range(len(nut_values)):
        nut_values[i]=nut_values[i][0]

    return nut_values

def get_food_id(food_name):
    con=sql.connect('sr_legacy/sr_legacy.db')
    cur=con.cursor()
    cur.execute(
        "SELECT id FROM food_des where long_desc = ?", [food_name])
    food_id=cur.fetchall()

    for i in range(len(food_id)):
        food_id=food_id[i][0]

    return food_id

def get_food_name(food_id):
    con=sql.connect('sr_legacy/sr_legacy.db')
    cur=con.cursor()
    cur.execute(
        "SELECT long_desc FROM food_des where id = ?", [food_id])
    food_name=cur.fetchall()

    for i in range(len(food_name)):
        food_name=food_name[i][0]

    return food_name

if __name__ == '__main__':
    pass
