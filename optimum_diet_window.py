import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PySide2.QtGui import QFont

import database
import basic_foods
from gui_constants import *
from gui_helpers import *
from spartan import Optimizier, Person
from diet_model import DietModel
from ui_optimumdietwindow import Ui_OptimumDietWindow


class OptimumDietWindow(QMainWindow, Ui_OptimumDietWindow):
    def __init__(self, parent=None, person=None):
        super().__init__(parent=None)
        self.setupUi(self)

        self.person = person
        self.optimizier = Optimizier()
        self.optimizier.optimize_diet(self.person)
        self.populate_diet_table()
        self.optimizier.describe_solution()

        #self.resize(800, 600)
        self.show()

    def populate_diet_table(self):
        prices = [
            food.price if food.price is not None else 1 for food in self.person.foods]


        lp_variables = self.optimizier.lp_prob.variables()
        foods = []
        for i, var in enumerate(lp_variables):
            if (var.varValue is not None and var.varValue > 0):
                food_name = database.get_food_name(var.name)
                cost = round(float(prices[i]) * var.varValue, 2)
                quantity = round(100 * var.varValue, 2)
                foods.append({"name":food_name, "cost":cost,"quantity":quantity, "unit":'g'})

        foods.append({"name":"", "cost":"","quantity":"", "unit":""})

        num_value, cost_value, mass_value = self.optimizier.get_totals()
        foods.append({"name":str(num_value) + ' items of fod', "cost":cost_value, "quantity":mass_value, "unit":'g'})

        diet_model = DietModel(foods=foods)

        self.diet_view.setModel(diet_model)

if __name__ == "__main__":
    person = Person(19, 'm')

    app = QApplication(sys.argv)
    window = OptimumDietWindow(person=person)
    sys.exit(app.exec_())