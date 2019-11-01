import copy
import operator
import os.path
import random
import sqlite3 as sql
import time
from datetime import date
from timeit import default_timer as timer

import numpy as np
from pulp import *

import database
import req
import storage
from constants import *


class Person(object):
    def __init__(self):
        # Personal nutrient requirements and foods in a person's fridge
        self.nuts = []
        self.foods = []
        self.populate_foods_from_db()
        self.populate_nuts_from_db()

    def __repr__(self):
        return str(self.__dict__)

    def set_nuts(self, nuts):
        self.nuts = nuts
        update_nuts_in_db(nuts)

    def set_nut(self, nut, attr, value):
        setattr(nut, attr, value)
        update_nut_in_db(nut, attr, value)

    def populate_nuts_from_db(self):
        con = sql.connect('spartan.db')
        cur = con.cursor()
        sql_stmt = (
            'SELECT * '
            'FROM nuts '
            'ORDER BY rowid'
        )
        for row in cur.execute(sql_stmt):
            self.nuts.append(Nutrient(name=row[0], min=row[1], max=row[2], target=row[3]))

        con.commit()
        con.close()

    def populate_foods_from_db(self):
        con = sql.connect('spartan.db')
        cur = con.cursor()

        sql_stmt = (
            'SELECT * '
            'FROM foods '
            'ORDER BY rowid '
        )

        for row in cur.execute(sql_stmt):
            self.foods.append(Food(*row))

        con.commit()
        con.close()

    def add_foods(self, food_names):
        for food_name in food_names:
            self.foods.append(Food(name=food_name))

    def add_food_to_db(self, food):
        con = sql.connect("spartan.db")
        cur = con.cursor()

        # Store everything but selectable units, as this is a dynamic list
        food_vars = list(vars(food).keys())
        food_vars.remove('selectable_units')
        food_tuple = str(tuple(food_vars))

        food_values = [getattr(food, var) for var in food_vars]
        sql_stmt = (
            'INSERT INTO foods' + food_tuple + ''
            'VALUES (' + (len(food_vars)-1)*'?,' + '?)'
        )

        cur.execute(sql_stmt, food_values)
        con.commit()
        con.close()

    def remove_foods_from_db(self, food_ids):
        con = sql.connect("spartan.db")
        cur = con.cursor()

        foods_tuple = [(food_id,) for food_id in food_ids]
        sql_stmt = (
            'DELETE FROM foods '
            'WHERE food_id = ?'
        )

        cur.executemany(sql_stmt, foods_tuple)
        con.commit()
        con.close()

    def update_food_in_user_db(self, food):
        con = sql.connect("spartan.db")
        cur = con.cursor()

        food_vars = list(vars(food).keys())
        food_vars.remove('selectable_units')
        food_tuple = str(tuple(food_vars))
        food_values = [getattr(food, var) for var in food_vars]

        # Tuple comes from our dict of attr strings, so no need to sanitize
        sql_stmt = (
            "UPDATE foods "
            "SET "+ food_tuple +" = "
            "("+ (len(food_values)-1)*"?," +"?)"
            "WHERE food_id = ?"
        )

        cur.execute(sql_stmt, food_values + [food.food_id])
        con.commit()
        con.close()

class Restriction:
    def __repr__(self):
        return str(self.__dict__)

    def __init__(self, filename, res=None):
        self.filename = filename
        self.res = res or storage.read_csv(filename)

    def add_res(self, res_to_add):
        self.res.add(res_to_add)
        storage.write_csv(self.filename, self.res)

    def remove_res(self, res_to_remove):
        self.res.remove(res_to_remove)
        storage.write_csv(self.filename, self.res)

