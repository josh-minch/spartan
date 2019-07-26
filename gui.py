import sys
import database
import user_db
from gui_constants import *
from spartan import Person, Food, Nutrient, Optimizier
from ui_mainwindow import Ui_MainWindow
from ui_optimum_diet_window import Ui_OptimumDietWindow
from PySide2.QtCore import Qt, QEvent
from PySide2.QtGui import QFont, QKeySequence
from PySide2.QtWidgets import (QApplication, QMainWindow, QListWidget, QTableWidget,
                               QListWidgetItem, QTableWidgetItem, QAbstractItemView, QHeaderView, QShortcut)

from PySide2 import QtCore, QtWidgets, QtGui

from timeit import default_timer as timer


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.person = Person('josh', 25, 'm')

        self.setup_connections()
        self.setup_filters()
        self.setup_selection_modes()
        self.setup_fridge()
        self.setup_nutrition()

        self.fridge_table.setShowGrid(False)

        self.search_box.setFocus()
        self.resize(1366, 768)
        self.show()

    def search_food(self):
        self.search_list.clear()
        search_result = database.search_food(self.search_box.text())
        self.search_list.addItems(search_result)

    def add_to_fridge(self):
        selected_items = [str(x.text())
                          for x in self.search_list.selectedItems()]
        for item in selected_items:
            current_row = self.fridge_table.rowCount()
            self.fridge_table.insertRow(current_row)
            self.fridge_table.setItem(current_row, 0, QTableWidgetItem(item))

        self.person.add_foods(food_names=selected_items)

    def remove_from_fridge(self):
        food_names_to_remove = []

        for item in self.fridge_table.selectedItems():
            food_names_to_remove.append(str(item.data(Qt.EditRole)))
            self.fridge_table.removeRow(item.row())

        self.person.remove_foods(food_names=food_names_to_remove)

    def setup_fridge(self):
        setup_table_header(self.fridge_table, labels=[
                           'Food', 'Price', 'Min', 'Max', 'Target'])

        for food in self.person.foods:
            current_row = self.fridge_table.rowCount()
            self.fridge_table.insertRow(current_row)

            for col, attr in col_to_attr.items():
                item = QTableWidgetItem()
                if col == PRICE_COL:
                    pass
                attr_val = getattr(food, attr)

                self.fridge_table.blockSignals(True)
                item.setData(Qt.EditRole, attr_val)
                self.fridge_table.setItem(current_row, col, item)
                self.fridge_table.blockSignals(False)

    def update_persons_food_attr(self, item):
        # Update food attributes, not food name
        if item.column() > NAME_COL:
            food_name = self.fridge_table.item(item.row(), 0).data(Qt.EditRole)
            attr = col_to_attr[item.column()]
            if item.data(Qt.EditRole) == "":
                self.person.set_food_attr(
                    attr, attr_value=None, food_name=food_name)
            else:
                self.person.set_food_attr(attr, attr_value=float(
                    item.data(Qt.EditRole)), food_name=food_name)

    def optimize(self):
        optimum_diet_window = OptimumDietWindow(self, person=self.person)
        optimum_diet_window.setAttribute(Qt.WA_DeleteOnClose)

    def setup_nutrition(self):
        setup_table_header(self.nutrition_table, [
                           'Nutrient', 'Quantity', 'Percent'])

    def display_nutrition(self, current, previous):
        # Check if incoming item is from the search_list or Food name column in fridge_table
        if isinstance(current, QListWidgetItem) or current.column() == NAME_COL:
            #self.nutrition_label.setText("Nutrition of selected item")

            self.nutrition_table.setRowCount(0)

            selected_food = Food(name=current.data(Qt.EditRole))
            nutrition = selected_food.get_nutrition(self.person)
            for nutrient in nutrition:
                current_row = self.nutrition_table.rowCount()
                self.nutrition_table.insertRow(current_row)
                self.nutrition_table.setItem(
                    current_row, 0, QTableWidgetItem(nutrient[0]))

                nutrient_quantity = QTableWidgetItem()
                if nutrient[1] is not None:
                    nutrient_quantity.setData(Qt.EditRole, nutrient[1])
                else:
                    nutrient_quantity.setData(Qt.EditRole, 'No data')
                self.nutrition_table.setItem(current_row, 1, nutrient_quantity)

    def toggle_add_btn(self):
        if self.search_selection_model.hasSelection():
            self.add_to_fridge_btn.setEnabled(True)
        else:
            self.add_to_fridge_btn.setEnabled(False)

    def toggle_remove_btn(self):
        if self.fridge_selection_model.hasSelection():
            self.remove_btn.setEnabled(True)
        else:
            self.remove_btn.setEnabled(False)

    def setup_selection_modes(self):
        # self.search_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #self.fridge_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        pass
        
    def setup_filters(self):
        self.search_list.installEventFilter(self)
        self.fridge_table.installEventFilter(self)

    def eventFilter(self, obj, event):
        # Press return in search_list to add item selected item to fridge
        if obj == self.search_list:
            if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
                self.add_to_fridge()
                return True
            else:
                return False
        # Press delete in fridge_table to remove selected
        elif obj == self.fridge_table:
            if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Delete:
                self.remove_from_fridge()
                return True
            else:
                return False
        else:
            # pass the event on to the parent class
            return QMainWindow.eventFilter(self, obj, event)

    def setup_connections(self):
        # Search panel connections
        self.search_box.returnPressed.connect(self.search_food)
        self.search_btn.clicked.connect(self.search_food)
        self.add_to_fridge_btn.clicked.connect(self.add_to_fridge)

        # Toggle add button
        self.search_selection_model = self.search_list.selectionModel()
        self.search_selection_model.selectionChanged.connect(self.toggle_add_btn)
        
        # Fridge panel connections
        self.fridge_table.itemChanged.connect(self.update_persons_food_attr)
        self.remove_btn.clicked.connect(self.remove_from_fridge)
        self.optimize_btn.clicked.connect(self.optimize)
        optimize_shortcut = QShortcut(QKeySequence(Qt.Key_F5), self)
        optimize_shortcut.activated.connect(self.optimize)

        # Toggle remove button
        self.fridge_selection_model = self.fridge_table.selectionModel()
        self.fridge_selection_model.selectionChanged.connect(self.toggle_remove_btn)

        # Nutriton panel connections
        self.search_list.currentItemChanged.connect(self.display_nutrition)
        self.fridge_table.currentItemChanged.connect(self.display_nutrition)

        # Debug 
        self.debug_btn.clicked.connect(self.print_debug_info)
        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        print([str(x.text()) for x in self.search_list.selectedItems()])
        print([str(x.text()) for x in self.fridge_table.selectedItems()])
        for food in self.person.foods:
            print(vars(food))


