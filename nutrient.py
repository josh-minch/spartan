class Nutrient:
    def __init__(self, name, id = None, lower_req = None, target_req = None, upper_req = None):
        self.name = name
        self.id = id
        self.lower_req = lower_req
        self.target_req = target_req
        self.upper_req = upper_req