class Food:
    def __init__(self, food_id=None, name=None, price=None, price_quantity=None, price_unit = 'g', min=None, min_unit='g',
                max=None, max_unit='g', target=None, target_unit='g', nut_quantity=100, nut_quantity_unit='g'):

        self.food_id: int = food_id if food_id is not None else database.get_food_id(name)
        self.name = name or database.get_food_name(food_id)
        self.price: float          = price
        self.price_quantity: float = price_quantity
        self.min: float            = min
        self.max: float            = max
        self.target: float         = target
        self.nut_quantity: float   = nut_quantity

        self.price_unit = price_unit
        self.min_unit = min_unit
        self.max_unit = max_unit
        self.target_unit = target_unit
        self.nut_quantity_unit = nut_quantity_unit
        self.selectable_units = self.get_selectable_units()

    def __repr__(self):
        return str(self.__dict__)

    def get_selectable_units(self):
        con = sql.connect('sr_legacy/sr_legacy.db')
        cur = con.cursor()
        sql_stmnt = (
            'SELECT amount, description, gm_weight '
            'FROM weight '
            'WHERE food_id = ?'
        )
        cur.execute(sql_stmnt, [self.food_id])
        units = cur.fetchall()

        con.commit()
        cur.close()

        selectable_units = ['g']
        for unit in units:
            if unit[0] == 1.0:
                amount_display = ''
            else:
                amount_display = '{:f}'.format(unit[0]).rstrip('0').rstrip('.') + ' '
            description = unit[1]
            gm_weight_display = '{:f}'.format(unit[2]).rstrip('0').rstrip('.')
            gm_weight_display = ' (' + gm_weight_display + ' g)'
            selectable_units.append(amount_display + description + gm_weight_display)

        return selectable_units

class Nutrient:
    def __init__(self, name, nut_id=None, min=None, max=None, target=None):
        self.name = name
        self.nut_id = req.display_name_to_id[self.name]
        self.min = min
        self.max = max
        self.target = target
        self.min_unit = self.max_unit = self.target_unit = self.get_unit()

    def __repr__(self):
        return str(self.__dict__)

    def get_unit(self):
        con = sql.connect("sr_legacy/sr_legacy.db")
        cur = con.cursor()
        sql_stmt = (
            'SELECT units '
            'FROM nutr_def '
            'WHERE id = ?'
        )
        cur.execute(sql_stmt, [self.nut_id])
        unit = cur.fetchall()[0][0]
        con.commit()
        con.close()
        return unit