class OptimumDietWindow(QMainWindow, Ui_OptimumDietWindow):
    def __init__(self, parent=None, person=None):
        super().__init__(parent)
        self.setupUi(self)
        self.resize(1300, 900)

        self.optimizier = Optimizier()
        self.optimizier.optimize_diet(person)
        self.populate_optimum_diet_table(person)
        self.populate_optimum_diet_totals()
        self.optimizier.describe_solution()
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
                    current_row, NAME_COL, food_name)

                price = QTableWidgetItem()
                price.setData(Qt.EditRole, prices[i] * var.varValue)
                self.optimum_diet_table.setItem(current_row, PRICE_COL, price)

                quantity = QTableWidgetItem()
                quantity.setData(Qt.EditRole, 100 * var.varValue)
                self.optimum_diet_table.setItem(
                    current_row, QUANTITY_COL, quantity)

    def populate_optimum_diet_totals(self):
        for i in range(2):
            current_row = self.optimum_diet_table.rowCount()
            self.optimum_diet_table.insertRow(current_row)

        totals_font = QFont()
        totals_font.setBold(True)

        num_value, cost_value, mass_value = self.optimizier.get_totals()

        number_item = QTableWidgetItem()
        number_item.setFont(totals_font)
        number_item.setData(Qt.EditRole, str(num_value) + " items")
        self.optimum_diet_table.setItem(current_row, NAME_COL, number_item)

        cost_item = QTableWidgetItem()
        cost_item.setFont(totals_font)
        cost_item.setData(Qt.EditRole, cost_value)
        self.optimum_diet_table.setItem(current_row, PRICE_COL, cost_item)

        mass_item = QTableWidgetItem()
        mass_item.setFont(totals_font)
        mass_item.setData(Qt.EditRole, mass_value)
        self.optimum_diet_table.setItem(current_row, QUANTITY_COL, mass_item)


def setup_table_header(table, labels):
    header = table.horizontalHeader()
    table.setHorizontalHeaderLabels(labels)
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    for i in range(1, len(labels)):
        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

    header.setDefaultAlignment(Qt.AlignLeft) 

    header_font = QFont()
    header_font.setWeight(QFont.DemiBold)
    header.setFont(header_font)


if __name__ == "__main__":
    user_db.create_user_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
