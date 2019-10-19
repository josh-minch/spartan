import spartan
import basic_foods
import constants
from timeit import default_timer

if __name__ == '__main__':
    person = spartan.Person('m', 1993, 12, 1)
    food_ids = basic_foods.food_ids
    #food_ids = spartan.get_all_food_ids()

    for food_id in food_ids:
        person.foods.append(spartan.Food(food_id=food_id))

    optimizer = spartan.Optimizier(person)
    start = default_timer()
    optimizer.optimize_diet()
    print(default_timer() - start)
    optimizer.describe_solution()

