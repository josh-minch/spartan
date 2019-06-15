import sqlite3 as sql
import numpy as np
from pulp import *
from person import Person
import query


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
    food_constraints = [f for f in food_amount if f.name in ['1077', '15265']]
    for food in food_constraints:
        prob += food == 2

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
