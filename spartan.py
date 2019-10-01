import operator
import os.path
import random
import time
import copy
import sqlite3 as sql
import numpy as np
from datetime import date
from timeit import default_timer as timer

from pulp import *

import req
import database
import storage
from constants import *


class Person(object):
    def __init__(self, sex, bd_year, bd_mon, bd_day, rec):
        self.sex = sex
        self.bd_year = bd_year
        self.bd_mon = bd_mon
        self.bd_day = bd_day
        self.rec = rec
        self.age_range = req.calculate_age_range(self.bd_year, self.bd_mon, self.bd_day)
        self.age = req.calculate_age(self.bd_year, self.bd_mon, self.bd_day)

        # Food groups restricted in search results and generated deits
        self.restrict_fds, self.restrict_types = [], []

        # Personal nutrient requirements and foods in a person's fridge
        self.nuts = []
        self.foods = []
        self.set_nuts()
        self.populate_foods_from_db()

    def __repr__(self):
        return str(self.__dict__)

    def set_nuts(self):
        (macro, vit, mineral) = req.get_reqs(self.age_range, self.sex)

        for nut in macro + vit + mineral:
            nut_id = req.display_name_to_id[nut['name']]
            nut_to_append = Nutrient(name=nut['name'], nut_id=nut_id, min=nut['min'], max=nut['max'], target=None)
            self.nuts.append(nut_to_append)

        self.nuts.sort(key=lambda nut: nut.nut_id)

    def add_nut(self, nutrient):
        self.nuts.append(nutrient)
        self.nuts.sort(key=lambda nut: nut.nut_id)

    def remove_nut(self, nut_name):
        self.nuts = [nut for nut in self.nuts if nut.name not in nut_name]

    def populate_foods_from_db(self):
        con = sql.connect("spartan.db")
        cur = con.cursor()

        sql_stmt = (
            'SELECT * '
            'FROM foods'
        )

        for row in cur.execute(sql_stmt):
            self.foods.append(
                Food(row[0], row[1], row[2], row[3], row[4], row[5],
                     row[6], row[7], row[8], row[9], row[10]))

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

    def remove_foods(self, food_ids):
        con = sql.connect("spartan.db")
        cur = con.cursor()

        foods_tuple = [(food_ids,) for food_ids in food_ids]
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
        # tuple comes from our dict of attr strings, so no need to sanitize
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
                max=None, max_unit='g', target=None, target_unit='g'):

        self.food_id = food_id if food_id is not None else database.get_food_id(name)
        self.name = name or database.get_food_name(food_id)
        self.price: float          = price
        self.price_quantity: float = price_quantity
        self.min: float            = min
        self.max: float            = max
        self.target: float         = target

        self.price_unit = price_unit
        self.min_unit = min_unit
        self.max_unit = max_unit
        self.target_unit = target_unit
        self.selectable_units = self.get_selectable_units()

    def __repr__(self):
        return str(self.__dict__)

    def get_selectable_units(self):
        con = sql.connect('sr_legacy/sr_legacy.db')
        cur = con.cursor()
        sql_stmnt = (
            'SELECT description '
            'FROM weight '
            'WHERE food_id = ?'
        )
        cur.execute(sql_stmnt, [self.food_id])
        units = cur.fetchall()
        con.commit()
        cur.close()

        return ['g'] + [unit[0] for unit in units]

class Nutrient:
    def __init__(self, name, nut_id=None, min=None, target=None, max=None):
        self.name = name
        self.nut_id = nut_id
        self.min = min
        self.target = target
        self.max = max

    def __repr__(self):
        return str(self.__dict__)

