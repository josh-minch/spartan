from pulp import LpProblem, LpMinimize, LpVariable, LpContinuous
from operator import le, eq, ge

lp_prob = LpProblem("Diet", sense=LpMinimize)

var1 = LpVariable('sup', 0, None, LpContinuous)
var2 = LpVariable('bro', 0, None, LpContinuous)

def add_constraint(lp_prob, var, comparator, constraint_value):
    lp_prob += comparator(var, constraint_value)

add_constraint(lp_prob, var1, ge, 100)

lp_prob.solve()