class Optimizer:
    def __init__(self, person, type_res, fd_res):
        self.lp_prob = LpProblem("Diet", sense=LpMinimize)
        self.type_res = type_res
        self.fd_res = fd_res
        self.foods = sorted(person.foods, key=lambda f: int(f.food_id))
        self.nuts = sorted(person.nuts, key=lambda n: int(n.nut_id))

    def optimize_diet(self):
        if GEN_RESTRICT in self.type_res.res:
            self.foods = self.filter_foods(self.foods, self.fd_res.res)
        self.make_nutrition_matrix()
        self.construct_lp_problem()
        self.add_nutrient_constraints()
        self.add_food_constraints()

        self.lp_prob.writeLP("DietModel.lp")
        self.lp_prob.solve()

        self.describe_solution()

    def filter_foods(self, foods, fd_res):
        food_ids = [food.food_id for food in foods]

        food_id_batches, fd_grps = [], []
        for i in range(0, len(food_ids), SQL_VARIABLE_LIMIT):
            food_id_batches.append(food_ids[i:i + SQL_VARIABLE_LIMIT])

        con = sql.connect('sr_legacy/sr_legacy.db')
        cur = con.cursor()

        for batch in food_id_batches:
            sql_stmnt = (
                'SELECT food_group_id '
                'FROM food_des '
                'WHERE id IN (?'+(len(batch) - 1)*',?'+') '
                'ORDER BY id '
            )
            cur.execute(sql_stmnt, batch)
            fd_grps = fd_grps + cur.fetchall()

        filtered_foods = [food for fd_grp, food in zip(fd_grps, foods) if fd_grp[0] not in fd_res]
        return filtered_foods

    def make_nutrition_matrix(self):
        nut_ids = [nut.nut_id for nut in self.nuts]
        food_ids = [food.food_id for food in self.foods]

        # Due to sqlite3 limitations, we must batch large queries
        food_batch_size = SQL_VARIABLE_LIMIT - len(nut_ids)
        q, final_batch_size = divmod(len(food_ids), food_batch_size)
        n_batches = q + bool(final_batch_size)

        con = sql.connect('sr_legacy/sr_legacy.db')
        cur = con.cursor()
        nut_data = []

        # Get nutritional values for each of the nutrients for each user's food.
        # We must programmatically generate a SQL statement with a variable length number of parameters
        # since food_ids and nut_ids vary depending on user settings
        if n_batches > 1:
            for batch in range(n_batches-1):
                sql_stmnt = (
                    'SELECT amount '
                    'FROM nut_data '
                    'WHERE food_id IN (?'+(food_batch_size - 1)*',?'+') '
                    'AND nut_id IN (?'+(len(nut_ids) - 1)*',?'+')'
                    'ORDER BY food_id, nut_id'
                )

                batch_start = batch * food_batch_size
                batch_end = batch * food_batch_size + food_batch_size

                cur.execute(sql_stmnt, food_ids[batch_start:batch_end] + nut_ids)
                nut_data = nut_data + cur.fetchall()

        sql_stmnt = (
            'SELECT amount '
            'FROM nut_data '
            'WHERE food_id IN (?'+(final_batch_size - 1)*',?'+') '
            'AND nut_id IN (?'+(len(nut_ids) - 1)*',?'+')'
            'ORDER BY food_id, nut_id'
        )

        if n_batches > 1:
            batch_start = batch_end
        else:
            batch_start = 0
        cur.execute(sql_stmnt, food_ids[batch_start:] + nut_ids)

        nut_data = nut_data + cur.fetchall()

        self.nutrition_matrix = self.format_nutrition_matrix(nut_data)

    def format_nutrition_matrix(self, unformatted_data):
        # Construct formatted matrix where each row is a food and each col is a nutrient
        unformatted_data = np.array(unformatted_data)
        unformatted_data[unformatted_data == None] = 0
        unformatted_data = unformatted_data.reshape(len(self.foods), len(self.nuts))

        formatted_data = np.transpose(unformatted_data)
        return formatted_data

    def construct_lp_problem(self):
        food_ids = [food.food_id for food in self.foods]
        prices = [food.price for food in self.foods]

        # Optimize by price or weight depending on if user has prices for all their foods
        if None in prices:
            prices = len(prices) * [1]
            self.optimization_type = 'w'
        else:
            self.optimization_type = 'p'

        self.food_quantity_vector = np.array(
            [LpVariable(str(food_id), 0, None, LpContinuous) for food_id in food_ids])

        self.lp_prob += lpSum(prices * self.food_quantity_vector), "Total cost of foods"

    def add_food_constraints(self):
        for i, food in enumerate(self.foods):
            self.lp_prob += self.food_quantity_vector[i] >= 0

            constraints = [food.min, food.max, food.target]
            units = [food.min_unit, food.max_unit, food.target_unit]
            operators = [operator.ge, operator.le, operator.eq]

            for constraint, unit, op in zip(constraints, units, operators):
                if constraint is not None:
                    if unit != 'g':
                        constraint = convert_quantity(constraint, unit)
                    self.add_constraint(self.food_quantity_vector[i], op,
                                        constraint/DB_SCALER)

    def add_constraint(self, var, comparator, constraint_value):
        # parameterized <=, >=, and == comparators with operator
        self.lp_prob += comparator(var, constraint_value)

    def add_nutrient_constraints(self):
        mins = [nut.min for nut in self.nuts]
        targets = [nut.target for nut in self.nuts]
        maxes = [nut.max for nut in self.nuts]

        for i in range(len(self.nutrition_matrix)):
            if mins[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) >= mins[i]
            if targets[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) == targets[i]
            if maxes[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) <= maxes[i]

    def get_solution_status(self):
        if self.lp_prob.status == LpStatusOptimal:
            if self.optimization_type == 'p':
                title = "Diet: Optimized by price"
                subtitle = (
                    'The cheapest nutritionally complete diet given the foods in your fridge and their prices.'
                )
            elif self.optimization_type == 'w':
                title = "Diet: Optimized by nutritional density"
                subtitle = (
                    'Some of your foods lack prices, so your generated diet '
                    'has been optimized to minimize its total weight.'
                )
        elif self.lp_prob.status == LpStatusInfeasible:
            title = 'Diet: No feasible solution'
            subtitle = (
                'Given the foods in your fridge, '
                'a diet that satisfies your nutritional requirements is '
                'not possible without also exceeding your daily upper limits.'
            )
        return title, subtitle

    def describe_solution(self):
        print("Status: " + LpStatus[self.lp_prob.status])

        for v in self.lp_prob.variables():
            if (v.varValue is not None and v.varValue > 0):
                print(database.get_food_name(v.name), "=", 100 * v.varValue)

        print(100 * value(self.lp_prob.objective), "total grams of food")

    def get_diet_report(self):
        prices = [food.price if food.price is not None else 1 for food in self.foods]

        foods = []
        for i, var in enumerate(self.lp_prob.variables()):
            if (var.varValue is not None and var.varValue > 0):
                food_name = database.get_food_name(var.name)
                cost = round(float(prices[i]) * var.varValue, 2)
                quantity = round(DB_SCALER * var.varValue, 2)
                foods.append({'id': int(var.name), 'name': food_name,
                              'cost': cost, 'quantity': quantity, 'unit': 'g'})

        return foods

    def get_data_for_nutrition_lookup(self):
        food_ids = []
        food_amounts = []

        variables = []
        for var in self.lp_prob.variables():
            if var.varValue is None:
                continue
            if var.varValue <= 0:
                continue
            variables.append(var)
        variables.sort(key = lambda v : int(v.name))

        for var in variables:
            food_ids.append(int(var.name))
            food_amounts.append(DB_SCALER * var.varValue)

        return food_ids, food_amounts

    def get_totals(self):
        total_number = len([v for v in self.lp_prob.variables() if v.varValue is not None and v.varValue > 0])
        total_cost = value(self.lp_prob.objective)
        running_total_mass = 0
        for var in self.lp_prob.variables():
            if (var.varValue is not None and var.varValue > 0):
                running_total_mass += 100 * var.varValue

        return total_number, total_cost, running_total_mass

