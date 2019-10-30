'''
Functions related to querying food database sr_legacy.db
'''
import sqlite3 as sql

from constants import SEARCH_RESTRICT

def search_food(food_name, type_res, fd_res):
    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()

    # Split search term for multi-word searches eg, 'chocolate milk'
    split_food_names = food_name.split()
    wildcard_padded_split_food_names = ['%' + name + '%' for name in split_food_names]

    # Return entire list of foods if no search term supplied
    if len(split_food_names) == 0:
        sql_stmt = (
            'SELECT food_group_id, long_desc FROM food_des '
            'ORDER BY food_group_id '
        )
        parameters = []

    fd_grps, fd_grps_tuple = get_fd_grps(type_res, fd_res)
    # Otherwise, return filtered search result
    # We need to call UPPER because INSTR is not case-sensitive.
    # Order by the sum of how early each term appears in the search result strings.
    if len(split_food_names) > 0:
        sql_stmt = (
            'SELECT food_group_id, long_desc FROM food_des '
            'WHERE long_desc LIKE ? '
            + (len(wildcard_padded_split_food_names)-1) * ' AND long_desc LIKE ?' +
            'AND food_group_id not in ' + fd_grps_tuple +
            ' ORDER BY INSTR(UPPER(long_desc), UPPER(?))'
            + (len(split_food_names)-1) * ' + INSTR(UPPER(long_desc), UPPER(?))' + ' ASC'
        )
        parameters = wildcard_padded_split_food_names + fd_grps + split_food_names

    cur.execute(sql_stmt, parameters)
    return cur.fetchall()

# Create string of the form (?,?,?) where number of ? == number of restricted food groups
def get_fd_grps(type_res, fd_res):
    if SEARCH_RESTRICT not in type_res.res:
        fd_grps_tuple = '()'
        fd_grps = []
    else:
        fd_grps = list(fd_res.res)
        if len(fd_res.res) == 1:
            fd_grps_tuple = '(?)'
        elif len(fd_res.res) > 1:
            fd_grps_tuple = str(tuple(q_mark for q_mark in len(fd_grps)*'?'))
            fd_grps_tuple = fd_grps_tuple.replace("'", "")

    return fd_grps, fd_grps_tuple

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
    import spartan
    type_res = spartan.Restriction('type_res.csv')
    fd_res = spartan.Restriction('fd_res.csv')
    result = search_food('', type_res, fd_res)
