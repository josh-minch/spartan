import sys
import ctypes
from timeit import default_timer as timer

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Qt, QEvent
from PySide2.QtGui import QFont, QKeySequence
from PySide2.QtWidgets import (QApplication, QMainWindow, QListWidget, QTableWidget,
                               QListWidgetItem, QTableWidgetItem, QAbstractItemView, QHeaderView, QShortcut)

from spartan import Person, Food, Nutrient, Optimizier
from gui_constants import *
import database
import user_db
from ui_mainwindow import Ui_MainWindow
from ui_optimum_diet_window import Ui_OptimumDietWindow
from ui_searchwindow import Ui_SearchWindow

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

        self.add_foods_btn.setFocus()
        self.move(30,30)
        self.resize(1366, 768)
        self.show()

    def remove_from_fridge(self):
        food_names_to_remove = []

        for item in self.fridge_table.selectedItems():
            food_names_to_remove.append(str(item.data(Qt.EditRole)))
            self.fridge_table.removeRow(item.row())

        self.person.remove_foods(food_names=food_names_to_remove)

    def setup_fridge(self):
        setup_table_header(self.fridge_table, labels=[
                           'Food', 'Price', 'Min', 'Max', 'Tar'])

        # Set vertical header height to determine table's row height
        v_header = self.fridge_table.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.Fixed)
        v_header.setDefaultSectionSize(V_HEADER_SIZE)

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

    def open_search_window(self):
        search_window = SearchWindow(self, person=self.person, fridge_table=self.fridge_table)
        search_window.setAttribute(Qt.WA_DeleteOnClose)

    def optimize(self):
        optimum_diet_window = OptimumDietWindow(self, person=self.person)
        optimum_diet_window.setAttribute(Qt.WA_DeleteOnClose)

    def setup_nutrition(self):
        labels = ['Nutrient', 'Quantity', 'Unit', 'debug val', 'Daily value bar']
        h_header = self.nutrition_table.horizontalHeader()
        self.nutrition_table.setHorizontalHeaderLabels(labels)
        
        h_header.setDefaultAlignment(Qt.AlignLeft) 
        for i in range(0, len(labels)-1):
            h_header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        header_font = QFont()
        header_font.setWeight(QFont.DemiBold)
        h_header.setFont(header_font)
        

        # Set vertical header height to determine table's row height
        v_header = self.nutrition_table.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.Fixed)
        v_header.setDefaultSectionSize(V_HEADER_SIZE)

    def display_nutrition(self, current, previous):
        # Check if incoming item is from Food name column in fridge_table
        if current.column() == NAME_COL:
            #self.nutrition_label.setText("Nutrition of selected item")

            self.nutrition_table.setRowCount(0)

            selected_food = Food(name=current.data(Qt.EditRole))
            nutrition = selected_food.get_nutrition(self.person)
            for nutrient in nutrition:
                current_row = self.nutrition_table.rowCount()
                nut_name = nutrient[0]
                nut_amount = nutrient[1]
                unit = nutrient[2]

                # Set nutrient name
                self.nutrition_table.insertRow(current_row)
                self.nutrition_table.setItem(
                    current_row, 0, QTableWidgetItem(nut_name))

                # Set nutrient quantity
                nutrient_quantity = QTableWidgetItem()
                if nut_amount is not None:
                    nutrient_quantity.setData(Qt.EditRole, nut_amount)
                    nutrient_quantity.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    #nutrient_quantity.setTextAlignment(Qt.AlignVCenter)
                else:
                    nutrient_quantity.setData(Qt.EditRole, 'No data')
                self.nutrition_table.setItem(current_row, 1, nutrient_quantity)

                # Set unit
                self.nutrition_table.setItem(
                    current_row, 2, QTableWidgetItem(unit))

                # Set percent decimal for testing
                percent_widget = QTableWidgetItem()
                if nut_amount is None:
                    percent_widget.setData(Qt.EditRole, 'No data')
                else:
                    percent_widget.setData(Qt.EditRole, self.person.calculate_dv(nut_name, nut_amount))
                self.nutrition_table.setItem(current_row, 3, percent_widget)

                # Set percentage daily value bar
                percent_bar = QtWidgets.QProgressBar(self)
                #percent_bar.setStyleSheet(open('qprogress_bar.css').read())
                #percent_bar.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
                if nut_amount is None:
                    percent_bar.setValue(0)
                elif round(self.person.calculate_dv(nut_name, nut_amount)) > 100:
                    percent_bar.setValue(100)
                else:
                    percent_bar.setValue(round(self.person.calculate_dv(nut_name, nut_amount)))
                self.nutrition_table.setCellWidget(current_row, 4, percent_bar)

    def toggle_remove_btn(self):
        if self.fridge_selection_model.hasSelection():
            self.remove_btn.setEnabled(True)
        else:
            self.remove_btn.setEnabled(False)

    def setup_selection_modes(self):
        self.fridge_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
    
    def setup_filters(self):
        self.fridge_table.installEventFilter(self)
    
    def eventFilter(self, obj, event):
        # Press delete in fridge_table to remove selected
        if obj == self.fridge_table:
            if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Delete:
                self.remove_from_fridge()
                return True
            else:
                return False
        else:
            # pass the event on to the parent class
            return QMainWindow.eventFilter(self, obj, event)
    

    def setup_connections(self):
        
        # Fridge panel connections
        self.fridge_table.itemChanged.connect(self.update_persons_food_attr)
        self.remove_btn.clicked.connect(self.remove_from_fridge)
        self.optimize_btn.clicked.connect(self.optimize)
        optimize_shortcut = QShortcut(QKeySequence(Qt.Key_F5), self)
        optimize_shortcut.activated.connect(self.optimize)

        self.add_foods_btn.clicked.connect(self.open_search_window)

        # Toggle remove button
        #self.fridge_table.selectionModel().selectionChanged.connect(self.toggle_remove_btn)

        # Nutriton panel connections
        #self.search_list.currentItemChanged.connect(self.display_nutrition)
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

