import req_data
from nutrient import Nutrient

class Person:
    def __init__(self, age, sex, activity_level):
        assert isinstance(age, (int, float)), "Age must be a number"
        assert sex in {'f', 'm', 'c', 'l', 'p'}, "Select female, male, child, lactating, or pregnant"
        self.age = age
        self.sex = sex
        self.activity_level = activity_level

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

    # Add or remove nutrients by which to optimize diet
    
    def add_nut(self, Nutrient):
        if (Nutrient.id == None):
            nut_index = req_data.nut_names.index(Nutrient.name)
            Nutrient.id = req_data.nut_ids[nut_index]

        self.nuts.append(Nutrient)
        self.nuts.sort(key=lambda x: x.id)
        
    def remove_nut(self, nut_to_delete):
        self.nuts = [n for n in self.nuts if n.name not in nut_to_delete] 
    
    def add_foods(self, food_ids):
        for food in food_ids:
            if food not in self.food_ids:
                self.food_ids += [food]

        self.food_ids.sort(key=int)

    def remove_foods(self, food_ids):
        for food in food_ids:
            if food not in self.food_ids:
                self.food_ids -= [food]
    