# Unit includes a parenthetical suffic that gives the equivalent
# quantity in grams, eg oz (85g). Instead of actually converting by
# looking at the appropriate table, simply trim off this suffix
def convert_quantity(quantity, old_unit):
    gm_weight_index_start = old_unit.rfind('(') + 1
    gm_weight_index_end = old_unit.rfind('g')
    gm_weight = float(old_unit[gm_weight_index_start:gm_weight_index_end])
    converted_quantity = quantity * gm_weight
    return converted_quantity
'''
def convert_quantity(food_id, quantity, old_unit, new_unit):

    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()
    sql_stmnt = (
        'SELECT gm_weight '
        'FROM weight '
        'WHERE food_id = ? AND description = ? '
    )

    if old_unit == 'g':
        cur.execute(sql_stmnt, [food_id, new_unit])
        unit_scale_factors = cur.fetchall()
        return quantity * (1 / unit_scale_factors[0][0])
    elif new_unit == 'g':
        cur.execute(sql_stmnt, [food_id, old_unit])
        unit_scale_factors = cur.fetchall()
        return quantity * unit_scale_factors[0][0]


    #Bug: sql query always returns an ordering which may not correspond to the order
    #passed to unit_scale_factors. explicitly return which gm_weight corresponds to which
    #unit description
    #else:
    #    cur.execute(sql_stmnt, [self.food_id, old_unit, new_unit])
    #    unit_scale_factors = cur.fetchall()
    #    return quantity * (unit_scale_factors[0] / unit_scale_factors[1])

'''
def get_nut_groups(nuts):
    macro_end = vit_start = len(req.macro_names)
    vit_end = mineral_start = len(req.vit_names)+len(req.mineral_names)

    macro = [nut for nut in nuts[0:macro_end]]
    vit = [nut for nut in nuts[vit_start:vit_end]]
    mineral = [nut for nut in nuts[mineral_start:]]

    return macro, vit, mineral

