import sys, query
from gui_constants import *
from spartan import Person, Nutrient, Optimizier, create_db
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QTableWidgetItem, QAbstractItemView
from PySide2.QtCore import Qt, QEvent
from ui_mainwindow import Ui_MainWindow
from ui_optimum_diet_window import Ui_OptimumDietWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.person = Person('josh', 25, 'm')
        
        self.setup_connections()
        self.setup_filters()
        self.setup_selection_modes()
        self.setup_fridge()
        
        self.search_box.setFocus()
        self.resize(1400, 800)
        self.show()

    def search_food(self):
        self.search_list.clear()
        search_result = query.search_food(self.search_box.text())
        self.search_list.addItems(search_result)

    def add_to_fridge(self):
        selected_items = [str(x.text()) for x in self.search_list.selectedItems()]
        for item in selected_items:
            current_row = self.fridge_table.rowCount()
            self.fridge_table.insertRow(current_row)
            self.fridge_table.setItem(current_row, 0, QTableWidgetItem(item))

        self.person.add_foods(food_names=selected_items)

    def remove_from_fridge(self):
        food_names_to_remove = []
        
        for item in self.fridge_table.selectedItems():
            food_names_to_remove.append(str(item.text()))
            self.fridge_table.removeRow(item.row())
        
        self.person.remove_foods(food_names=food_names_to_remove)


    def setup_fridge(self):
        self.fridge_table.setHorizontalHeaderLabels(['Food', 'Price', 'Minimum', 'Maximum', 'Target'])
      
        for food in self.person.foods:
            current_row = self.fridge_table.rowCount()
            self.fridge_table.insertRow(current_row)

            for col, attr in col_to_attr.items():
                item = QTableWidgetItem()
                attr_val = getattr(food, attr)

                self.fridge_table.blockSignals(True)
                item.setData(Qt.EditRole, attr_val)
                self.fridge_table.setItem(current_row, col, item)
                self.fridge_table.blockSignals(False)
          
    def update_persons_food_attr(self, item):
        if item.row() > 0:
            food_name = self.fridge_table.item(item.row(), 0).text()
            attr = col_to_attr[item.column()]
            self.person.set_food_attr(attr, attr_value=item.text(), food_name=food_name)

    def optimize(self):
        optimum_diet_window = OptimumDietWindow(self, person=self.person)
        optimum_diet_window.setAttribute(Qt.WA_DeleteOnClose)

    def display_nutrition(self):
        pass

    def setup_selection_modes(self):
        self.search_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.fridge_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        pass
    
    def setup_filters(self):
        #return_pressed_filter = ReturnPressedFilter(self)
        self.search_list.installEventFilter(self)

    def eventFilter(self, obj, event):
        # Search list return key to add to fridge
        if isinstance(obj, QListWidget):
            if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
                self.add_to_fridge()
                return True
            else:
                return False
        else:
            # pass the event on to the parent class
            return QMainWindow.eventFilter(self, obj, event)
        
    def setup_connections(self):
        self.search_box.returnPressed.connect(self.search_food)
        self.search_btn.clicked.connect(self.search_food)
        self.add_to_fridge_btn.clicked.connect(self.add_to_fridge)

        self.fridge_table.itemChanged.connect(self.update_persons_food_attr)
        self.remove_btn.clicked.connect(self.remove_from_fridge)
        self.optimize_btn.clicked.connect(self.optimize)
        
        self.debug_btn.clicked.connect(self.print_debug_info)
       
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
        self.populate_optimum_diet_table()
        self.populate_optimum_diet_totals()
        self.optimizier.describe_solution()
        self.show()       

    def populate_optimum_diet_table(self):
        self.optimum_diet_table.setHorizontalHeaderLabels(['Food', 'Price', 'Quantity'])
        self.diet_label.setText(self.optimizier.describe_solution_status())

        for v in self.optimizier.lp_prob.variables():
            if (v.varValue is not None and v.varValue > 0):
                current_row = self.optimum_diet_table.rowCount()
                self.optimum_diet_table.insertRow(current_row)

                food_name = QTableWidgetItem()
                food_name.setData(Qt.EditRole, query.get_food_name(v.name))
                self.optimum_diet_table.setItem(current_row, NAME_COL, food_name)

                quantity = QTableWidgetItem()
                quantity.setData(Qt.EditRole, 100 * v.varValue)
                self.optimum_diet_table.setItem(current_row, QUANTITY_COL, quantity)

        total_number, total_mass = self.optimizier.get_totals()
        current_row = self.optimum_diet_table.rowCount()
        self.optimum_diet_table.insertRow(current_row)

        number_item = QTableWidgetItem()
        number_item.setData(Qt.EditRole, total_number)
        self.optimum_diet_table.setItem(current_row, NAME_COL, number_item)

        mass_item = QTableWidgetItem()
        mass_item.setData(Qt.EditRole, total_mass)
        self.optimum_diet_table.setItem(current_row, QUANTITY_COL, mass_item)

    def populate_optimum_diet_totals(self):
        total_number, total_mass = self.optimizier.get_totals()

        number_item = QTableWidgetItem()
        number_item.setData(Qt.EditRole, total_number)
        self.optimum_diet_totals.setItem(0, NAME_COL, number_item)

        mass_item = QTableWidgetItem()
        mass_item.setData(Qt.EditRole, total_mass)
        self.optimum_diet_totals.setItem(0, QUANTITY_COL, mass_item)
    
if __name__ == "__main__":
    create_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
