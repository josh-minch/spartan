from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PySide2.QtGui import QFont

import database
from gui_constants import *
from gui_helpers import *
from spartan import Optimizier
from ui_optimumdietwindow import Ui_OptimumDietWindow

class OptimumDietWindow(QMainWindow, Ui_OptimumDietWindow):
    def __init__(self, parent=None, person=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.optimizier = Optimizier()
        self.optimizier.optimize_diet(person)
        self.populate_optimum_diet_table(person)
        self.populate_optimum_diet_totals()
        self.optimizier.describe_solution()

        #self.resize(800, 600)
        self.show()

    def populate_optimum_diet_table(self, person):
        setup_table_header(self.optimum_diet_table, labels=[
                           'Food', 'Cost', 'Quantity'])

        self.diet_label.setText(self.optimizier.describe_solution_status())

        prices = [
            food.price if food.price is not None else 1 for food in person.foods]

        for i, var in enumerate(self.optimizier.lp_prob.variables()):
            if (var.varValue is not None and var.varValue > 0):
                current_row = self.optimum_diet_table.rowCount()
                self.optimum_diet_table.insertRow(current_row)

                food_name = QTableWidgetItem()
                food_name.setData(Qt.EditRole, database.get_food_name(var.name))
                self.optimum_diet_table.setItem(
                    current_row, OPT_NAME_COL, food_name)

                price = QTableWidgetItem()
                price.setData(Qt.EditRole, float(prices[i]) * var.varValue)
                self.optimum_diet_table.setItem(current_row, OPT_PRICE_COL, price)

                quantity = QTableWidgetItem()
                quantity.setData(Qt.EditRole, 100 * var.varValue)
                self.optimum_diet_table.setItem(
                    current_row, OPT_QUANTITY_COL, quantity)

    def populate_optimum_diet_totals(self):
        for i in range(2):
            current_row = self.optimum_diet_table.rowCount()
            self.optimum_diet_table.insertRow(current_row)

        totals_font = QFont()
        totals_font.setWeight(QFont.DemiBold)

        num_value, cost_value, mass_value = self.optimizier.get_totals()

        number_item = QTableWidgetItem()
        number_item.setFont(totals_font)
        number_item.setData(Qt.EditRole, str(num_value) + " items")
        self.optimum_diet_table.setItem(current_row, OPT_NAME_COL, number_item)

        cost_item = QTableWidgetItem()
        cost_item.setFont(totals_font)
        cost_item.setData(Qt.EditRole, cost_value)
        self.optimum_diet_table.setItem(current_row, OPT_PRICE_COL, cost_item)

        mass_item = QTableWidgetItem()
        mass_item.setFont(totals_font)
        mass_item.setData(Qt.EditRole, mass_value)
        self.optimum_diet_table.setItem(current_row, OPT_QUANTITY_COL, mass_item)