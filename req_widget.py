import sys
import datetime

from PySide2.QtCore import Qt
from PySide2.QtGui import QKeySequence, QPalette, QIntValidator, QFont, QPalette, QColor, QPixmap
from PySide2.QtWidgets import (QApplication, QWidget, QStyleFactory, QDialog, QShortcut,
QHeaderView, QListView, QStyledItemDelegate, QStyleFactory)

from spartan import *
import req
from gui_constants import *
from models.requirements_model import MacroModel, VitModel, MineralModel
from ui.ui_reqwidget import Ui_ReqWidget


class ReqWidget(QWidget, Ui_ReqWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.back_btn.setIcon(QPixmap("images/back-black.svg"))
        self.set_defaults()
        self.setup_connections()

        int_validator = QIntValidator()
        self.day_edit.setValidator(int_validator)
        self.mon_edit.setValidator(int_validator)
        self.year_edit.setValidator(int_validator)

        self.cust_edit.setStyle(QStyleFactory.create('windowsvista'))

        self.req_edit.setView(QListView())
        self.sex_edit.setView(QListView())

    def set_defaults(self):
        self.bd_day = None
        self.bd_mon = None
        self.bd_year = None
        self.sex = 'f'
        self.req = 'us'

    def init_person(self):
        person = Person('name', self.sex, self.bd_day, self.bd_month, self.bd_year)
        person.set_nuts()

    def valid_date(self):
        try:
            datetime.datetime(self.bd_year, self.bd_mon, self.bd_day)
            date_validity = True
        except ValueError:
            date_validity = False
        return date_validity

    def display_req(self):
        if None in (self.bd_day, self.bd_mon, self.bd_year):
            return
        if not self.valid_date():
            return
        if len(str(self.bd_year)) < 4:
            return

        self.age_range = req.calculate_age_range(self.bd_year, self.bd_mon, self.bd_day)
        (macro, vit, mineral) = req.get_reqs(self.age_range, self.sex)

        self.macro_model = MacroModel(nutrients=macro)
        self.vit_model = VitModel(nutrients=vit)
        self.mineral_model = MineralModel(nutrients=mineral)

        self.macro_view.setModel(self.macro_model)
        self.vit_view.setModel(self.vit_model)
        self.mineral_view.setModel(self.mineral_model)

        self.macro_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.vit_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.mineral_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def cust_edit_changed(self):
        if self.cust_edit.isChecked():
            pass

    def setup_connections(self):
        self.day_edit.textChanged.connect(self.day_edit_changed)
        self.mon_edit.textChanged.connect(self.mon_edit_changed)
        self.year_edit.textChanged.connect(self.year_edit_changed)
        self.sex_edit.currentIndexChanged[int].connect(self.sex_edit_changed)
        self.req_edit.currentIndexChanged[int].connect(self.req_edit_changed)
        self.cust_edit.stateChanged.connect(self.cust_edit_changed)

        self.day_edit.textChanged.connect(self.display_req)
        self.mon_edit.textChanged.connect(self.display_req)
        self.year_edit.textChanged.connect(self.display_req)
        self.sex_edit.currentIndexChanged[int].connect(self.display_req)
        self.req_edit.currentIndexChanged[int].connect(self.display_req)

        # Debug
        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        pass

    def day_edit_changed(self, day):
        self.bd_day = int(day)
    def mon_edit_changed(self, mon):
        self.bd_mon = int(mon)
    def year_edit_changed(self, year):
        self.bd_year = int(year)
    def sex_edit_changed(self, index):
        self.sex = INDEX_TO_SEX[index]
    def req_edit_changed(self, req_text):
        self.req_text = req_text