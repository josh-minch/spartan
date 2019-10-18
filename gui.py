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
from model.nutrition_model import MacroModel, VitModel, MineralModel
from model.fridge_model import FridgeModel
from model.fridge_selected_model import FridgeSelectedModel
from view.combo_table_view import ComboTableView
from delegate.progress_bar_delegate import ProgressBarDelegate
from delegate.align_right_delegate import AlignRightDelegate
from delegate.combobox_delegate import ComboBoxDelegate
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.blockSignals(True)
        self.person = Person('m', 1993, 12, 1, 'us')
        self.blockSignals(False)
        self.type_res = Restriction(RESTRICT_TYPES_FILE)
        self.fd_res = Restriction(RESTRICT_FDS_FILE)

        self.person.remove_nut('Fluoride (F)')
        # self.person.remove_nut('Water')
        # self.person.remove_nut('Energy')
        #self.person.add_nut(Nutrient('Energy', min=2000))

        self.setup_fridge_views()
        # self.setup_selected_foods()
        self.setup_connections()
        self.setup_shortcuts()
        self.setup_selection_modes()

        self.add_foods_btn.setFocus()
        #self.resize(QDesktopWidget().availableGeometry(self).size() * 0.90)
        self.resize(1500, 700)
        self.show()

    def setup_connections(self):
        self.fridge_model.dataChanged.connect(self.update_foods)
        self.fridge_model.dataChanged.connect(self.display_nutrition)
        self.fridge_view.selectionModel().selectionChanged.connect(self.display_nutrition)
        self.fridge_line_edit.textChanged.connect(
            self.fridge_line_edit_changed)

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
        add_foods_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_F), self)
        add_foods_shortcut.activated.connect(self.open_search_window)

        remove_shortcut = QShortcut(QKeySequence(Qt.Key_Delete), self)
        remove_shortcut.activated.connect(self.remove_from_fridge)

        close_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_W), self)
        close_shortcut.activated.connect(self.close)

        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def fridge_line_edit_changed(self):
        reg_exp = QRegExp(self.fridge_line_edit.text(), Qt.CaseInsensitive)
        self.fridge_filter_model.setFilterRegExp(reg_exp)

    def setup_fridge_views(self):
        self.fridge_model = FridgeModel(foods=self.person.foods, currency='$')
        self.fridge_filter_model = QSortFilterProxyModel(self)
        self.fridge_filter_model.setSourceModel(self.fridge_model)

        self.fridge_view.setModel(self.fridge_filter_model)
        self.prices_view.setModel(self.fridge_filter_model)
        self.constraints_view.setModel(self.fridge_filter_model)
        self.nut_quant_view.setModel(self.fridge_filter_model)

        self.fridge_filter_model.setFilterKeyColumn(NAME_COL)

        # Alignment delegates
        #self.prices_view.setItemDelegateForColumn(PRICE_COL, AlignRightDelegate(self))
        #self.prices_view.setItemDelegateForColumn(PRICE_QUANTITY_COL, AlignRightDelegate(self))
        #self.constraints_view.setItemDelegateForColumn(MIN_COL, AlignRightDelegate(self))
        #self.constraints_view.setItemDelegateForColumn(MAX_COL, AlignRightDelegate(self))
        #self.constraints_view.setItemDelegateForColumn(TARGET_COL, AlignRightDelegate(self))

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

        # Header must be explicitly set to visible even though it's already
        # set in Qt Designer or else it doesn't display for constraints view
        f_header.setVisible(True)
        p_header.setVisible(True)
        c_header.setVisible(True)

        # Set column width
        self.fridge_view.setColumnWidth(NAME_COL, 1)
        self.prices_view.setColumnWidth(PRICE_COL, VALUE_COL_WIDTH)
        self.prices_view.setColumnWidth(PER_COL, PER_COL_WIDTH)
        self.prices_view.setColumnWidth(PRICE_QUANTITY_COL, VALUE_COL_WIDTH)
        self.prices_view.setColumnWidth(PRICE_UNIT_COL, UNIT_COL_WIDTH)

        self.constraints_view.setColumnWidth(MIN_COL, VALUE_COL_WIDTH)
        self.constraints_view.setColumnWidth(MIN_UNIT_COL, UNIT_COL_WIDTH)
        self.constraints_view.setColumnWidth(MAX_COL, VALUE_COL_WIDTH)
        self.constraints_view.setColumnWidth(MAX_UNIT_COL, UNIT_COL_WIDTH)
        self.constraints_view.setColumnWidth(TARGET_COL, VALUE_COL_WIDTH)
        self.constraints_view.setColumnWidth(TARGET_UNIT_COL, UNIT_COL_WIDTH)

        f_header.setSectionResizeMode(NAME_COL, QHeaderView.Stretch)
        c_header.setSectionResizeMode(NAME_COL, QHeaderView.Stretch)

        set_v_header_height(self.fridge_view, FRIDGE_V_HEADER_SIZE)
        set_header_weight(f_header, QFont.DemiBold)
        set_v_header_height(self.prices_view, FRIDGE_V_HEADER_SIZE)
        set_header_weight(p_header, QFont.DemiBold)
        set_v_header_height(self.constraints_view, FRIDGE_V_HEADER_SIZE)
        set_header_weight(c_header, QFont.DemiBold)
        set_v_header_height(self.nut_quant_view, FRIDGE_V_HEADER_SIZE)
        set_header_weight(n_header, QFont.DemiBold)

        # Hide fridge scrollbar
        self.fridge_view.verticalScrollBar().setStyleSheet(
            "QScrollBar {width:0px;}")

    def setup_nutrition(self):
        set_column_widths(self.macros_view,
                          nut_col_to_attr.keys(), nut_col_widths)
        set_column_widths(
            self.vits_view, nut_col_to_attr.keys(), nut_col_widths)
        set_column_widths(self.minerals_view,
                          nut_col_to_attr.keys(), nut_col_widths)

        set_view_header_weights(self.macros_view, QFont.DemiBold)
        set_view_header_weights(self.vits_view, QFont.DemiBold)
        set_view_header_weights(self.minerals_view, QFont.DemiBold)
        '''
        # Set vertical header height to determine table's row height
        v_header = self.nutrition_view.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.Fixed)
        v_header.setDefaultSectionSize(V_HEADER_SIZE)
        '''

    def remove_from_fridge(self):
        selected_food_id_indexes = self.fridge_view.selectionModel().selectedRows()
        food_ids = self.fridge_model.data(
            selected_food_id_indexes[0], Qt.DisplayRole)

        self.fridge_model.removeRow(selected_food_id_indexes[0].row())
        self.person.remove_foods(food_ids=[food_ids])

    def update_foods(self, index):
        if index.column() != FOOD_ID_COL:
            food = self.person.foods[index.row()]
            self.person.update_food_in_user_db(food=food)

    def open_search_window(self):
        self.search_window = SearchWindow(
            parent=None, person=self.person, fridge_model=self.fridge_model)
        self.search_window.setAttribute(Qt.WA_DeleteOnClose)

    def open_pref(self):
        self.pref_window = PrefWindow(
            parent=None, person=self.person, type_res=self.type_res, fd_res=self.fd_res, )
        self.pref_window.setAttribute(Qt.WA_DeleteOnClose)

    def optimize(self):
        if len(self.person.foods) == 0:
            return

        self.optimum_diet_window = OptimumDietWindow(
            parent=None, person=self.person)
        self.optimum_diet_window.setAttribute(Qt.WA_DeleteOnClose)

    def change_fridge_selection(self, selected, deselected):
        selected_food_id_ixs = self.fridge_view.selectionModel().selectedRows()
        selected_food_name_ixs = [ix.siblingAtColumn(
            NAME_COL) for ix in selected_food_id_ixs]

        self.selected_food_ids = [ix.data() for ix in selected_food_id_ixs]
        food_names = [ix.data() for ix in selected_food_name_ixs]

        while self.fridge_selected_model.rowCount() > 0:
            self.fridge_selected_model.removeRow(0)

        for i, name in enumerate(food_names):
            self.fridge_selected_model.insertRows(i)

            name_ix = self.fridge_selected_model.index(
                i, S_NAME_COL, QModelIndex())
            amount_ix = self.fridge_selected_model.index(
                i, S_AMOUNT_COL, QModelIndex())
            unit_ix = self.fridge_selected_model.index(
                i, S_UNIT_COL, QModelIndex())

            self.fridge_selected_model.blockSignals(True)
            self.fridge_selected_model.setData(name_ix, name, Qt.EditRole)
            self.fridge_selected_model.setData(unit_ix, 'g', Qt.EditRole)
            self.fridge_selected_model.blockSignals(False)

            self.fridge_selected_model.setData(
                amount_ix, float(100), Qt.EditRole)

    def display_nutrition(self):
        selected_food_id_ixs = self.fridge_view.selectionModel().selectedRows()
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

        macros_model = MacroModel(nutrients=macros)
        vits_model = VitModel(nutrients=vits)
        minerals_model = MineralModel(nutrients=minerals)

        self.macros_view.setModel(macros_model)
        self.vits_view.setModel(vits_model)
        self.minerals_view.setModel(minerals_model)

        self.macros_view.setItemDelegate(ProgressBarDelegate(self))
        self.vits_view.setItemDelegate(ProgressBarDelegate(self))
        self.minerals_view.setItemDelegate(ProgressBarDelegate(self))

        self.setup_nutrition()

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
        print(self.person.foods[0])

    '''
    def closeEvent(self, event):
        for food in self.person.foods:
            self.person.update_food_in_user_db(food)
        event.accept()
    '''


if __name__ == "__main__":
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