def get_empty_nutrition(person):
    sorted_nuts = sorted(person.nuts, key=lambda n: int(n.nut_id))
    nut_ids = [nut.nut_id for nut in sorted_nuts]
    nut_names = [nut.name for nut in sorted_nuts]
    units = get_nutrition_units(nut_ids)

    nutrition = []

    for nut_name, unit in zip(nut_names, units):
        dv = calculate_dv(person, nut_name, None)
        nutrition.append({'name': nut_name, 'amount': None, 'unit': unit[0], 'percent': dv})

    return sort_nutrition(nutrition)

def get_nutrition(person, food_ids, food_amounts):
    # Sort input lists according to food ids in ascending order
    if len(food_amounts) == 0:
        return get_empty_nutrition(person)
    food_tups = sorted(zip(food_ids, food_amounts))
    food_ids, food_amounts = (list(food_tup) for food_tup in zip(*food_tups))
    sorted_nuts = sorted(person.nuts, key=lambda n: int(n.nut_id))
    nut_ids = [nut.nut_id for nut in sorted_nuts]
    nut_names = [nut.name for nut in sorted_nuts]
    units = get_nutrition_units(nut_ids)

    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()
    sql_stmt = (
        'SELECT amount '
        'FROM nut_data WHERE food_id IN (' + (len(food_ids) - 1) * '?, ' + '?) '
        'AND nut_id IN (' + (len(nut_ids) - 1) * '?, ' + '?) '
        'ORDER BY food_id, nut_id'
    )
    cur.execute(sql_stmt, food_ids + nut_ids)
    nut_amounts = np.array(cur.fetchall())

    # Reshape array into matrix, where each row is a food and each column a nutrient
    nut_amounts = nut_amounts.reshape(len(food_ids), len(nut_ids))

    # Check if database lacks a value for each nutrient for all foods and record for later.
    # If every selected food lacks a value for a given nutrient, we display No data.
    # If one or more selected foods have a value, even if the rest have no value in the database,
    # we treat the NULL value in the database as 0 and add them.
    nut_has_data = check_if_sparse_nutrient(nut_amounts)

    nut_amounts[nut_amounts == None] = 0

    # Sum amounts for each respective nutrient given each amount of food
    food_amounts = np.reshape(food_amounts, (len(food_amounts), 1))
    nut_amounts = sum(food_amounts * (nut_amounts / DB_SCALER))

    nutrition = []
    for nut_name, nut_amount, has_data, unit in zip(nut_names, nut_amounts, nut_has_data, units):
        if has_data:
            dv = calculate_dv(person, nut_name, nut_amount)
            nutrition.append({'name':nut_name, 'amount': nut_amount, 'unit': unit[0], 'percent': dv})
        else:
            nutrition.append({'name':nut_name, 'amount': None, 'unit': unit[0], 'percent': None})

    return sort_nutrition(nutrition)

def sort_nutrition(nutrition):
    nutrition = sorted(nutrition, key=lambda n: req.nut_names.index(n['name']))

    macros, vits, minerals = [], [], []

    for nutrient in nutrition:
        if nutrient['name'] in req.macro_names:
            macros.append(nutrient)
        elif nutrient['name'] in req.vit_names:
            vits.append(nutrient)
        elif nutrient['name'] in req.mineral_names:
            minerals.append(nutrient)

    return macros, vits, minerals

def calculate_dv(person, nut_name, nutrient_amount):
    # No data
    if nutrient_amount is None:
        return None

    [min_value] = [nut.min for nut in person.nuts if nut.name == nut_name]

    # No recommendation flag of -1
    if min_value is None:
        return -1

    return 100 * (nutrient_amount / min_value)

