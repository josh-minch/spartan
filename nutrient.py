import sqlite3 as sql
import numpy as np
from pulp import *
from timeit import default_timer as timer

import req_data
import basic_foods

MAX_FOOD_ID_LEN = 5

class Database:
    def __init__(self, name):
        con = sql.connect(name)
        cur = con.cursor()

class Person:
    def __init__(self, age, sex, activity_level):
        assert isinstance(age, (int, float)), "Age must be an int"
        assert sex in {'f', 'm', 'c', 'l', 'p'}, "Select female, male, child, lactating, or pregnant"
        self.age = age
        self.sex = sex
        self.activity_level = activity_level
        self.age_range = self.set_age_range()
        
        # List of tuples nutrients by which to optimize diet
        # (nutrient id, nutrient name, nutrient requirement)
        self.nut = self.set_nut()

        # List of foods available to user 
        # TODO: Make tuple with associated price
        self.food_ids = []

    def set_age_range(self):
        for i, ar in enumerate(req_data.age_range):
            if self.age < ar: 
                return req_data.age_range[i-1]

    def set_nut(self):

        nut = [ (id, name, req, 'lower') for (id, name, req) in zip(req_data.nut_ids, req_data.nut_names, 
        req_data.req[ (self.age_range, self.sex)]) ]
        
        nut.sort()

        return nut

    # Add or remove nutrients by which to optimize diet
    
    def add_nut(self, nut_id, nut_name, req_value, req_constraint = 'lower'):

        if (nut_id == None):
            nut_index = req_data.nut_names.index(nut_name)
            nut_id = req_data.nut_ids[nut_index]
            if (req_value == None):
                req_value = req_data.req[(self.age_range, self.sex)][nut_index]

        self.nut.append((nut_id, nut_name, req_value, req_constraint))
        self.nut.sort()
        
    def remove_nut(self, nut_to_delete):
        self.nut = [n for n in self.nut if n[1] not in nut_to_delete] 

    def add_foods(self, food_ids):
        for food in food_ids:
            if food not in self.food_ids:
                self.food_ids += [food]

        self.food_ids.sort(key=int)

    def remove_foods(self, food_ids):
        for food in food_ids:
            if food not in self.food_ids:
                self.food_ids -= [food]
    
    # Give cheapest diet from list of foods that meets person's rdi nutrients in nut_ids
    '''
    def construct_nut_matrix(self)
        return matrix
    def optimize_diet(matrix)
        return sol
    ''' 
    def optimize_diet(self):
        
        con = sql.connect('sr28.db')
        cur = con.cursor()

        nut_values = np.zeros([len(self.food_ids), len(self.nut)])
        nut_ids = [i for (i, n, r, c) in self.nut]
        
        # Get nutritional values for each of the nutrients for each user's food.
        cur.execute('''select nut_value from nut_data where food_id in \
        (''' + (len(self.food_ids) - 1) * '?, ' + '?) and nut_id in \
        (''' + (len(nut_ids) - 1) * '?, ' + '?) order by food_id, nut_id''', self.food_ids + nut_ids)

        fetch_data = cur.fetchall()

        # Construct nut_values matrix where each row is a food and each col is a nutrient
        fetch_data = np.array([float(d[0]) for d in fetch_data])
        nut_values = fetch_data.reshape(len(self.food_ids), len(self.nut))

        A = np.transpose(nut_values)
        b = [r for (i, n, r, c) in self.nut]
        c =  1 * np.ones(len(self.food_ids))
        
        prob = LpProblem("Diet", sense = LpMinimize)
        
        x = np.array([LpVariable("food " + format(i).zfill(MAX_FOOD_ID_LEN), 0, None, LpContinuous) for i in self.food_ids])

        start1 = timer()

        prob += lpSum(c * x), "Total cost of foods"
        for i in range(len(A)):
            if self.nut[i][3] == 'lower':
                prob += lpSum(A[i] * x) >= b[i]
            elif self.nut[i][3] == 'equality':
                prob += lpSum(A[i] * x) == b[i]
            elif self.nut[i][3] == 'upper':
                prob += lpSum(A[i] * x) <= b[i]
            
        for i in range(len(x)):
            prob += x[i] >= 0

        end1 = timer()
        print("Adding constraints took " + str(end1 - start1))
        
        prob.writeLP("DietModel.lp")

        start2 = timer()

        print(prob.solve())

        end2 = timer()
        print("Solving took " + str(end2 - start2))

        return prob

def search_food(food_name):
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT food_name FROM food_des where food_name LIKE ? ", [food_name + '%'])
    food_list = cur.fetchall()
    cur.execute("SELECT food_name FROM food_des where food_name LIKE ? ", ['%' + food_name])
    food_list += cur.fetchall()
    cur.execute("SELECT food_name FROM food_des where food_name LIKE ? ", ['%' + food_name + '%'])
    food_list += cur.fetchall()

    for i in range(len(food_list)):
        food_list[i] = food_list[i][0]

    return food_list

def describe_food(food_id):
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT nut_value FROM nut_data where food_id = ?", [food_id])
    nut_values = cur.fetchall()

    for i in range(len(nut_values)):
        nut_values[i] = nut_values[i][0]

    return nut_values

def name_food(food_id):
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT food_name FROM food_des where food_id = ?", [food_id])
    food_name = cur.fetchall()

    for i in range(len(food_name)):
        food_name = food_name[i][0]

    return food_name
    
def list_foods(food_ids):
    for f in food_ids:
        print( str(format(f).zfill(MAX_FOOD_ID_LEN)) + " - " + name_food(f) )

import random 

def main():
    
    josh = Person(24, 'm', 'light')
    
    # Add random foods
    con = sql.connect('sr28.db')
    cur = con.cursor()
    cur.execute("SELECT food_id FROM food_des")
    food_list = cur.fetchall()
    food_list = random.sample(food_list, 950)

    food_ids = [f[0] for f in food_list]
    #josh.add_foods(food_ids) 

    food_ids = basic_foods.food
    list_foods(food_ids)
    josh.add_foods(food_ids)

    #josh.remove_nut(req_data.vit_nut_names + req_data.min_nut_names)
    josh.remove_nut(['fl'])
    #josh.remove_nut(['lin'])
    #josh.remove_nut(['alpha-lin'])
    #josh.remove_nut(req_data.nut_names)
    #josh.add_nut(618, 'lin', 20, 'upper')
    #josh.add_nut(619, 'alpha-lin', 5, 'lower')
    josh.add_nut(621, 'DHA', 2, 'lower')
    josh.add_nut(629, 'EPA', 2, 'lower')
    
    josh.add_nut(208, 'energy', 1800, 'upper')
    josh.add_nut(606, 'sat', 40, 'upper')
    
    prob = josh.optimize_diet()
  
    for i, v in enumerate(prob.variables()):
        if (v.varValue != 0):
            print(name_food(josh.food_ids[i]), "=", 100 * v.varValue)

    print("Total Cost of Food = ", 100 * value(prob.objective)) 
    
    
    # PulP giving worse solutions with inclusion of more food vhoices. Try adding lettuce, cos or romaine and seeing resukt
    # Changing calories to upper constraint instead of equality gave gave same sol.
    # However, still not meeting daily requirments for several nutrients like vit b12. Why salmon reccomend so low?
if __name__ == '__main__':
    main()