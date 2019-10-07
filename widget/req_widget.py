import sys
import datetime

from PySide2.QtCore import Qt
from PySide2.QtGui import QKeySequence, QPalette, QIntValidator, QFont, QPalette, QColor, QPixmap
from PySide2.QtWidgets import (QApplication, QWidget, QStyleFactory, QDialog, QShortcut,
                               QHeaderView, QListView, QStyledItemDelegate, QStyleFactory)

from spartan import *
import req
from gui_constants import *
from model.requirements_model import RequirementsModel
from delegate.lineedit_delegate import LineEditDelegate
from ui.ui_reqwidget import Ui_ReqWidget


class ReqWidget(QWidget, Ui_ReqWidget):
    def __init__(self, person, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.person = person
        self.back_btn.setIcon(QPixmap("images/back-black.svg"))
        self.set_defaults()
        self.setup_connections()

        int_validator = QIntValidator()
        self.day_edit.setValidator(int_validator)
        self.mon_edit.setValidator(int_validator)
        self.year_edit.setValidator(int_validator)

        self.rec_edit.setView(QListView())
        self.sex_edit.setView(QListView())
        self.display_req()

    def set_defaults(self):
        self.day_edit.setText(str(self.person.bd_day))
        self.mon_edit.setText(str(self.person.bd_mon))
        self.year_edit.setText(str(self.person.bd_year))
        self.sex_edit.setCurrentIndex(sex_to_index[self.person.sex])
        self.rec_edit.setCurrentIndex(rec_to_index[self.person.rec])

    def valid_date(self):
        try:
            datetime.datetime(self.person.bd_year,
                              self.person.bd_mon, self.person.bd_day)
            date_validity = True
        except ValueError:
            date_validity = False
        return date_validity

    def display_req(self):
        if None in (self.person.bd_day, self.person.bd_mon, self.person.bd_year):
            return
        if not self.valid_date():
            return
        if len(str(self.person.bd_year)) < 4:
            return

        self.person.set_nuts()

        self.macro_model = RequirementsModel(nutrients=self.person.macro, nutrient_group='Macronutrients')
        self.vit_model = RequirementsModel(nutrients=self.person.vit, nutrient_group='Vitamins')
        self.mineral_model = RequirementsModel(nutrients=self.person.mineral, nutrient_group='Minerals')

        self.macro_view.setItemDelegate(LineEditDelegate())
        self.vit_view.setItemDelegate(LineEditDelegate())
        self.mineral_view.setItemDelegate(LineEditDelegate())

        self.macro_view.setModel(self.macro_model)
        self.vit_view.setModel(self.vit_model)
        self.mineral_view.setModel(self.mineral_model)

        self.macro_view.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.vit_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.mineral_view.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)

    def cust_edit_changed(self):
        if self.cust_edit.isChecked():
            pass

    def day_edit_changed(self, day):
        self.person.bd_day = int(day)
    def mon_edit_changed(self, mon):
        self.person.bd_mon = int(mon)
    def year_edit_changed(self, year):
        self.person.bd_year = int(year)
    def sex_edit_changed(self, index):
        self.person.sex = index_to_sex[index]
    def rec_edit_changed(self, rec_text):
        self.person.rec_text = rec_text

    def setup_connections(self):
        self.day_edit.textChanged.connect(self.day_edit_changed)
        self.mon_edit.textChanged.connect(self.mon_edit_changed)
        self.year_edit.textChanged.connect(self.year_edit_changed)
        self.sex_edit.currentIndexChanged[int].connect(self.sex_edit_changed)
        self.rec_edit.currentIndexChanged[int].connect(self.rec_edit_changed)
        self.cust_edit.stateChanged.connect(self.cust_edit_changed)

        self.day_edit.textChanged.connect(self.display_req)
        self.mon_edit.textChanged.connect(self.display_req)
        self.year_edit.textChanged.connect(self.display_req)
        self.sex_edit.currentIndexChanged[int].connect(self.display_req)
        self.rec_edit.currentIndexChanged[int].connect(self.display_req)

        # Debug
        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        print(self.person.macro)
