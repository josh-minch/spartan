import sys, query
from spartan import Person
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.search_box.setFocus()
        self.show()

    def setup_connections(self):
        self.search_box.returnPressed.connect(self.search_food)
        self.search_btn.clicked.connect(self.search_food)
        self.add_to_fridge_btn.clicked.connect(self.add_to_fridge)
        self.remove_btn.clicked.connect(self.remove_from_fridge)
        
        self.debug_btn.clicked.connect(self.print_debug_info)

    def search_food(self):
        self.search_list.clear()
        search_result = query.search_food(self.search_box.text())
        print(search_result)
        self.search_list.addItems(search_result)

    def add_to_fridge(self):
        selected_items = [str(x.text()) for x in self.search_list.selectedItems()]
        food_id = query.get_food_id(selected_items[0])
        user.add_food(food_id)
        food_names = [food.name for food in user.foods]
        self.fridge_list.addItems(selected_items)

    def remove_from_fridge(self):
        #selected_items = [str(x.text()) for x in self.fridge_list.selectedItems()]
        #self.fridge_list.addItems(selected_items)
        self.fridge_list.clear()

    def print_debug_info(self):
        print([str(x.text()) for x in self.search_list.selectedItems()])
        print([str(x.text()) for x in self.fridge_list.selectedItems()])

if __name__ == "__main__":
    user = Person(25, 'm')
    app = QApplication(sys.argv)
    window = MainWindow(user)
    sys.exit(app.exec_())