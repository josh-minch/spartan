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
import nutrition_model
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

        self.resize(1400, 700)
        self.show()

    def populate_title(self):
        self.diet_label.setText(self.optimizier.get_solution_status())

    def populate_diet_table(self):
        foods = self.optimizier.get_diet_report()

        foods.append({"name":"", "cost":"","quantity":"", "unit":""})

        num_value, cost_value, mass_value = self.optimizier.get_totals()
        foods.append({"name":str(num_value) + ' items of food', "cost":cost_value, "quantity":mass_value, "unit":'g'})

        self.diet_model = DietModel(foods=foods)
        self.diet_view.setModel(self.diet_model)
        self.diet_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def populate_nutrition_table(self):
        (food_ids, food_amounts) = self.optimizier.get_data_for_nutrition_lookup()
        macros, vits, minerals = spartan.get_nutrition(self.person, food_ids, food_amounts)

        macros_model = nutrition_model.MacroModel(nutrients=macros)
        vits_model = nutrition_model.VitModel(nutrients=vits)
        minerals_model = nutrition_model.MineralModel(nutrients=minerals)

        self.macros_view.setModel(macros_model)
        self.vits_view.setModel(vits_model)
        self.minerals_view.setModel(minerals_model)

        self.macros_view.setItemDelegate(ProgressBarDelegate(self))
        self.vits_view.setItemDelegate(ProgressBarDelegate(self))
        self.minerals_view.setItemDelegate(ProgressBarDelegate(self))

        self.setup_nutrition()

    def setup_nutrition(self):
        set_column_widths(self.macros_view, nut_col_to_attr.keys(), nut_col_widths)
        set_column_widths(self.vits_view, nut_col_to_attr.keys(), nut_col_widths)
        set_column_widths(self.minerals_view, nut_col_to_attr.keys(), nut_col_widths)

        set_view_header_weights(self.macros_view, QFont.DemiBold)
        set_view_header_weights(self.vits_view, QFont.DemiBold)
        set_view_header_weights(self.minerals_view, QFont.DemiBold)

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
    person = spartan.Person(19, 'm')

    app = QApplication(sys.argv)
    window = OptimumDietWindow(person=person)
    sys.exit(app.exec_())