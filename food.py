import sqlite3 as sql

class Food:
    def __init__(self, id, price, name = None, lower_req = None, target_req = None, upper_req = None):
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
