import sys
import ctypes
from timeit import default_timer as timer

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Qt, QEvent
from PySide2.QtGui import QFont, QKeySequence, QPalette
from PySide2.QtWidgets import (QApplication, QMainWindow, QListWidget, QTableWidget,
                               QListWidgetItem, QTableWidgetItem, QAbstractItemView, QHeaderView, QShortcut)

from spartan import Person, Food, Nutrient, Optimizier
from gui_constants import *
from gui_helpers import *
import database
import user_db
from search_window import SearchWindow
from optimum_diet_window import OptimumDietWindow
from fridge_model import FridgeModel
from nutrition_model import NutritionTableModel
from progress_bar_delegate import ProgressBarDelegate

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.person = Person('josh', 25, 'm')

        self.setup_fridge_view()
        self.setup_constraints_view()
        self.setup_connections()
        self.setup_filters()
        self.setup_selection_modes()    

        self.add_foods_btn.setFocus()
        #self.move(WINDOW_POS, WINDOW_POS)
        self.resize(1600-10*WINDOW_POS, 900-4*WINDOW_POS)
        self.show()

    def setup_fridge_view(self):

        self.fridge_model = FridgeModel(foods=self.person.foods)
        self.fridge_view.setModel(self.fridge_model)

        # Hide col
        cols_to_hide = [FOOD_ID_COL, MIN_COL, MAX_COL, TARGET_COL]
        hide_view_cols(self.fridge_view, cols_to_hide)
        
        # Horizontal header
        h_header = self.fridge_view.horizontalHeader()
        h_header.setSectionResizeMode(NAME_COL, QHeaderView.Stretch)
        self.fridge_view.setColumnWidth(PRICE_COL, PRICE_COL_WIDTH)

        set_v_header_height(self.fridge_view, FRIDGE_V_HEADER_SIZE)
        set_header_weight(h_header, QFont.DemiBold)
    
    def setup_constraints_view(self):
        '''
        self.constraints_view.setModel(self.fridge_model)

        cols_to_hide = [FOOD_ID_COL, PRICE_COL]
        hide_view_cols(self.constraints_view, cols_to_hide)
        
        # Horizontal header
        h_header = self.constraints_view.horizontalHeader()
        h_header.setDefaultSectionSize(100)
        h_header.setSectionResizeMode(NAME_COL, QHeaderView.Stretch)
        
        h_header.setDefaultAlignment(Qt.AlignCenter) 
    
        set_header_weight(h_header, QFont.DemiBold)

        set_v_header_height(self.constraints_view, V_HEADER_SIZE)
        '''

    def setup_nutrition(self):
        
        self.nutrition_view_1.setMinimumSize(sum(NUT_COL_WIDTHS) + 15, 0)

        for col, width in zip(COL_TO_NUT_ATTR.keys(), NUT_COL_WIDTHS):
            self.nutrition_view_1.setColumnWidth(col, width)
            self.nutrition_view_2.setColumnWidth(col, width)
        
        h_header = self.nutrition_view_1.horizontalHeader()
        header_font = QFont()
        header_font.setWeight(QFont.DemiBold)
        h_header.setFont(header_font)

        # Set vertical header height to determine table's row height
        v_header = self.nutrition_view_1.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.Fixed)
        v_header.setDefaultSectionSize(V_HEADER_SIZE)

    def remove_from_fridge(self):
        food_names_to_remove = []

        for item in self.fridge_view.selectedItems():
            food_names_to_remove.append(str(item.data(Qt.EditRole)))
            self.fridge_view.removeRow(item.row())

        self.person.remove_foods(food_names=food_names_to_remove)

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

    def display_nutrition(self, selected, deselected):
           
        food_name = self.fridge_model.data(selected.indexes()[0], Qt.DisplayRole)

        selected_food = Food(name=food_name)
        nutrients = selected_food.get_nutrition(self.person)
        nutrition_model = NutritionTableModel(nutrients=nutrients)
        
        self.nutrition_view_1.setModel(nutrition_model)

        self.setup_nutrition()   

        progress_bar_delegate = ProgressBarDelegate(self)
        self.nutrition_view_1.setItemDelegate(progress_bar_delegate)
          
        
        '''
        # Check if incoming item is from Food name column in fridge_view
    
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

                # Change bar and text color
                p = QPalette()
                p.setColor(QPalette.Highlight, Qt.darkRed)
                p.setColor(QPalette.HighlightedText, Qt.white)
                percent_bar.setPalette(p)

                if nut_amount is None:
                    percent_bar.setValue(0)
                elif round(self.person.calculate_dv(nut_name, nut_amount)) > 100:
                    percent_bar.setValue(100)
                else:
                    percent_bar.setValue(round(self.person.calculate_dv(nut_name, nut_amount)))
                self.nutrition_table.setCellWidget(current_row, 4, percent_bar)
        '''

    def toggle_remove_btn(self):
        if self.fridge_selection_model.hasSelection():
            self.remove_btn.setEnabled(True)
        else:
            self.remove_btn.setEnabled(False)

    def setup_selection_modes(self):
        #self.fridge_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        pass

    def setup_filters(self):
        self.fridge_view.installEventFilter(self)
    
    def eventFilter(self, obj, event):
        # Press delete in fridge_view to remove selected
        if obj == self.fridge_view:
            if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Delete:
                self.remove_from_fridge()
                return True
            else:
                return False
        else:
            # pass the event on to the parent class
            return QMainWindow.eventFilter(self, obj, event)
    

    def setup_connections(self):
        
        self.fridge_model.dataChanged.connect(self.update_persons_food_attr)
        
        # Add to fridge button
        self.add_foods_btn.clicked.connect(self.open_search_window)
        self.add_foods_btn_2.clicked.connect(self.open_search_window)
        add_foods_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_F), self)
        add_foods_shortcut.activated.connect(self.open_search_window)
        
        # Remove button
        self.remove_btn.clicked.connect(self.remove_from_fridge)
        self.remove_btn_2.clicked.connect(self.remove_from_fridge)

        # Toggle remove button
        #self.fridge_view.selectionModel().selectionChanged.connect(self.toggle_remove_btn)

        self.optimize_btn.clicked.connect(self.optimize)
        # Optimize button shortcut set in Qt Designer
       
        # Nutriton panel connections
        #self.search_list.currentItemChanged.connect(self.display_nutrition)
        self.fridge_view.selectionModel().selectionChanged.connect(self.display_nutrition)
        #self.fridge_view_2.currentItemChanged.connect(self.display_nutrition)

        # Close 
        close_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_W), self)
        close_shortcut.activated.connect(self.close)

        # Debug 
        self.debug_btn.clicked.connect(self.print_debug_info)
        add_foods_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        add_foods_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        print('''(づ ◕‿◕ )づ ❤️  Jane is such a sweetie pie (=⌒‿‿⌒=) ٩(◕‿◕)۶ ❤️
                  ｡^‿^｡ ❀◕ ‿ ◕❀     ''')

if __name__ == "__main__":
    # Necessarry to get icon in Windows Taskbar
    myappid = u'spartan.0.5'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    user_db.create_user_db()
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('fusion'))
    
    p = QPalette()
    p.setColor(QPalette.Highlight, Qt.darkRed)
    app.setPalette(p)
    
    window = MainWindow()
    sys.exit(app.exec_())