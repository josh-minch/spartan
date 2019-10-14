from PySide2.QtCore import Qt, QModelIndex, Signal
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import (QApplication, QMainWindow, QHeaderView, QShortcut)

import spartan
import database
from gui_constants import *
from ui.ui_searchwindow import Ui_SearchWindow
from model.search_model import SearchModel

class SearchWindow(QMainWindow, Ui_SearchWindow):
    def __init__(self, parent=None, person=None, fridge_model=None):
        super().__init__(parent)
        self.setupUi(self)
        self.fridge_model = fridge_model
        self.person = person

        self.setup_connections()
        #self.setup_selection_modes()

        self.search_box.setFocus()
        self.resize(850, 500)
        self.show()

    def search_food(self):
        search_result = database.search_food(self.search_box.text(), self.person)

        self.search_model = SearchModel(search_result)
        self.search_list.setModel(self.search_model)

        # Set horizontal header stretched so table fills horizontal space
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
        selected_items = self.search_list.selectionModel().selectedRows()
        for item in selected_items:
            current_row = self.fridge_model.rowCount()
            food_name = self.search_model.data(item, Qt.DisplayRole)
            food_to_add = spartan.Food(name=food_name)
            self.fridge_model.insertRows(current_row+1)
            name_ix = self.fridge_model.index(current_row+1, NAME_COL)
            self.blockSignals(True)
            self.fridge_model.setData(name_ix, food_name)
            self.blockSignals(False)

            self.person.add_food_to_db(food_to_add)

    def toggle_add_btn(self):
        if self.search_selection_model is None:
            self.add_to_fridge_btn.setEnabled(False)
        elif self.search_selection_model.hasSelection():
            self.add_to_fridge_btn.setEnabled(True)
        else:
            self.add_to_fridge_btn.setEnabled(False)

    def setup_connections(self):
        self.search_box.textChanged.connect(self.search_food)
        self.add_to_fridge_btn.clicked.connect(self.add_to_fridge)

        add_shortcut = QShortcut(QKeySequence(Qt.Key_Return), self.search_list)
        add_shortcut.activated.connect(self.add_to_fridge)

        self.debug_btn.clicked.connect(self.print_debug_info)
        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        print(self.search_list)
        print(self.search_list.selectionModel())
        print(self.search_list.selectionModel().selectedRows())
