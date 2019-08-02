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
from search_window import SearchWindow
from optimum_diet_window import OptimumDietWindow
from fridge_model import FridgeModel

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.person = Person('josh', 25, 'm')

        self.setup_fridge()
        self.setup_connections()
        self.setup_filters()
        self.setup_selection_modes()
        
        self.setup_nutrition()

        self.add_foods_btn.setFocus()
        self.move(30,30)
        self.resize(1366, 768)
        self.show()

    def remove_from_fridge(self):
        food_names_to_remove = []

        for item in self.fridge_view_1.selectedItems():
            food_names_to_remove.append(str(item.data(Qt.EditRole)))
            self.fridge_view_1.removeRow(item.row())

        self.person.remove_foods(food_names=food_names_to_remove)

    def setup_fridge(self):
        
        self.fridge_model = FridgeModel(foods=self.person.foods)
        self.fridge_view_1.setModel(self.fridge_model)

        # Move to setup constraints view
        self.fridge_view_2.setModel(self.fridge_model)

        # Hide id column
        #self.fridge_view_1.setColumnHidden(FOOD_ID_COL, True)
        #self.fridge_view_2.setColumnHidden(FOOD_ID_COL, True)

        # Horizontal header
        
        header = self.fridge_view_1.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        header.setDefaultAlignment(Qt.AlignLeft) 

        header_font = QFont()
        header_font.setWeight(QFont.DemiBold)
        header.setFont(header_font)

        # Set vertical header height to determine table's row height
        v_header = self.fridge_view_1.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.Fixed)
        v_header.setDefaultSectionSize(V_HEADER_SIZE)
        
        '''
        for food in self.person.foods:

            for col, attr in col_to_attr.items():
                item = QTableWidgetItem()
                if col == PRICE_COL:
                    pass
                attr_val = getattr(food, attr)

                self.fridge_view_1.blockSignals(True)
                item.setData(Qt.EditRole, attr_val)
                self.fridge_view_1.setItem(current_row, col, item)
                self.fridge_view_1.blockSignals(False)
        '''

    def update_persons_food_attr(self, index):
        # Update food attributes, not food name
        if index.column() > NAME_COL:
            food_name = self.person.foods[index.row()].name
            attr = col_to_attr[index.column()]
            # User entering empty string stores NULL in database
            if index.data(Qt.EditRole) == "":
                self.person.update_attr_in_db(
                    attr, attr_value=None, food_name=food_name)
            else:
                self.person.update_attr_in_db(attr, attr_value=float(
                    index.data(Qt.EditRole)), food_name=food_name)

    def open_search_window(self):
        self.search_window = SearchWindow(parent=None, person=self.person, fridge_model=self.fridge_model)
        self.search_window.setAttribute(Qt.WA_DeleteOnClose)

    def optimize(self):
        self.optimum_diet_window = OptimumDietWindow(parent=None, person=self.person)
        self.optimum_diet_window.setAttribute(Qt.WA_DeleteOnClose)

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

    def display_nutrition(self, selected, deselected):
        # Check if incoming item is from Food name column in fridge_view_1
   
        if selected.indexes()[0].column() == NAME_COL:
            #self.nutrition_label.setText("Nutrition of selected item")

            self.nutrition_table.setRowCount(0)

            food_name = self.fridge_model.data(selected.indexes()[0], Qt.DisplayRole)

            selected_food = Food(name=food_name)
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
        #self.fridge_view_1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        pass

    def setup_filters(self):
        self.fridge_view_1.installEventFilter(self)
    
    def eventFilter(self, obj, event):
        # Press delete in fridge_view_1 to remove selected
        if obj == self.fridge_view_1:
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
        self.fridge_model.dataChanged.connect(self.update_persons_food_attr)
        self.remove_btn.clicked.connect(self.remove_from_fridge)
        self.optimize_btn.clicked.connect(self.optimize)
        optimize_shortcut = QShortcut(QKeySequence(Qt.Key_F5), self)
        optimize_shortcut.activated.connect(self.optimize)

        self.add_foods_btn.clicked.connect(self.open_search_window)
        add_foods_shortcut = QShortcut(QKeySequence(Qt.Key_Control + Qt.Key_F), self)
        add_foods_shortcut.activated.connect(self.open_search_window)


        # Toggle remove button
        #self.fridge_view_1.selectionModel().selectionChanged.connect(self.toggle_remove_btn)

        # Nutriton panel connections
        #self.search_list.currentItemChanged.connect(self.display_nutrition)
        self.fridge_view_1.selectionModel().selectionChanged.connect(self.display_nutrition)
        self.fridge_view_1.selectionModel().selectionChanged.connect(self.print_debug_info)
        #self.fridge_view_2.currentItemChanged.connect(self.display_nutrition)

        # Debug 
        self.debug_btn.clicked.connect(self.print_debug_info)
        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self, selected, deselected):
        print(selected.indexes())



if __name__ == "__main__":
    # Necessarry to get icon in Windows Taskbar
    myappid = u'spartan.0.5'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    user_db.create_user_db()
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    window = MainWindow()
    sys.exit(app.exec_())