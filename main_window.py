import sys, query
from spartan import Person, Optimizier
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.setup_fridge()
        self.search_box.setFocus()
        self.search_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.show()

        self.person = Person(25, 'm')
        self.optimizier = Optimizier()

    def search_food(self):
        self.search_list.clear()
        search_result = query.search_food(self.search_box.text())
        print(search_result)
        self.search_list.addItems(search_result)

    def add_to_fridge(self):
        selected_items = [str(x.text()) for x in self.search_list.selectedItems()]
        #selected_items = self.search_list.selectedItems()
        for item in selected_items:
            current_row = self.fridge_table.rowCount()
            self.fridge_table.insertRow(current_row)
            self.fridge_table.setItem(current_row, 0, QTableWidgetItem(item))

        self.person.add_foods(food_names = selected_items)

    def remove_from_fridge(self):
        pass

    def setup_fridge(self):
        self.fridge_table.setHorizontalHeaderLabels(['Food', 'Price', 'Minimum', 'Maximum', 'Target'])

    def update_persons_food_constraints(self, item):
        food_name = self.fridge_table.item(item.row(), 0).text()
        if (item.column() == 1):
            self.person.set_food_price(item.text(), food_name=food_name)
        if (item.column() == 2):
            self.person.set_food_min(item.text(), food_name=food_name)
        if (item.column() == 3):
            self.person.set_food_max(item.text(), food_name=food_name)
        if (item.column() == 4):
            self.person.set_food_target(item.text(), food_name=food_name)

        for food in self.person.foods:
            print(vars(food))
        
    def optimize(self):
        self.optimizier.optimize_diet(self.person)
        self.optimizier.describe_solution()

    def setup_connections(self):
        self.search_box.returnPressed.connect(self.search_food)
        self.search_btn.clicked.connect(self.search_food)
        self.add_to_fridge_btn.clicked.connect(self.add_to_fridge)
        self.remove_btn.clicked.connect(self.remove_from_fridge)
        self.optimize_btn.clicked.connect(self.optimize)
        self.fridge_table.itemChanged.connect(self.update_persons_food_constraints)

        self.debug_btn.clicked.connect(self.print_debug_info)
       
    def print_debug_info(self):
        print([str(x.text()) for x in self.search_list.selectedItems()])
        print([str(x.text()) for x in self.fridge_table.selectedItems()])
        print("table row count is ", self.fridge_table.rowCount())
        print("table items are ",  self.fridge_table.items())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())