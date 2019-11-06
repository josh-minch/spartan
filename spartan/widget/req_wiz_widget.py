import sys
import datetime

from PySide2.QtCore import Qt
from PySide2.QtGui import QKeySequence, QPalette, QIntValidator, QFont, QPalette, QColor, QPixmap
from PySide2.QtWidgets import (QApplication, QWidget, QStyleFactory, QDialog, QShortcut,
                               QHeaderView, QListView, QStyledItemDelegate, QStyleFactory)

from spartan import *
import req
from gui_constants import *
import gui_helpers
from model.requirements_model import RequirementsModel
from delegate.lineedit_delegate import LineEditDelegate
from ui.ui_reqwizwidget import Ui_ReqWizWidget


class ReqWizWidget(QWidget, Ui_ReqWizWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setup_connections()
        self.set_validators()
        self.set_defaults()
        self.init_req()
        self.sex_edit.setView(QListView())

    def set_defaults(self):
        self.bd_year, self.bd_mon, self.bd_day = None, None, None
        self.sex = 'f'

    def set_validators(self):
        int_validator = QIntValidator()
        self.day_edit.setValidator(int_validator)
        self.mon_edit.setValidator(int_validator)
        self.year_edit.setValidator(int_validator)

    def init_req(self):
        self.macro, self.vit, self.mineral = req.get_empty_reqs()
        self.display_req()

    def update_displayed_req(self):
        if not self.fields_are_valid():
            return

        self.age_range = req.calculate_age_range(
            self.bd_year, self.bd_mon, self.bd_day)
        self.macro, self.vit, self.mineral = req.get_reqs(
            self.age_range, self.sex)

        self.display_req()

    def display_req(self):
        self.macro_model = RequirementsModel(
            nutrients=self.macro, nutrient_group='General')
        self.vit_model = RequirementsModel(
            nutrients=self.vit, nutrient_group='Vitamins')
        self.mineral_model = RequirementsModel(
            nutrients=self.mineral, nutrient_group='Minerals')

        self.macro_view.setModel(self.macro_model)
        self.vit_view.setModel(self.vit_model)
        self.mineral_view.setModel(self.mineral_model)

        self.setup_req_view(self.macro_view)
        self.setup_req_view(self.vit_view)
        self.setup_req_view(self.mineral_view)

    def setup_req_view(self, view):
        gui_helpers.hide_view_cols(view, [Req.attr_to_col['nut_id']])
        view.setColumnWidth(Req.attr_to_col['name'], 150)
        gui_helpers.vertical_resize_table_view_to_contents(view)
        gui_helpers.set_header_font(view, FONT_SECONDARY_SIZE, QFont.DemiBold)

    def fields_are_valid(self):
        if None in (self.bd_day, self.bd_mon, self.bd_year):
            return False
        if not self.valid_date():
            return False
        if len(str(self.bd_year)) < 4:
            return False
        return True

    def valid_date(self):
        try:
            datetime.datetime(self.bd_year, self.bd_mon, self.bd_day)
            date_validity = True
        except ValueError:
            date_validity = False
        return date_validity

    def day_edit_changed(self, day):
        self.bd_day = int(day)
    def mon_edit_changed(self, mon):
        self.bd_mon = int(mon)
    def year_edit_changed(self, year):
        self.bd_year = int(year)
    def sex_edit_changed(self, index):
        self.sex = index_to_sex[index]

    def setup_connections(self):
        self.day_edit.textChanged.connect(self.day_edit_changed)
        self.mon_edit.textChanged.connect(self.mon_edit_changed)
        self.year_edit.textChanged.connect(self.year_edit_changed)
        self.sex_edit.currentIndexChanged[int].connect(self.sex_edit_changed)

        self.day_edit.textChanged.connect(self.update_displayed_req)
        self.mon_edit.textChanged.connect(self.update_displayed_req)
        self.year_edit.textChanged.connect(self.update_displayed_req)
        self.sex_edit.currentIndexChanged[int].connect(self.update_displayed_req)

        # Debug
        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        print(self.person.macro)
