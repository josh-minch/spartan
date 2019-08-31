import sys
import ctypes
from timeit import default_timer as timer

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Qt, QEvent
from PySide2.QtGui import QFont, QKeySequence, QPalette
from PySide2.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QListWidget, QTableWidget,
                               QListWidgetItem, QTableWidgetItem, QAbstractItemView, 
                               QHeaderView, QShortcut)

from spartan import *
from gui_constants import *
from gui_helpers import *
import database
import user_db
from search_window import SearchWindow
from optimum_diet_window import OptimumDietWindow
from fridge_model import FridgeModel
from nutrition_model import NutritionTableModel
from progress_bar_delegate import ProgressBarDelegate
from fridge_quantity_delegate import FridgeQuantityDelegate

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.person = Person('josh', 25, 'm')

        self.setup_fridge_views()
        self.setup_connections()
        self.setup_selection_modes()    

        self.add_foods_btn.setFocus()
        #self.resize(QDesktopWidget().availableGeometry(self).size() * 0.90)
        self.resize(1200, 800)
        self.show()

    def setup_fridge_views(self):

        self.fridge_model = FridgeModel(foods=self.person.foods)
        self.fridge_view.setModel(self.fridge_model)
        self.prices_view.setModel(self.fridge_model)
        self.constraints_view.setModel(self.fridge_model)

        # Set custom delegates
        fridge_quantity_delegate = FridgeQuantityDelegate(self)
        self.prices_view.setItemDelegate(fridge_quantity_delegate)
        self.constraints_view.setItemDelegate(fridge_quantity_delegate)
        
        # Hide col
        hide_view_cols(self.fridge_view, F_COLS_TO_HIDE)
        hide_view_cols(self.prices_view, P_COLS_TO_HIDE)
        hide_view_cols(self.constraints_view, C_COLS_TO_HIDE)
        
        # Horizontal header
        f_header = self.fridge_view.horizontalHeader()
        p_header = self.prices_view.horizontalHeader()
        c_header = self.constraints_view.horizontalHeader()

        # Header must be explicitly set to visible even though it's already 
        # set in Qt Designer or else it doesn't display for constraints view
        f_header.setVisible(True)
        p_header.setVisible(True)
        c_header.setVisible(True)

        f_header.setSectionResizeMode(NAME_COL, QHeaderView.Stretch)
        self.fridge_view.setColumnWidth(PRICE_COL, PRICE_COL_WIDTH)
        c_header.setSectionResizeMode(NAME_COL, QHeaderView.Stretch)

        set_v_header_height(self.fridge_view, FRIDGE_V_HEADER_SIZE)
        set_header_weight(f_header, QFont.DemiBold)
        set_v_header_height(self.prices_view, FRIDGE_V_HEADER_SIZE)
        set_header_weight(p_header, QFont.DemiBold)
        set_v_header_height(self.constraints_view, FRIDGE_V_HEADER_SIZE)
        set_header_weight(c_header, QFont.DemiBold)

        # Hide fridge scrollbar
        self.fridge_view.verticalScrollBar().setStyleSheet("QScrollBar {width:0px;}");
      
    def setup_nutrition(self):
        
        for col, width in zip(COL_TO_NUT_ATTR.keys(), NUT_COL_WIDTHS):
            self.nutrition_view.setColumnWidth(col, width)
        
        '''
        # Set vertical header height to determine table's row height
        v_header = self.nutrition_view.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.Fixed)
        v_header.setDefaultSectionSize(V_HEADER_SIZE)
        '''
    
    def remove_from_fridge(self):
        selected_food_id_indexes = self.fridge_view.selectionModel().selectedRows()
        food_ids = self.fridge_model.data(selected_food_id_indexes[0], Qt.DisplayRole)

        self.fridge_model.removeRow(selected_food_id_indexes[0].row())
        self.person.remove_foods(food_ids=[food_ids])

    def update_persons_food_attr(self, index):
        if index.column() != FOOD_ID_COL:
            food_id = self.person.foods[index.row()].food_id
            attr = col_to_attr[index.column()]

            # User entering empty string stores NULL in database
            if index.data(Qt.EditRole) in ("", None):
                self.person.update_attr_in_db(
                    attr, attr_value=None, food_id=food_id)
            else:
                self.person.update_attr_in_db(attr, 
                    attr_value=index.data(Qt.EditRole), food_id=food_id)

    def open_search_window(self):
        self.search_window = SearchWindow(parent=None, person=self.person, fridge_model=self.fridge_model)
        self.search_window.setAttribute(Qt.WA_DeleteOnClose)

    def optimize(self):
        self.optimum_diet_window = OptimumDietWindow(parent=None, person=self.person)
        self.optimum_diet_window.setAttribute(Qt.WA_DeleteOnClose)

    def display_nutrition(self, selected, deselected):
        if not self.fridge_view.selectionModel().hasSelection():
            return

        selected_food_ixs = self.fridge_view.selectionModel().selectedRows()

        food_ids = [self.fridge_model.data(ix, Qt.DisplayRole) for ix in selected_food_ixs]
        nutrients = get_nutrition(self.person, food_ids)

        nutrition_model = NutritionTableModel(nutrients=nutrients)
        progress_bar_delegate = ProgressBarDelegate(self)
        self.nutrition_view.setItemDelegate(progress_bar_delegate)
        self.nutrition_view.setModel(nutrition_model)

        self.setup_nutrition()   

    def toggle_remove_btn(self):
        if self.fridge_view.selectionModel() is None:
            self.remove_btn.setEnabled(False)
        elif self.fridge_view.selectionModel().hasSelection():
            self.remove_btn.setEnabled(True)
        else:
            self.remove_btn.setEnabled(False)

    def setup_selection_modes(self):
        #self.fridge_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        pass
    
    def setup_connections(self):
        
        self.fridge_model.dataChanged.connect(self.update_persons_food_attr)

        # Synchronize scrollbars       
        self.fridge_view.verticalScrollBar().valueChanged.connect(
            self.prices_view.verticalScrollBar().setValue)
        self.prices_view.verticalScrollBar().valueChanged.connect(
            self.fridge_view.verticalScrollBar().setValue)

        self.fridge_view.verticalScrollBar().valueChanged.connect(
            self.constraints_view.verticalScrollBar().setValue)
        self.constraints_view.verticalScrollBar().valueChanged.connect(
            self.fridge_view.verticalScrollBar().setValue)
        

        # Add to fridge button
        self.add_foods_btn.clicked.connect(self.open_search_window)
        #self.add_foods_btn_2.clicked.connect(self.open_search_window)
        add_foods_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_F), self)
        add_foods_shortcut.activated.connect(self.open_search_window)
        
        # Remove button
        self.remove_btn.clicked.connect(self.remove_from_fridge)
        #self.remove_btn_2.clicked.connect(self.remove_from_fridge)
        self.fridge_view.selectionModel().selectionChanged.connect(self.toggle_remove_btn)
        remove_shortcut = QShortcut(QKeySequence(Qt.Key_Delete), self)
        remove_shortcut.activated.connect(self.remove_from_fridge)

        self.optimize_btn.clicked.connect(self.optimize)
        # optimize button shortcut set in Qt Designer
       
        # Nutriton panel connections
        self.fridge_view.selectionModel().selectionChanged.connect(self.display_nutrition)
        self.prices_view.setSelectionModel(self.fridge_view.selectionModel())
        self.constraints_view.setSelectionModel(self.fridge_view.selectionModel())
        #self.constraints_view.selectionModel().selectionChanged.connect(self.display_nutrition)
        #self.fridge_view_2.currentItemChanged.connect(self.display_nutrition)

        # Close 
        close_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_W), self)
        close_shortcut.activated.connect(self.close)

        # Debug 
        self.debug_btn.clicked.connect(self.print_debug_info)
        add_foods_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        add_foods_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        print(self.fridge_view.selectionModel().hasSelection())
        print(self.fridge_view.selectionModel().selectedIndexes())
        print(self.fridge_view.selectionModel().selectedRows())
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