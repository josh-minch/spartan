import sqlite3 as sql
import req_data, basic_foods, query, random, time
import numpy as np
from pulp import *
from timeit import default_timer as timer

MAX_FOOD_ID_LEN = 5

class Person:
    def __init__(self, age, sex):
        assert isinstance(age, (int, float)), "Age must be a number"
        assert sex in {'f', 'm', 'c', 'l', 'p'}, "Select female, male, child, lactating, or pregnant"
        self.age = age
        self.sex = sex
        #self.activity_level = activity_level

        self.age_range = self.set_age_range()
        self.nuts = self.set_nuts()
        self.foods = []

    def set_age_range(self):
        for i, ar in enumerate(req_data.age_range):
            if self.age < ar: 
                return req_data.age_range[i-1]

    def set_nuts(self):
        nuts = [ Nutrient(name, id, lower_req) for (id, name, lower_req) 
        in zip(req_data.nut_ids, req_data.nut_names, req_data.lower_req[(self.age_range, self.sex)])]
        
        nuts.sort(key=lambda x: x.id)
        return nuts

    def add_nut(self, nutrient):
        if (nutrient.id == None):
            nut_index = req_data.nut_names.index(nutrient.name)
            nutrient.id = req_data.nut_ids[nut_index]

        self.nuts.append(nutrient)
        self.nuts.sort(key=lambda x: x.id)
        
    def remove_nut(self, nut_name):
        self.nuts = [nut for nut in self.nuts if nut.name not in nut_name] 
   
    def add_foods(self, food_ids, prices=None):
        for food_id, price in zip(food_ids, prices):
            self.foods.append(Food(food_id, price=price))
        self.foods.sort(key = lambda f: f.id)

    def remove_foods(self, food_name):
        self.foods = [food for food in self.foods if food.name not in food_name] 


class Food:
    def __init__(self, id, price=None, name=None, lower_req=None, target_req=None, upper_req=None):
        self.id = id
        self.price = price
        self.name = name or self.get_food_name()
        self.lower_req = lower_req
        self.target_req = target_req
        self.upper_req = upper_req

    def get_nutrition(self):
        con = sql.connect('sr28.db')
        cur = con.cursor()
        cur.execute("SELECT nut_value FROM nut_data where food_id = ?", [self.id])
        nut_values = cur.fetchall()

        for i in range(len(nut_values)):
            nut_values[i] = nut_values[i][0]

        return nut_values

    def get_food_name(self):
        con = sql.connect('sr28.db')
        cur = con.cursor()
        cur.execute("SELECT food_name FROM food_des where food_id = ?", [self.id])
        food_name = cur.fetchall()

        for i in range(len(food_name)):
            food_name = food_name[i][0]

        return food_name

class Nutrient:
    def __init__(self, name, id=None, lower_req=None, target_req=None, upper_req=None):
        self.name = name
        self.id = id
        self.lower_req = lower_req
        self.target_req = target_req
        self.upper_req = upper_req

