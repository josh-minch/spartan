# Each Nutrient for a given Person has a short name, id, and optional requirements.
# req_eq is a requirement that must be satisfied to equality. For example, a diet with Calories = 2000
# req_min is a minumum requirement. For example, a diet with Calcium >= 1000 mg
# req_max is a maximum requirement. This corresponds to tolerable upper intakes as specified in the DRI.
# For example, a diet with Calcium <= 3000 mg

class Nutrient:
        def __init__(self, name, id, req_eq, req_min, req_max):
            self.name = name
            self.id = id
            self.req_eq = req_eq
            self.req_min = req_min
            self.req_max = req_max