class Optimizier:
    def __init__(self, person):
        self.lp_prob = LpProblem("Diet", sense=LpMinimize)
        self.person = person
        self.foods = copy.deepcopy(self.person.foods)
        self.foods.sort(key=lambda f: f.food_id)

    def optimize_diet(self):
        self.make_nutrition_matrix()
        self.construct_lp_problem()
        self.add_nutrient_constraints()
        self.add_food_constraints()

        self.lp_prob.writeLP("DietModel.lp")
        self.lp_prob.solve()

    def make_nutrition_matrix(self):
        nut_ids = [nut.nut_id for nut in self.person.nuts]
        food_ids = [food.food_id for food in self.foods]

        con = sql.connect('sr_legacy/sr_legacy.db')
        cur = con.cursor()

        # Get nutritional values for each of the nutrients for each user's food.
        # The len(food_ids)-1 are to programmatically generate a SQL statement with
        # a variable length number of parameters, since food_ids and nut_ids vary depending on user settings

        sql_stmnt = '''select amount from nut_data where food_id in \
        (''' + (len(food_ids) - 1) * '?, ' + '?) and nut_id in \
        (''' + (len(nut_ids) - 1) * '?, ' + '?) order by food_id, nut_id'''

        cur.execute(sql_stmnt, food_ids + nut_ids)

        nut_data = cur.fetchall()
        self.nutrition_matrix = self.format_nutrition_matrix(nut_data)

    def format_nutrition_matrix(self, unformatted_data):
        # Construct formatted matrix where each row is a food and each col is a nutrient
        unformatted_data = np.array(unformatted_data)
        unformatted_data[unformatted_data == None] = 0
        unformatted_data = unformatted_data.reshape(len(self.foods), len(self.person.nuts))

        formatted_data = np.transpose(unformatted_data)
        return formatted_data

    def construct_lp_problem(self):
        food_ids = [food.food_id for food in self.foods]
        ## TODO: Require prices on all foods? SETTING PRICE = 1 TEMPORARY FOR TESTING
        prices = [float(food.price) if food.price is not None else 1 for food in self.foods]

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
                    converted_constraint = self.convert_constraint(food.food_id, constraint, unit)
                    self.add_constraint(self.food_quantity_vector[i], op,
                                        converted_constraint/DB_SCALER)

    def convert_constraint(self, food_id, constraint_value, constraint_unit):
        if constraint_unit == 'g':
            return constraint_value
        else:
            return convert_quantity(food_id, constraint_value, constraint_unit, 'g')

    def add_constraint(self, var, comparator, constraint_value):
        # parameterized <=, >=, and == comparators with operator
        self.lp_prob += comparator(var, constraint_value)

    def add_nutrient_constraints(self):
        mins = [nut.min for nut in self.person.nuts]
        targets = [nut.target for nut in self.person.nuts]
        maxes = [nut.max for nut in self.person.nuts]

        for i in range(len(self.nutrition_matrix)):
            if mins[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) >= mins[i]
            if targets[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) == targets[i]
            if maxes[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) <= maxes[i]

    def get_solution_status(self):
        status_statement = ""

        if (self.lp_prob.status == LpStatusOptimal):
            status_statement = "Optimum diet"
        elif (self.lp_prob.status == LpStatusInfeasible):
            status_statement = "A diet that meets your current constraints is infeasible"

        return status_statement

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

        vars = self.lp_prob.variables()
        vars = [v for v in vars if v.varValue is not None and v.varValue > 0]
        vars.sort(key = lambda v : int(v.name))

        for var in vars:
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

    '''
    Bug: sql query always returns an ordering which may not correspond to the order
    passed to unit_scale_factors. explicitly return which gm_weight corresponds to which
    unit description
    else:
        cur.execute(sql_stmnt, [self.food_id, old_unit, new_unit])
        unit_scale_factors = cur.fetchall()
        return quantity * (unit_scale_factors[0] / unit_scale_factors[1])
    '''

def get_nutrition(person, food_ids, food_amounts):
    # Sort input lists according to food ids in ascending order
    food_tups = sorted(zip(food_ids, food_amounts))
    food_ids, food_amounts = (list(food_tup) for food_tup in zip(*food_tups))

    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()

    nut_ids = [nut.nut_id for nut in person.nuts]

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

    units = get_nutrition_unit(nut_ids)

    nutrition = []
    nut_names = [nut.name for nut in person.nuts]
    for nut_name, nut_amount, has_data, unit in zip(nut_names, nut_amounts, nut_has_data, units):
        dv = calculate_dv(person, nut_name, nut_amount)
        if has_data:
            nutrition.append({'name':nut_name, 'amount': nut_amount, 'unit': unit[0], 'percent': dv})
        else:
            nutrition.append({'name':nut_name, 'amount': None, 'unit': unit[0], 'percent': dv})

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
        if nutrient_amount is None:
            return None

        [min_value] = [nut.min for nut in person.nuts if nut.name == nut_name]

        if min_value is None:
            return None

        return round(100 * (nutrient_amount / min_value), 1)

def get_nutrition_unit(nut_ids):
    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()
    sql_stmt = (
        'SELECT units '
        'FROM nutr_def WHERE id IN (' + (len(nut_ids) - 1) * '?, ' + '?) '
    )
    cur.execute(sql_stmt, nut_ids)
    return cur.fetchall()

def check_if_sparse_nutrient(nut_amounts):
    nut_has_data = []
    for nut in np.transpose(nut_amounts):
        if all(value is None for value in nut):
            nut_has_data.append(False)
        else:
            nut_has_data.append(True)

    return nut_has_data

def add_random_foods():
    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()
    cur.execute("SELECT food_id FROM food_des")
    food_list = cur.fetchall()
    food_list = random.sample(food_list, 300)

    food_ids = [f[0] for f in food_list]

    return food_ids.sort()

def main():
    pass

if __name__ == '__main__':
    main()
