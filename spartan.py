import sqlite3 as sql
import req, basic_foods, database, random, time
import numpy as np
from pulp import *
from timeit import default_timer as timer
import os.path

MAX_FOOD_ID_LEN = 5
        
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
            'SELECT id, name, price, min, max, target '
            'FROM foods'
        )

        for row in cur.execute(sql_stmt):
            self.foods.append(
                Food(food_id=row[0], name=row[1], price=row[2], min=row[3], max=row[4], target=row[5]))

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
            'INSERT INTO foods(name, id) '
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
            'WHERE id = ?'
        )

        cur.executemany(sql_stmt, foods_tuple)
        con.commit()
        con.close()

    def update_attr_in_db(self, attr, attr_value, food_name):
        con = sql.connect("spartan.db")
        cur = con.cursor()
       
        # attr comes from our dict of attr strings, so no need to sanitize
        sql_stmt = (
            'UPDATE foods '
            'SET ' + attr + ' = ?'
            'WHERE name = ?'
        )

        cur.execute(sql_stmt, [attr_value] + [food_name])
        con.commit()
        con.close()

    # Calculate the equivalent daily value percentage of a given nutrient amount
    # based on a person's nutrient requirements. 

class Food:
    def __init__(self, food_id=None, name=None, price=None, min=None, target=None, max=None):
        self.food_id = food_id if food_id is not None else database.get_food_id(name)
        self.name = name or database.get_food_name(food_id)
        self.price: float = price
        self.min: float = min
        self.target: float = target
        self.max: float = max

        self.price_quantity = 100
        self.price_unit = 'g'
        self.min_unit = 'g'
        self.max_unit = 'g'
        self.target_unit = 'g'

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

    def convert_quantity(self, quantity, old_unit, new_unit):

        con = sql.connect('sr_legacy/sr_legacy.db')
        cur = con.cursor()
        sql_stmnt = (
            'SELECT gm_weight'
            'FROM weight'
            'WEHERE food_id = ? AND description = ?'
        )

        if old_unit == 'g':
            cur.execute(sql_stmnt, self.food_id, [new_unit])
            unit_scale_factors = cur.fetchall()
            return quantity * (1 / unit_scale_factors[1][0])
        else:
            cur.execute(sql_stmnt, self.food_id, [old_unit, new_unit])
            unit_scale_factors = cur.fetchall()
            return quantity * (unit_scale_factors[0][0] / unit_scale_factors[1][0])

    def get_nutrition(self, person):
        con = sql.connect('sr_legacy/sr_legacy.db')
        cur = con.cursor()

        # Get nutrient and amount
        nut_ids = [nut.nut_id for nut in person.nuts]
        nut_ids = tuple(nut_ids)
        sql_stmt = (
            'SELECT nut_id, amount '
            'FROM nut_data WHERE food_id = ? AND nut_id IN '+ str(nut_ids)
        )
        cur.execute(sql_stmt, [self.food_id])
        nutrition = cur.fetchall()
        nutrition = [(req.nuts[n[0]], n[1]) for n in nutrition]

        # Get nutrient's corresponding unit
        sql_stmt = (
            'SELECT units '
            'FROM nutr_def WHERE id IN '+ str(nut_ids)
        )
        cur.execute(sql_stmt)
        units = cur.fetchall()

        daily_value = []
        for nut in nutrition:
            daily_value.append(self.calculate_dv(person, nut[0], nut[1]))

        nutrition = [{'name': n[0], 'amount': n[1], 'unit': u[0], 'percent': d}
                      for (n, u, d) in zip(nutrition, units, daily_value)]

        return nutrition

    def calculate_dv(self, person, nutrient_name, nutrient_amount):
        if nutrient_amount is None:
            return None
            
        [min_value] = [nut.min for nut in person.nuts if nut.name == nutrient_name]

        return round(100 * (nutrient_amount / min_value), 1)

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

        data = cur.fetchall()
        self.nutrition_matrix = self.format_nutrition_matrix(data, person)

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
            if food.min is not None:
                if food.min_unit != 'g':
                    min_value = food.convert_quantity(food.min, food.min_unit, 'g')
                else:
                    min_value = food.min
                self.lp_prob += self.food_quantity_vector[i] >= min_value / 100
            if food.max is not None:
                if food.max_unit != 'g':
                    max_value = food.convert_quantity(food.max, food.max_unit, 'g')
                else:
                    max_value = food.max
                self.lp_prob += self.food_quantity_vector[i] <= max_value / 100
            if food.target is not None:
                if food.min_unit != 'g':
                    target_value = food.convert_quantity(food.target, food.target_unit, 'g')
                else:
                    target_value = food.target
                self.lp_prob += self.food_quantity_vector[i] == target_value / 100

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

    food_ids = basic_foods.food

    with open('fridge.txt', 'w') as file:
        for f in food_ids:
            file.write(str(format(f).zfill(MAX_FOOD_ID_LEN)) + " - " + database.get_food_name(f) + '\n')
    
    prices = len(food_ids) * [1]
    josh.add_foods(food_ids=food_ids)
    for food in food_ids:
        josh.set_food_price(food, 1)
    
    for food in josh.foods[:5]:
        food.min = 1

    josh.remove_nut(['fl'])

    josh.add_nut(Nutrient('DHA', 631, min = 0.3))
    josh.add_nut(Nutrient('EPA', 629, min = 0.3))
    josh.add_nut(Nutrient('energy', 208, min=2000, max=2500))
    josh.add_nut(Nutrient('sat', 606, max=27))

    optimizier = Optimizier()
    start_time = time.time()
    optimizier.optimize_diet(josh)
    print("--- %s seconds ---" % (time.time() - start_time))
    optimizier.describe_solution()
   
if __name__ == '__main__':
    main()