def get_nutrition_units(nut_ids):
    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()
    sql_stmt = (
        'SELECT units '
        'FROM nutr_def '
        'WHERE id = ?'
    )
    units = []
    for nut_id in nut_ids:
        cur.execute(sql_stmt, [nut_id])
        units.append(cur.fetchall()[0])

    cur.close()
    con.commit()
    return units

def check_if_sparse_nutrient(nut_amounts):
    nut_has_data = []
    for nut in np.transpose(nut_amounts):
        if all(value is None for value in nut):
            nut_has_data.append(False)
        else:
            nut_has_data.append(True)

    return nut_has_data

def update_sex_bd_in_db(sex, year, mon, day):
    con = sql.connect('spartan.db')
    cur = con.cursor()

    sql_stmt = (
        'UPDATE person '
        'SET (sex, bd_year, bd_mon, bd_day) = '
        '(?,?,?,?)'
    )
    parameters = [sex, year, mon, day]
    cur.execute(sql_stmt, parameters)

    con.commit()
    con.close()

def update_nuts_in_db(nutrients):
    con = sql.connect('spartan.db')
    cur = con.cursor()
    for nutrient in nutrients:
        sql_stmt = (
            'UPDATE nuts '
            'SET (min, max, target) = '
            '(?,?,?) '
            'WHERE name = ?'
        )
        parameters = [nutrient.min, nutrient.max, nutrient.target, nutrient.name]
        cur.execute(sql_stmt, parameters)

    con.commit()
    con.close()

def update_nut_in_db(nut, attr, value):
    con = sql.connect('spartan.db')
    cur = con.cursor()

    # attr comes from our dict, no need to sanitize.
    # In addition, columns cannot be parameterized in SQLite3
    sql_stmt = (
        'UPDATE nuts '
        'SET '+attr+' = '
        '(?) '
        'WHERE name = ?'
    )
    parameters = [value, nut.name]
    cur.execute(sql_stmt, parameters)

    con.commit()
    con.close()

def get_sex_bd_from_db():
    con = sql.connect('spartan.db')
    cur = con.cursor()
    sql_stmt = (
        'SELECT * '
        'FROM person '
        'ORDER BY rowid '
    )

    cur.execute(sql_stmt)
    (sex, bd_year, bd_mon, bd_day) = cur.fetchall()[0]
    return sex, bd_year, bd_mon, bd_day

def get_nuts_from_db():
    con = sql.connect('spartan.db')
    cur = con.cursor()
    sql_stmt = (
        'SELECT * '
        'FROM nuts '
        'ORDER BY rowid '
    )

    cur.execute(sql_stmt)
    nuts = cur.fetchall()

    macro_end = vit_start = len(req.macro_names)
    vit_end = mineral_start = len(req.vit_names)+len(req.mineral_names)

    macro = [Nutrient(name=n[0], min=n[1], max=n[2], target=n[3]) for n in nuts[0:macro_end]]
    vit = [Nutrient(name=n[0], min=n[1], max=n[2], target=n[3]) for n in nuts[vit_start:vit_end]]
    mineral = [Nutrient(name=n[0], min=n[1], max=n[2], target=n[3]) for n in nuts[mineral_start:]]

    return macro, vit, mineral

def get_random_foods_ids(n_foods):
    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()
    cur.execute("SELECT id FROM food_des")
    food_list = cur.fetchall()
    food_list = random.sample(food_list, n_foods)

    food_ids = [f[0] for f in food_list]

    return food_ids

def get_food_ids(n_foods):
    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()
    cur.execute("SELECT id FROM food_des")
    food_list = cur.fetchall()
    food_list = food_list[:n_foods]

    food_ids = [f[0] for f in food_list]

    return food_ids

def get_all_food_ids():
    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()
    cur.execute("SELECT id FROM food_des")
    food_list = cur.fetchall()

    food_ids = [f[0] for f in food_list]

    return food_ids

def main():
    pass

if __name__ == '__main__':
    main()