class Optimizier:
    def __init__(self):
        self.lp_prob = None
        self.food_quantity_vector = None
        self.nutrition_matrix = None
        self.optimum_solution = None
    
    def make_nutrition_matrix(self, person):
        nut_ids = [nut.id for nut in person.nuts]
        food_ids = [food.id for food in person.foods]

        con = sql.connect('sr28.db')
        cur = con.cursor()

        # Get nutritional values for each of the nutrients for each user's food.
        # The len(food_ids)-1 are to programmatically generate a SQL statement with 
        # a variable length number of parameters, since food_ids and nut_ids vary depending on user settings
        cur.execute('''select nut_value from nut_data where food_id in \
        (''' + (len(food_ids) - 1) * '?, ' + '?) and nut_id in \
        (''' + (len(nut_ids) - 1) * '?, ' + '?) order by food_id, nut_id''', food_ids + nut_ids)

        unformatted_data = cur.fetchall()
        self.nutrition_matrix = self.format_nutrition_matrix(unformatted_data, person)
        
    def format_nutrition_matrix(self, unformatted_data, person):
        # Construct formatted matrix where each row is a food and each col is a nutrient
        unformatted_data = np.array([float(d[0]) for d in unformatted_data])
        unformatted_data = unformatted_data.reshape(len(person.foods), len(person.nuts))

        formatted_data = np.transpose(unformatted_data)
        return formatted_data

    def construct_lp_problem(self, person):
        self.lp_prob = LpProblem("Diet", sense=LpMinimize)

        food_ids = [food.id for food in person.foods]
        prices = [food.price for food in person.foods]

        self.food_quantity_vector = np.array(
        [LpVariable(str(id), 0, None, LpContinuous) for id in food_ids])

        self.lp_prob += lpSum(prices * self.food_quantity_vector), "Total cost of foods"

    def add_food_constraints(self, person):

        # Add food quantity constraint
        #food_constraints = [f for f in food_amount if f.name in ['1077', '15265']]
        #for food in food_constraints:
        #    self.lp_prob += food == 2

        # Add cost constraint
        #self.lp_prob += lpSum(prices * food_amount) >= 1000 / 100

        # Add food quantity constraint
        #self.lp_prob += food_amount[0] >= 100 / 100

        for i, food in enumerate(person.foods):
            self.lp_prob += self.food_quantity_vector[i] >= 0
            if food.lower_req is not None:
                self.lp_prob += self.food_quantity_vector[i] >= food.lower_req
            if food.target_req is not None:
                self.lp_prob += self.food_quantity_vector[i] == food.target_req
            if food.upper_req is not None:
                self.lp_prob += self.food_quantity_vector[i] <= food.upper_req

    def add_nutrient_constraints(self, person):
        lower_reqs = [nut.lower_req for nut in person.nuts]
        target_reqs = [nut.target_req for nut in person.nuts]
        upper_reqs = [nut.upper_req for nut in person.nuts]

        for i in range(len(self.nutrition_matrix)):
            if lower_reqs[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) >= lower_reqs[i]
            if target_reqs[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) == target_reqs[i]
            if upper_reqs[i] is not None:
                self.lp_prob += lpSum(self.nutrition_matrix[i] * self.food_quantity_vector) <= upper_reqs[i]

    def optimize_diet(self, person):
        
        self.make_nutrition_matrix(person)
        self.construct_lp_problem(person)
        self.add_nutrient_constraints(person)
        self.add_food_constraints(person)

        self.lp_prob.writeLP("DietModel.lp")
        self.lp_prob.solve()
        
    def describe_solution(self):

        print("Status: " + LpStatus[self.lp_prob.status])

        for v in self.lp_prob.variables():
            if (v.varValue != 0):
                print(query.get_food_name(v.name), "=", 100 * v.varValue)

        print(100 * value(self.lp_prob.objective), "total grams of food")

def add_random_foods():
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT food_id FROM food_des")
    food_list = cur.fetchall()
    food_list = random.sample(food_list, 300)

    food_ids = [f[0] for f in food_list]

    return food_ids.sort()

def main():
    josh = Person(25, 'm')

    food_ids = basic_foods.food

    with open('fridge.txt', 'w') as file:
        for f in food_ids:
            file.write(str(format(f).zfill(MAX_FOOD_ID_LEN)) + " - " + query.get_food_name(f) + '\n')
    
    prices = len(food_ids) * [1]
    josh.add_foods(food_ids, prices)
    
    for food in josh.foods[:5]:
        food.lower_req = 1

    josh.remove_nut(['fl'])

    josh.add_nut(Nutrient('DHA', 631, lower_req = 0.3))
    josh.add_nut(Nutrient('EPA', 629, lower_req = 0.3))
    josh.add_nut(Nutrient('energy', 208, lower_req=2000))
    josh.add_nut(Nutrient('sat', 606, upper_req=27))

    optimizier = Optimizier()
    start_time = time.time()
    optimizier.optimize_diet(josh)
    print("--- %s seconds ---" % (time.time() - start_time))
    optimizier.describe_solution()
   

if __name__ == '__main__':
   
    main()
   