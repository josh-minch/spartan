import spartan
import basic_foods
import constants
from timeit import default_timer

if __name__ == '__main__':
    person = spartan.Person('m', 1993, 12, 1)
    type_res = spartan.Restriction('type_res.csv')
    fd_res = spartan.Restriction('fd_res.csv')

    person.remove_nut('Water')

    #food_ids = basic_foods.food_ids
    #food_ids = spartan.get_food_ids(2000)
    food_ids = spartan.get_all_food_ids()

    for food_id in food_ids:
        person.foods.append(spartan.Food(food_id=food_id))

    optimizer = spartan.Optimizier(person, type_res, fd_res)
    start = default_timer()
    optimizer.optimize_diet()
    print(default_timer() - start)
    optimizer.describe_solution()

