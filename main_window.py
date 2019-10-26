import sys
import ctypes
from timeit import default_timer as timer

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Qt, QEvent, Slot, QModelIndex, QRegExp, QSortFilterProxyModel
from PySide2.QtGui import QFont, QKeySequence, QPalette
from PySide2.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QListWidget, QTableWidget,
                               QListWidgetItem, QTableWidgetItem, QAbstractItemView,
                               QHeaderView, QShortcut)

from spartan import *
import database
import storage
from gui_constants import *
from gui_helpers import *
from window.search_window import SearchWindow
from window.pref_window import PrefWindow
from window.optimum_diet_window import OptimumDietWindow
from model.nutrition_model import NutritionTableModel
from model.fridge_model import FridgeModel
from view.combo_table_view import ComboTableView
from delegate.progress_bar_delegate import ProgressBarDelegate
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.blockSignals(True)
        self.person = Person('m', 1993, 12, 1)
        self.blockSignals(False)
        self.type_res = Restriction(RESTRICT_TYPES_FILE)
        self.fd_res = Restriction(RESTRICT_FDS_FILE)

        self.setup_fridge_views()
        self.display_empty_nutrition()
        self.setup_connections()
        self.setup_shortcuts()
        self.setup_selection_modes()
        self.update_fridge_line_edit_placeholder()

        self.add_foods_btn.setFocus()
        #self.resize(QDesktopWidget().availableGeometry(self).size() * 0.90)
        self.resize(1500, 700)
        self.show()

    def setup_connections(self):
        self.fridge_model.dataChanged.connect(self.update_foods)
        #self.fridge_model.dataChanged.connect(self.display_nutrition)
        self.fridge_view.selectionModel().selectionChanged.connect(self.display_nutrition)

        # Update filtered view
        self.fridge_line_edit.textChanged.connect(
            self.fridge_line_edit_changed)

        # Update fridge search placeholder
        self.fridge_model.rowsInserted.connect(
            self.update_fridge_line_edit_placeholder)
        self.fridge_model.rowsRemoved.connect(
            self.update_fridge_line_edit_placeholder)

        # Synchronize fridge selection to prices and constraints
        self.prices_view.setSelectionModel(self.fridge_view.selectionModel())
        self.constraints_view.setSelectionModel(
            self.fridge_view.selectionModel())
        self.nut_quant_view.setSelectionModel(
            self.fridge_view.selectionModel())

        # Synchronize scrollbars
        self.fridge_view.verticalScrollBar().valueChanged.connect(
            self.prices_view.verticalScrollBar().setValue)
        self.prices_view.verticalScrollBar().valueChanged.connect(
            self.fridge_view.verticalScrollBar().setValue)

        self.fridge_view.verticalScrollBar().valueChanged.connect(
            self.constraints_view.verticalScrollBar().setValue)
        self.constraints_view.verticalScrollBar().valueChanged.connect(
            self.fridge_view.verticalScrollBar().setValue)

        self.fridge_view.verticalScrollBar().valueChanged.connect(
            self.nut_quant_view.verticalScrollBar().setValue)
        self.nut_quant_view.verticalScrollBar().valueChanged.connect(
            self.fridge_view.verticalScrollBar().setValue)

        # Add to fridge button
        self.add_foods_btn.clicked.connect(self.open_search_window)

        # Remove button
        self.remove_btn.clicked.connect(self.remove_from_fridge)
        self.fridge_view.selectionModel().selectionChanged.connect(self.toggle_remove_btn)

        # Optimize button
        self.optimize_btn.clicked.connect(self.optimize)
        # optimize button shortcut set in Qt Designer

        # Preferences button
        self.pref_btn.clicked.connect(self.open_pref)

    def setup_shortcuts(self):
        #add_foods_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_F), self)
        #add_foods_shortcut.activated.connect(self.open_search_window)

        remove_shortcut = QShortcut(QKeySequence(Qt.Key_Delete), self)
        remove_shortcut.activated.connect(self.remove_from_fridge)

        close_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_W), self)
        close_shortcut.activated.connect(self.close)

        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def update_fridge_line_edit_placeholder(self):
        number = len(self.person.foods)
        plural = '' if number == 1 else 's'
        text = '🔍 Search my fridge ({number} item{plural})'.format(
            number=number, plural=plural)
        self.fridge_line_edit.setPlaceholderText(text)

    def fridge_line_edit_changed(self):
        reg_exp = QRegExp(self.fridge_line_edit.text(), Qt.CaseInsensitive)
        self.fridge_filter_model.setFilterRegExp(reg_exp)

    def setup_fridge_views(self):
        self.fridge_model = FridgeModel(foods=self.person.foods)
        self.fridge_filter_model = QSortFilterProxyModel(self)
        self.fridge_filter_model.setSourceModel(self.fridge_model)

        self.fridge_view.setModel(self.fridge_filter_model)
        self.prices_view.setModel(self.fridge_filter_model)
        self.constraints_view.setModel(self.fridge_filter_model)
        self.nut_quant_view.setModel(self.fridge_filter_model)

        self.fridge_filter_model.setFilterKeyColumn(NAME_COL)

        # Delegates set in view

        # Hide col
        hide_view_cols(self.fridge_view, F_COLS_TO_HIDE)
        hide_view_cols(self.prices_view, P_COLS_TO_HIDE)
        hide_view_cols(self.constraints_view, C_COLS_TO_HIDE)
        hide_view_cols(self.nut_quant_view, N_COLS_TO_HIDE)

        # Horizontal header
        f_header = self.fridge_view.horizontalHeader()
        p_header = self.prices_view.horizontalHeader()
        c_header = self.constraints_view.horizontalHeader()
        n_header = self.nut_quant_view.horizontalHeader()

        # Header must be explicitly set to visible even if set in Designer
        f_header.setVisible(True)
        p_header.setVisible(True)
        c_header.setVisible(True)
        n_header.setVisible(True)

        # Set column width
        self.prices_view.setColumnWidth(PRICE_COL, VALUE_COL_WIDTH)
        self.prices_view.setColumnWidth(PER_COL, PER_COL_WIDTH)
        self.prices_view.setColumnWidth(PRICE_QUANTITY_COL, VALUE_COL_WIDTH)

        self.constraints_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.constraints_view.setColumnWidth(MIN_COL, VALUE_COL_WIDTH)
        self.constraints_view.setColumnWidth(MAX_COL, VALUE_COL_WIDTH)
        self.constraints_view.setColumnWidth(TARGET_COL, VALUE_COL_WIDTH)

        self.nut_quant_view.setColumnWidth(NUT_QUANT_COL, VALUE_COL_WIDTH)

        # Set row height
        set_v_header_height(self.fridge_view, FRIDGE_V_HEADER_SIZE)
        set_v_header_height(self.prices_view, FRIDGE_V_HEADER_SIZE)
        set_v_header_height(self.constraints_view, FRIDGE_V_HEADER_SIZE)
        set_v_header_height(self.nut_quant_view, FRIDGE_V_HEADER_SIZE)

        set_header_font(self.fridge_view, FONT_MAIN_SIZE, QFont.DemiBold)
        set_header_font(self.prices_view, FONT_MAIN_SIZE, QFont.DemiBold)
        set_header_font(self.constraints_view, FONT_MAIN_SIZE, QFont.DemiBold)
        set_header_font(self.nut_quant_view, FONT_MAIN_SIZE, QFont.DemiBold)

        # Set header fixed
        #self.fridge_view.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        #self.prices_view.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        #self.constraints_view.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        #self.nut_quant_view.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # Hide fridge scrollbar
        self.fridge_view.verticalScrollBar().setStyleSheet(
            "QScrollBar {width:0px;}")

    def display_empty_nutrition(self):
        macros, vits, minerals = get_empty_nutrition(self.person)

        macros_model = NutritionTableModel(nutrients=macros, nutrient_group='General')
        vits_model = NutritionTableModel(nutrients=vits, nutrient_group='Vitamins')
        minerals_model = NutritionTableModel(
            nutrients=minerals, nutrient_group='Minerals')

        self.macros_view.setModel(macros_model)
        self.vits_view.setModel(vits_model)
        self.minerals_view.setModel(minerals_model)

        self.macros_view.setItemDelegate(ProgressBarDelegate(self))
        self.vits_view.setItemDelegate(ProgressBarDelegate(self))
        self.minerals_view.setItemDelegate(ProgressBarDelegate(self))

        self.set_nutrition_size()

    def set_nutrition_size(self):
        set_column_widths(self.macros_view,
                          nut_col_to_attr.keys(), nut_col_widths)
        set_column_widths(
            self.vits_view, nut_col_to_attr.keys(), nut_col_widths)
        set_column_widths(self.minerals_view,
                          nut_col_to_attr.keys(), nut_col_widths)

        set_header_font(self.macros_view, FONT_MAIN_SIZE, QFont.DemiBold)
        set_header_font(self.vits_view, FONT_MAIN_SIZE, QFont.DemiBold)
        set_header_font(self.minerals_view, FONT_MAIN_SIZE, QFont.DemiBold)

        vertical_resize_table_view_to_contents(self.macros_view)
        vertical_resize_table_view_to_contents(self.vits_view)
        vertical_resize_table_view_to_contents(self.minerals_view)

        self.macros_view.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.vits_view.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.minerals_view.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def remove_from_fridge(self):
        selected_food_id_indexes = self.fridge_view.selectionModel().selectedRows()
        food_ids = []
        for index in selected_food_id_indexes:
            food_ids.append(index.data(Qt.DisplayRole))

        row = selected_food_id_indexes[0].row()
        count = selected_food_id_indexes[-1].row() - row + 1

        self.fridge_model.removeRows(row, count)
        self.person.remove_foods_from_db(food_ids=food_ids)

    def update_foods(self, index):
        if index.column() != FOOD_ID_COL:
            food = self.person.foods[index.row()]
            self.person.update_food_in_user_db(food=food)

    def open_search_window(self):
        self.search_window = SearchWindow(
            parent=None, person=self.person, fridge_model=self.fridge_model, type_res=self.type_res, fd_res=self.fd_res)
        self.search_window.setAttribute(Qt.WA_DeleteOnClose)

    def open_pref(self):
        self.pref_window = PrefWindow(
            parent=None, person=self.person, type_res=self.type_res, fd_res=self.fd_res)
        self.pref_window.setAttribute(Qt.WA_DeleteOnClose)

    def optimize(self):
        if len(self.person.foods) == 0:
            return

        self.optimum_diet_window = OptimumDietWindow(self.person, self.type_res, self.fd_res, self)
        self.optimum_diet_window.setAttribute(Qt.WA_DeleteOnClose)

    def display_nutrition(self):
        selected_food_id_ixs = self.fridge_view.selectionModel().selectedRows()
        if len(selected_food_id_ixs) == 0:
            self.display_empty_nutrition()
            return

        selected_food_ids = [ix.data() for ix in selected_food_id_ixs]
        selected_food_amounts = [ix.siblingAtColumn(
            NUT_QUANT_COL).data() for ix in selected_food_id_ixs]
        selected_food_units = [ix.siblingAtColumn(
            NUT_QUANT_UNIT_COL).data() for ix in selected_food_id_ixs]

        # Convert non-gram quantities to grams
        for i, (unit, food_id, amount) in enumerate(zip(selected_food_units, selected_food_ids, selected_food_amounts)):
            if unit != 'g':
                converted_amount = convert_quantity(food_id, amount, old_unit=unit, new_unit='g')
                selected_food_amounts[i] = converted_amount

        macros, vits, minerals = get_nutrition(
            self.person, selected_food_ids, selected_food_amounts)

        macros_model = NutritionTableModel(nutrients=macros, nutrient_group='General')
        vits_model = NutritionTableModel(
            nutrients=vits, nutrient_group='Vitamins')
        minerals_model = NutritionTableModel(
            nutrients=minerals, nutrient_group='Minerals')

        self.macros_view.setModel(macros_model)
        self.vits_view.setModel(vits_model)
        self.minerals_view.setModel(minerals_model)

        self.macros_view.setItemDelegate(ProgressBarDelegate(self))
        self.vits_view.setItemDelegate(ProgressBarDelegate(self))
        self.minerals_view.setItemDelegate(ProgressBarDelegate(self))

        self.set_nutrition_size()

    def toggle_remove_btn(self):
        if self.fridge_view.selectionModel() is None:
            self.remove_btn.setEnabled(False)
        elif self.fridge_view.selectionModel().hasSelection():
            self.remove_btn.setEnabled(True)
        else:
            self.remove_btn.setEnabled(False)

    def setup_selection_modes(self):
        # self.fridge_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        pass

    def print_debug_info(self):
        print(self.fridge_view.horizontalHeader().font())
        print(self.constraints_view.horizontalHeader().font())
        print(self.macros_view.horizontalHeader().font())

def main():
    # Necessarry to get icon in Windows Taskbar
    myappid = u'spartan.0.5'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    storage.create_spartan_db()
    app = QApplication(sys.argv)
    # app.setStyle(QtWidgets.QStyleFactory.create('fusion'))

    #p = QPalette()
    #p.setColor(QPalette.Highlight, Qt.darkRed)
    # app.setPalette(p)

    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
