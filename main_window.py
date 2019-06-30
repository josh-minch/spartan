import sys, query
from spartan import Person, Optimizier, create_db
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView
from PySide2.QtCore import Qt
from ui_mainwindow import Ui_MainWindow

NAME_COL = 0
PRICE_COL = 1
MIN_COL = 2
MAX_COL = 3
TARGET_COL = 4

col_to_attr = {NAME_COL: 'name', PRICE_COL: 'price',
               MIN_COL: 'min', MAX_COL: 'max', TARGET_COL: 'target'}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.person = Person('josh', 25, 'm')

        self.setupUi(self)
        self.setup_connections()
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
        food_names_to_remove = [str(x.text()) for x in self.fridge_table.selectedItems()]

        for item in self.fridge_table.selectedItems():
            self.fridge_table.removeRow(item.row())
        
        self.person.remove_foods(food_names=food_names_to_remove)

    def setup_fridge(self):
        self.fridge_table.setHorizontalHeaderLabels(['Food', 'Price', 'Minimum', 'Maximum', 'Target'])
        col_to_attr = {NAME_COL: 'name', PRICE_COL: 'price',
                             MIN_COL: 'min', MAX_COL: 'max', TARGET_COL: 'target'}
        attr = ['name', 'price', 'min', 'max', 'target']

        for food in self.person.foods:
            current_row = self.fridge_table.rowCount()
            self.fridge_table.insertRow(current_row)

            for col, attr in col_to_attr.items():
                item = QTableWidgetItem()
                attr_val = getattr(food, attr)

                self.fridge_table.blockSignals(True)
                item.setData(Qt.DisplayRole, attr_val)
                self.fridge_table.setItem(current_row, col, item)
                self.fridge_table.blockSignals(False)
          
    def update_persons_food_attr(self, item):
        col_to_attr = {NAME_COL: 'name', PRICE_COL: 'price',
                             MIN_COL: 'min', MAX_COL: 'max', TARGET_COL: 'target'}
        
        food_name = self.fridge_table.item(item.row(), 0).text()
        attr = col_to_attr[item.column()]
        self.person.set_food_attr(attr, attr_value=item.text(), food_name=food_name)

    def optimize(self):
        self.optimizier = Optimizier()
        self.optimizier.optimize_diet(self.person)
        self.optimizier.describe_solution()

    def setup_selection_modes(self):
        self.search_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.fridge_table.setSelectionMode(QAbstractItemView.ExtendedSelection)

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

if __name__ == "__main__":
    create_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