class SearchWindow(QMainWindow, Ui_SearchWindow):
    def __init__(self, parent=None, person=None, fridge_table=None):
        super().__init__(parent)
        self.setupUi(self)
        self.fridge_table = fridge_table
        self.person = person

        self.setup_connections()
        #self.setup_selection_modes()
        
        self.search_box.setFocus()
        self.resize(850, 500)
        self.show()

    def search_food(self):
        search_result = database.search_food(self.search_box.text())

        self.search_model = SearchModel(search_result)
        self.search_list.setModel(self.search_model)

        # Set horizontal header stretched table fills horizontal space
        h_header = self.search_list.horizontalHeader()
        h_header.setSectionResizeMode(0, QHeaderView.Stretch)

        # Set vertical header height to determine table's row height
        v_header = self.search_list.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.Fixed)
        v_header.setDefaultSectionSize(20)

        # Toggle add button
        self.search_selection_model = self.search_list.selectionModel()
        self.search_selection_model.selectionChanged.connect(self.toggle_add_btn)

        self.search_list.show()
      
    def add_to_fridge(self, selected_items=None):
        selected_items = self.search_selection_model.selectedRows()
        for item in selected_items:
            current_row = self.fridge_table.rowCount()
            self.fridge_table.insertRow(current_row)
            self.fridge_table.setItem(current_row, 0, 
                QTableWidgetItem(self.search_model.data(index=item, role=Qt.DisplayRole)))
            #TODO: Pass data directly from search model to fridge model
            self.person.add_foods([self.search_model.data(index=item, role=Qt.DisplayRole)])

    def toggle_add_btn(self):
        if self.search_selection_model is None:
            self.add_to_fridge_btn.setEnabled(False)
        if not self.search_selection_model.hasSelection():
            self.add_to_fridge_btn.setEnabled(False)
        else:
            self.add_to_fridge_btn.setEnabled(True)
    
    def setup_connections(self):
        self.search_box.textChanged.connect(self.search_food)
        self.add_to_fridge_btn.clicked.connect(self.add_to_fridge)
        
        shortcut = QtWidgets.QShortcut(QKeySequence(Qt.Key_Return), self.search_list)
        shortcut.activated.connect(self.add_to_fridge)

        
class SearchModel(QtCore.QAbstractTableModel):
    def __init__(self, search_result):
        QtCore.QAbstractTableModel.__init__(self)
        self.search_result = search_result

    def rowCount(self, parent):
        return len(self.search_result)

    def columnCount(self, parent):
        return 1
        #return len(SEARCH_COLS)

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return None
        return self.search_result[index.row()]


class OptimumDietWindow(QMainWindow, Ui_OptimumDietWindow):
    def __init__(self, parent=None, person=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.optimizier = Optimizier()
        self.optimizier.optimize_diet(person)
        self.populate_optimum_diet_table(person)
        self.populate_optimum_diet_totals()
        self.optimizier.describe_solution()

        self.resize(800, 600)
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
        totals_font.setWeight(QFont.DemiBold)

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
    # Necessarry to get icon in Windows Taskbar
    myappid = u'spartan.0.5'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    user_db.create_user_db()
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    window = MainWindow()
    sys.exit(app.exec_())
