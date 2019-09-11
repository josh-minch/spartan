import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PySide2.QtGui import QFont

import spartan
import database
import basic_foods
from gui_constants import *
from gui_helpers import *
from diet_model import DietModel
from nutrition_model import NutritionTableModel
from progress_bar_delegate import ProgressBarDelegate
from ui_optimumdietwindow import Ui_OptimumDietWindow


class OptimumDietWindow(QMainWindow, Ui_OptimumDietWindow):
    def __init__(self, parent=None, person=None):
        super().__init__(parent=None)
        self.setupUi(self)

        self.person = person
        self.optimizier = spartan.Optimizier(self.person)
        self.optimizier.optimize_diet()
        self.optimizier.describe_solution()
        self.populate_title()
        self.populate_diet_table()
        self.populate_nutrition_table()


        #self.resize(800, 600)
        self.show()

    def populate_title(self):
        self.diet_label.setText(self.optimizier.get_solution_status())

    def populate_diet_table(self):
        foods = self.optimizier.get_diet_report()

        foods.append({"name":"", "cost":"","quantity":"", "unit":""})

        num_value, cost_value, mass_value = self.optimizier.get_totals()
        foods.append({"name":str(num_value) + ' items of food', "cost":cost_value, "quantity":mass_value, "unit":'g'})

        self.diet_model = DietModel(foods=foods)
        self.diet_view.setModel(diet_model)

    def populate_nutrition_table(self):
        (food_ids, food_amounts) = self.optimizier.get_data_for_nutrition_lookup()

        nutrients = spartan.get_nutrition(self.person, food_ids, food_amounts)
        nutrition_model = NutritionTableModel(nutrients=nutrients)

        progress_bar_delegate = ProgressBarDelegate(self)
        self.nutrition_view.setItemDelegate(progress_bar_delegate)

        self.nutrition_view.setModel(nutrition_model)

    def display_selected_food_nutrition(self):
        amounts = []
        for row in range(self.diet_.rowCount()):
            index = self.fridge_selected_model.index(row, S_AMOUNT_COL)
            amounts.append(self.fridge_selected_model.data(index))

        nutrients = get_nutrition(self.person, self.selected_food_ids, amounts)
        nutrition_model = NutritionTableModel(nutrients=nutrients)
        self.nutrition_view.setModel(nutrition_model)

        progress_bar_delegate = ProgressBarDelegate(self)
        self.nutrition_view.setItemDelegate(progress_bar_delegate)


if __name__ == "__main__":
    person = Person(19, 'm')

    app = QApplication(sys.argv)
    window = OptimumDietWindow(person=person)
    sys.exit(app.exec_())