import sqlite3 as sql
import req, basic_foods, database, random, time
import numpy as np
import operator
from pulp import *
from timeit import default_timer as timer
import os.path

MAX_FOOD_ID_LEN = 5
DB_SCALER = 100
        
class Person(object):
    def __init__(self, name, age, sex):
        assert isinstance(age, (int, float)), "Age must be a number"
        assert sex in {'f', 'm', 'c', 'l', 'p'}, "Select female, male, child, lactating, or pregnant"
        self.name = name
        self.age = age
        self.sex = sex
        #self.activity_level = activity_level

        self.age_range = self.set_age_range()
        self.nuts = []
        self.set_nuts()
        self.foods = []
        self.populate_foods_from_db()

    def __repr__(self):
        return str(self.__dict__)
        
    def set_age_range(self):
        for i, ar in enumerate(req.age_range):
            if self.age < ar: 
                return req.age_range[i-1]

    def set_nuts(self):
        nuts = [ Nutrient(name, id, min) for (id, name, min) 
        in zip(req.nut_ids, req.nut_names, req.min[(self.age_range, self.sex)])]
  
        nuts.sort(key=lambda nut: nut.nut_id)
        self.nuts = nuts
        self.remove_nut('Fluoride, F')
        self.remove_nut('Total lipid (fat)')
        self.add_nut(Nutrient('Energy', 208, min=2300, max=2600))
        #self.add_nut(Nutrient('Sugars, total'))

    def add_nut(self, nutrient):
        if (nutrient.nut_id == None):
            nut_index = req.nut_names.index(nutrient.name)
            nutrient.nut_id = req.nut_ids[nut_index]

        self.nuts.append(nutrient)
        self.nuts.sort(key=lambda nut: nut.nut_id)
        
    def remove_nut(self, nut_name):
        self.nuts = [nut for nut in self.nuts if nut.name not in nut_name]

    def populate_foods_from_db(self):
        con = sql.connect("spartan.db")
        cur = con.cursor()

        sql_stmt = (
            'SELECT food_id, name, price, price_quantity, price_unit, '
            'min, min_unit, max, max_unit, target, target_unit '
            'FROM foods'
        )

        for row in cur.execute(sql_stmt):
            self.foods.append(
                Food(row[0], row[1], row[2], row[3], row[4], row[5],
                     row[6], row[7], row[8], row[9], row[10]))

        con.commit()
        con.close()
   
    def add_foods(self, food_names):
        #for name in food_names:
        #    self.foods.append(Food(name=name))
        self.add_foods_to_db(food_names)
        self.foods.sort(key=lambda f: f.food_id)

    def add_foods_to_db(self, food_names):
        con = sql.connect("spartan.db")
        cur = con.cursor()

        #TODO: One SQL statement to get food_id from food_name and insert it into user db
        foods_tuple = [(food_name, database.get_food_id(food_name)) for food_name in food_names]
        sql_stmt = (
            'INSERT INTO foods(name, food_id) '
            'VALUES (?, ?)'
        )

        cur.executemany(sql_stmt, foods_tuple)
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

    def update_attr_in_db(self, attr, attr_value, food_id):
        con = sql.connect("spartan.db")
        cur = con.cursor()

        if attr in ('price', 'price_quantity', 'min', 'max', 'target'):
            attr_value = float(attr_value)
 
        # attr comes from our dict of attr strings, so no need to sanitize
        sql_stmt = (
            'UPDATE foods '
            'SET ' + attr + ' = ?'
            'WHERE food_id = ?'
        )

        cur.execute(sql_stmt, [attr_value] + [food_id])
        con.commit()
        con.close()

    # Calculate the equivalent daily value percentage of a given nutrient amount
    # based on a person's nutrient requirements. 

