from PySide2.QtCore import Qt, QModelIndex, Signal
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import (QApplication, QMainWindow, QHeaderView, QShortcut)

import spartan
import database
from gui_constants import *
from ui.ui_searchwindow import Ui_SearchWindow
from model.search_model import SearchModel

class SearchWindow(QMainWindow, Ui_SearchWindow):
    def __init__(self, parent=None, person=None, fridge_model=None, type_res=None, fd_res=None):
        super().__init__(parent)
        self.setupUi(self)
        self.person = person
        self.fridge_model = fridge_model
        self.type_res = type_res
        self.fd_res = fd_res

        self.setup_connections()

        self.search_box.setFocus()
        self.resize(850, 500)
        self.show()

    def search_food(self):
        search_result = database.search_food(self.search_box.text(), self.person, self.type_res, self.fd_res)

        self.search_model = SearchModel(search_result)
        self.search_view.setModel(self.search_model)

        self.search_view.setColumnWidth(Search.attr_to_col['fd_grp'], 180)

        # Set vertical header height to determine table's row height
        v_header = self.search_view.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.Fixed)
        v_header.setDefaultSectionSize(20)

        # Toggle add button
        self.search_selection_model = self.search_view.selectionModel()
        self.search_selection_model.selectionChanged.connect(self.toggle_add_btn)

        self.search_view.show()

    def add_to_fridge(self):
        selected_item_ixs = self.search_view.selectionModel().selectedRows()
        for ix in selected_item_ixs:
            food_name_ix = ix.siblingAtColumn(Search.attr_to_col['name'])
            food_name = self.search_model.data(food_name_ix, Qt.DisplayRole)

            # Fridge can only have one entry for each food
            if food_name not in set([food.name for food in self.person.foods]):
                food_to_add = spartan.Food(name=food_name)
                self.fridge_model.insertRows(0, food_to_add)
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

        add_shortcut = QShortcut(QKeySequence(Qt.Key_Return), self.search_view)
        add_shortcut.activated.connect(self.add_to_fridge)

        self.debug_btn.clicked.connect(self.print_debug_info)
        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        print(self.person.restrict_types)
        print(self.person.restrict_fds)
