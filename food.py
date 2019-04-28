class Food:
    def __init__(self, name, id, nutrition):
        self.name = name
        self.id = id
        self.nutrition = self.get_nutrition()

    def get_nutrition(self):
        con = sql.connect('sr28.db')
        cur = con.cursor()
        cur.execute("SELECT nut_value FROM nut_data where food_id = ?", [self.id])
        nut_values = cur.fetchall()

        for i in range(len(nut_values)):
            nut_values[i] = nut_values[i][0]

        return nut_values


from collections import namedtuple

Food = namedtuple('Food', 'name id nutrition')
