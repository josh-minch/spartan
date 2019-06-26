import sqlite3 as sql
import req_data, basic_foods, query, random, time
import numpy as np
from pulp import *
from timeit import default_timer as timer

MAX_FOOD_ID_LEN = 5

class Person:
    def __init__(self, name, age, sex):
        assert isinstance(age, (int, float)), "Age must be a number"
        assert sex in {'f', 'm', 'c', 'l', 'p'}, "Select female, male, child, lactating, or pregnant"
        self.name = name
        self.age = age
        self.sex = sex
        #self.activity_level = activity_level

        self.age_range = self.set_age_range()
        self.nuts = []
        self.foods = []

        self.set_nuts()

    def create_user_db(self):
        con = sql.connect(self.name)
        cur = con.cursor()
        cur.execute("CREATE TABLE foods (food_id INT)")

        con.commit()
        con.close()

    def add_food_to_db(self, food_id):
        con = sql.connect(self.name)
        cur = con.cursor()
        cur.execute("INSERT INTO table (food_id) VALUES (?)", [food_id])

    def remove_food_from_db(self, food_id):
        pass
        
    def set_age_range(self):
        for i, ar in enumerate(req_data.age_range):
            if self.age < ar: 
                return req_data.age_range[i-1]

    def set_nuts(self):
        nuts = [ Nutrient(name, id, min) for (id, name, min) 
        in zip(req_data.nut_ids, req_data.nut_names, req_data.min[(self.age_range, self.sex)])]
  
        nuts.sort(key=lambda nut: nut.nut_id)
        self.nuts = nuts
        self.remove_nut('fl')
        self.add_nut(Nutrient('energy', 208, min=2000, max=2200))

    def add_nut(self, nutrient):
        if (nutrient.nut_id == None):
            nut_index = req_data.nut_names.index(nutrient.name)
            nutrient.id = req_data.nut_ids[nut_index]

        self.nuts.append(nutrient)
        self.nuts.sort(key=lambda nut: nut.nut_id)
        
    def remove_nut(self, nut_name):
        self.nuts = [nut for nut in self.nuts if nut.name not in nut_name]
   
    def add_foods(self, food_names=None, food_ids=None):
        if food_names is not None:
            for name in food_names:
                self.foods.append(Food(name=name))
        elif food_ids is not None:
            for food_id in food_ids:
                self.foods.append(Food(food_id=food_id))
        self.foods.sort(key = lambda f: f.food_id)

    def remove_foods(self, food_name):
        self.foods = [food for food in self.foods if food.name not in food_name] 

    def get_food_from_id_or_name(self, food_name=None, food_id=None):
        if food_name is not None:
            food = next(food for food in self.foods if food.name == food_name)
        elif food_id is not None:    
            food = next(food for food in self.foods if food.food_id == food_id)
        return food
    
    def set_food_constraint(self, constraint, constraint_value, food_name=None, food_id=None):
        food = self.get_food_from_id_or_name(food_name=food_name, food_id=food_id)
        setattr(food, constraint, constraint_value)
        
class Food:
    def __init__(self, food_id=None,  name=None, price=1, min=None, target=None, max=None):
        self.food_id = food_id or self.get_food_id(name)
        self.name = name or self.get_food_name(food_id)
        self.price = price
        self.min = min
        self.target = target
        self.max = max

    def get_nutrition(self):
        con = sql.connect('sr28.db')
        cur = con.cursor()
        cur.execute("SELECT nut_value FROM nut_data where food_id = ?", [self.food_id])
        nut_values = cur.fetchall()

        for i in range(len(nut_values)):
            nut_values[i] = nut_values[i][0]

        return nut_values

    def get_food_name(self, food_id):
        con = sql.connect('sr28.db')
        cur = con.cursor()
        cur.execute("SELECT food_name FROM food_des WHERE food_id = ?", [food_id])
        food_name = cur.fetchall()[0][0]

        return food_name
    
    def get_food_id(self, food_name):
        con = sql.connect('sr28.db')
        cur = con.cursor()
        cur.execute("SELECT food_id FROM food_des WHERE food_name = ?", [food_name])
        food_id = cur.fetchall()[0][0]

        return food_id

class Nutrient:
    def __init__(self, name, nut_id=None, min=None, target=None, max=None):
        self.name = name
        self.nut_id = nut_id
        self.min = min
        self.target = target
        self.max = max

class Optimizier:
    
    def make_nutrition_matrix(self, person):
        nut_ids = [nut.nut_id for nut in person.nuts]
        food_ids = [food.food_id for food in person.foods]

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

        food_ids = [food.food_id for food in person.foods]
        prices = [food.price for food in person.foods]

        self.food_quantity_vector = np.array(
            [LpVariable(str(food_id), 0, None, LpContinuous) for food_id in food_ids])

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
            if food.min is not None:
                self.lp_prob += self.food_quantity_vector[i] >= food.min
            if food.target is not None:
                self.lp_prob += self.food_quantity_vector[i] == food.target
            if food.max is not None:
                self.lp_prob += self.food_quantity_vector[i] <= food.max

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
        
    def describe_solution(self):

        print("Status: " + LpStatus[self.lp_prob.status])

        #if LpStatus[self.lp_prob.status] == 'Feasible':
        
        for v in self.lp_prob.variables():
            if (v.varValue is not None and v.varValue > 0):
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
    josh.add_foods(food_ids=food_ids)
    for food in food_ids:
        josh.set_food_price(food, 1)
    
    for food in josh.foods[:5]:
        food.min = 1

    josh.remove_nut(['fl'])

    josh.add_nut(Nutrient('DHA', 631, min = 0.3))
    josh.add_nut(Nutrient('EPA', 629, min = 0.3))
    josh.add_nut(Nutrient('energy', 208, min=2000))
    josh.add_nut(Nutrient('sat', 606, max=27))

    optimizier = Optimizier()
    start_time = time.time()
    optimizier.optimize_diet(josh)
    print("--- %s seconds ---" % (time.time() - start_time))
    optimizier.describe_solution()
   

if __name__ == '__main__':
   
    main()
   

'''
Structure I'm thinking of

    input = get_user_input()
    user = Person()
    user.name = input.name
    user.lifestage = user.lifestage 
    user.select_nutrients
        user.calculate_req()
    
    groc_store = GroceryStore('stater_bros')
    fridge = Fridge(Person)
    groc_store.groceries = input.groceries
    fridge.groceries = GroceryStore.groceries

    unformatted_data = query_nutritional_database(fridge, user)  //
    formatted_data = format_data(unformatted_data, fridge, user)
    optimize_diet(formatted_data, fridge, user)
'''