class Food:
    def __init__(self, food_id=None, name=None, 
                       price=None, price_quantity=100, price_unit='g',
                       min=None, min_unit='g', 
                       max=None, max_unit='g',
                       target=None, target_unit='g'):

        self.food_id = food_id if food_id is not None else database.get_food_id(name)
        self.name = name or database.get_food_name(food_id)
        self.price: float          = price
        self.price_quantity: float = price_quantity
        self.price_unit: str       = price_unit
        self.min: float            = min
        self.min_unit: str         = min_unit
        self.max: float            = max
        self.max_unit: str         = max_unit
        self.target: float         = target
        self.target_unit: str      = target_unit

    def __repr__(self):
        return str(self.__dict__)

    def get_selectable_units(self):

        con = sql.connect('sr_legacy/sr_legacy.db')
        cur = con.cursor()
        sql_stmnt = (
            'SELECT description'
            'FROM weight'
            'WEHERE food_id = ?'
        )
        cur.execute(sql_stmnt, self.food_id)

        return cur.fetchall()

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
    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()

    nut_ids = tuple([nut.nut_id for nut in person.nuts])
    # nutrient list is clean, no need to sanitize
    sql_stmt = (
        'SELECT amount '
        'FROM nut_data WHERE food_id IN (' + (len(food_ids) - 1) * '?, ' + '?) '
        'AND nut_id IN '+ str(nut_ids)
    )
    cur.execute(sql_stmt, food_ids)
    
    nut_amounts = cur.fetchall()
    nut_amounts = np.array([amount[0] if amount[0] is not None else 0 for amount in nut_amounts])

    # sum amounts for each respective nutrient given each amount of food
    nut_amounts = nut_amounts.reshape(len(food_ids), len(nut_ids))
    food_amounts = np.reshape(food_amounts, (len(food_amounts), 1))
    nut_amounts = sum(food_amounts * (nut_amounts / DB_SCALER))

    units = get_nutrition_unit(nut_ids)
  
    nutrition = []
    nut_names = [nut.name for nut in person.nuts]
    for nut_name, nut_amount, unit in zip(nut_names, nut_amounts, units):
        dv = calculate_dv(person, nut_name, nut_amount)
        nutrition.append({'name':nut_name, 'amount': nut_amount, 'unit': unit[0], 'percent': dv})
                
    return nutrition

def calculate_dv(person, nut_name, nutrient_amount):
        if nutrient_amount is None:
            return None
            
        [min_value] = [nut.min for nut in person.nuts if nut.name == nut_name]

        return round(100 * (nutrient_amount / min_value), 1)

def get_nutrition_unit(nut_ids):
    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()
    sql_stmt = (
        'SELECT units '
        'FROM nutr_def WHERE id IN '+ str(nut_ids)
    )
    cur.execute(sql_stmt)
    return cur.fetchall()

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

    def __init__(self):
        self.lp_prob = LpProblem("Diet", sense=LpMinimize)
    
    def make_nutrition_matrix(self, person):
        nut_ids = [nut.nut_id for nut in person.nuts]
        food_ids = [food.food_id for food in person.foods]

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
        self.nutrition_matrix = self.format_nutrition_matrix(nut_data, person)

    def format_nutrition_matrix(self, unformatted_data, person):
        # Construct formatted matrix where each row is a food and each col is a nutrient
        unformatted_data = np.array(unformatted_data)
        unformatted_data[unformatted_data == None] = 0
        unformatted_data = unformatted_data.reshape(len(person.foods), len(person.nuts))

        formatted_data = np.transpose(unformatted_data)
        return formatted_data

    def construct_lp_problem(self, person):
        
        food_ids = [food.food_id for food in person.foods]
        ## TODO: Require prices on all foods? SETTING PRICE = 1 TEMPORARY FOR TESTING
        prices = [float(food.price) if food.price is not None else 1 for food in person.foods]

        self.food_quantity_vector = np.array(
            [LpVariable(str(food_id), 0, None, LpContinuous) for food_id in food_ids])

        self.lp_prob += lpSum(prices * self.food_quantity_vector), "Total cost of foods"

    def add_food_constraints(self, person):
        for i, food in enumerate(person.foods):
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

    def add_nutrient_constraints(self, person):
        mins = [nut.min for nut in person.nuts]
        targets = [nut.target for nut in person.nuts]
        maxes = [nut.max for nut in person.nuts]

        for i in range(len(self.nutrition_matrix)):
            if mins[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) >= mins[i]
            if targets[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) == targets[i]
            if maxes[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) <= maxes[i]

    def optimize_diet(self, person):
        self.make_nutrition_matrix(person)
        self.construct_lp_problem(person)
        self.add_nutrient_constraints(person)
        self.add_food_constraints(person)

        self.lp_prob.writeLP("DietModel.lp")
        self.lp_prob.solve()
        
    def describe_solution_status(self):
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

    def get_totals(self):
        total_number = len([v for v in self.lp_prob.variables() if v.varValue is not None and v.varValue > 0])
        total_cost = value(self.lp_prob.objective)
        running_total_mass = 0
        for var in self.lp_prob.variables():
            if (var.varValue is not None and var.varValue > 0):
                running_total_mass += 100 * var.varValue

        return total_number, total_cost, running_total_mass


def add_random_foods():
    con = sql.connect('sr_legacy/sr_legacy.db')
    cur = con.cursor()
    cur.execute("SELECT food_id FROM food_des")
    food_list = cur.fetchall()
    food_list = random.sample(food_list, 300)

    food_ids = [f[0] for f in food_list]

    return food_ids.sort()

def main():
    josh = Person(name="josh", age=25, sex='m')

    food_ids = [1001, 1002]
    print(get_nutrition(josh, food_ids))
   
if __name__ == '__main__':
    main()
