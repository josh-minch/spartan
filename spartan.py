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

        # List of foods available to user 
        # TODO: Make tuple with associated price
        self.food_ids = []

    def set_age_range(self):
        for i, ar in enumerate(req_data.age_range):
            if self.age < ar: 
                return req_data.age_range[i-1]

    def set_nuts(self):
        nuts = [ Nutrient(name, id, lower_req) for (id, name, lower_req) 
        in zip(req_data.nut_ids, req_data.nut_names, req_data.lower_req[ (self.age_range, self.sex)]) ]
        
        nuts.sort(key=lambda x: x.id)
        return nuts

    def add_nut(self, Nutrient):
        if (Nutrient.id == None):
            nut_index = req_data.nut_names.index(Nutrient.name)
            Nutrient.id = req_data.nut_ids[nut_index]

        self.nuts.append(Nutrient)
        self.nuts.sort(key=lambda x: x.id)
        
    def remove_nut(self, nut_to_delete):
        self.nuts = [n for n in self.nuts if n.name not in nut_to_delete] 
   
    def add_food(self, food_id):
        self.foods.append(Food(food_id))
        self.foods.sort(key = lambda x: x.id)

    def remove_foods(self, food_ids):
        for food in food_ids:
            if food not in self.food_ids:
                self.food_ids -= [food]

class Food:
    def __init__(self, id, price = None, name = None, lower_req = None, target_req = None, upper_req = None):
        self.id = id
        self.price = price
        self.name = self.get_food_name()
        self.lower_req = lower_req
        self.target_req = target_req
        self.upper_req = upper_req
        self.nutrition = self.get_nutrition()

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
    def __init__(self, name, id = None, lower_req = None, target_req = None, upper_req = None):
        self.name = name
        self.id = id
        self.lower_req = lower_req
        self.target_req = target_req
        self.upper_req = upper_req

def query_database(Person):
    nut_ids = [nut.id for nut in Person.nuts]
    food_ids = Person.food_ids

    con = sql.connect('sr28.db')
    cur = con.cursor()

    # Get nutritional values for each of the nutrients for each user's food.
    cur.execute('''select nut_value from nut_data where food_id in \
    (''' + (len(food_ids) - 1) * '?, ' + '?) and nut_id in \
    (''' + (len(nut_ids) - 1) * '?, ' + '?) order by food_id, nut_id''', food_ids + nut_ids)

    unformatted_data = cur.fetchall()
    return unformatted_data

def shape_data(unformatted_data, Person):
    nutrients = Person.nuts
    food_ids = Person.food_ids

    # Construct formatted matrix where each row is a food and each col is a nutrient
    unformatted_data = np.array([float(d[0]) for d in unformatted_data])
    unformatted_data = unformatted_data.reshape(len(food_ids), len(nutrients))

    formatted_data = np.transpose(unformatted_data)
    return formatted_data

def optimize_diet(formatted_data, Person, prices):

    lower_reqs = [nut.lower_req for nut in Person.nuts]
    target_reqs = [nut.target_req for nut in Person.nuts]
    upper_reqs = [nut.upper_req for nut in Person.nuts]
    food_ids = Person.food_ids

    prob = LpProblem("Diet", sense=LpMinimize)

    food_amount = np.array(
       [LpVariable(str(id), 0, None, LpContinuous) for id in food_ids])

    prob += lpSum(prices * food_amount), "Total cost of foods"
    for i in range(len(formatted_data)):
        if lower_reqs[i] is not None:
            prob += lpSum(formatted_data[i] * food_amount) >= lower_reqs[i]
        if target_reqs[i] is not None:
            prob += lpSum(formatted_data[i] * food_amount) == target_reqs[i]
        if upper_reqs[i] is not None:
            prob += lpSum(formatted_data[i] * food_amount) <= upper_reqs[i]

    for i in range(len(food_amount)):
        prob += food_amount[i] >= 0

    # Add food quantity constraint
    #food_constraints = [f for f in food_amount if f.name in ['1077', '15265']]
    #for food in food_constraints:
    #    prob += food == 2

    # Add cost constraint
    #prob += lpSum(prices * food_amount) >= 1000 / 100

    # Add food quantity constraint
    #prob += food_amount[0] >= 100 / 100

    prob.writeLP("DietModel.lp")
    prob.solve()

    return prob

def describe_solution(prob, Person):

    print("Status: " + LpStatus[prob.solve()])

    for v in prob.variables():
        if (v.varValue != 0):
            print(query.get_food_name(v.name), "=", 100 * v.varValue)

    print(100 * value(prob.objective), "total grams of food")

def main():
    josh = Person(25, 'm', 'light')
    
    # Add random foods
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT food_id FROM food_des")
    food_list = cur.fetchall()
    food_list = random.sample(food_list, 300)

    food_ids = [f[0] for f in food_list]

    food_ids = basic_foods.food
    food_ids.sort()
    '''for f in food_ids:
        print( str(format(f).zfill(MAX_FOOD_ID_LEN)) + " - " + query.get_food_name(f) )'''

    with open('fridge.txt', 'w') as file:
        for f in food_ids:
            file.write(str(format(f).zfill(MAX_FOOD_ID_LEN)) + " - " + query.get_food_name(f) + '\n')

    josh.add_foods(food_ids)

    josh.remove_nut(['fl'])

    josh.add_nut(Nutrient('DHA', 631, lower_req = 0.3))
    josh.add_nut(Nutrient('EPA', 629, lower_req = 0.3))
    josh.add_nut(Nutrient('energy', 208, lower_req=2000, upper_req= 2200))
    josh.add_nut(Nutrient('sat', 606, upper_req=27))

    prices =  1 * np.ones(len(josh.food_ids))

    query_time = time.time()
    unformatted_data = query_database(josh)
    print("--- %s seconds query ---" % (time.time() - query_time))
    
    formatted_data = shape_data(unformatted_data, josh)

    opt_time = time.time()
    prob = optimize_diet(formatted_data, josh, prices)
    print("--- %s seconds opt ---" % (time.time() - opt_time))

    describe_solution(prob, josh)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))