import sys
import datetime

from PySide2.QtCore import Qt
from PySide2.QtGui import QKeySequence, QPalette, QIntValidator, QFont, QPalette, QColor, QPixmap
from PySide2.QtWidgets import (QApplication, QWidget, QStyleFactory, QDialog, QShortcut,
                               QHeaderView, QListView, QStyledItemDelegate, QStyleFactory)

import spartan
import req
from gui_constants import *
import gui_helpers
from model.requirements_model import RequirementsModel
from delegate.lineedit_delegate import LineEditDelegate
from ui.ui_reqwidget import Ui_ReqWidget


class ReqWidget(QWidget, Ui_ReqWidget):
    def __init__(self, person, sex, bd_year, bd_mon, bd_day, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.person = person
        self.sex = sex
        self.bd_year = bd_year
        self.bd_mon = bd_mon
        self.bd_day = bd_day

        self.macro, self.vit, self.mineral = spartan.get_nut_groups(self.person.nuts)

        self.set_defaults()
        self.setup_connections()
        self.set_validators()
        self.sex_edit.setView(QListView())
        self.display_req()

    def set_defaults(self):
        self.year_edit.setText(str(self.bd_year))
        self.mon_edit.setText(str(self.bd_mon))
        self.day_edit.setText(str(self.bd_day))

        self.sex_edit.setCurrentIndex(sex_to_index[self.sex])

    def set_validators(self):
        int_validator = QIntValidator()
        self.day_edit.setValidator(int_validator)
        self.mon_edit.setValidator(int_validator)
        self.year_edit.setValidator(int_validator)

    def valid_date(self):
        try:
            datetime.datetime(self.bd_year, self.bd_mon, self.bd_day)
            date_validity = True
        except ValueError:
            date_validity = False
        return date_validity

    def fields_are_valid(self):
        if None in (self.bd_year, self.bd_mon, self.bd_day):
            return False
        if not self.valid_date():
            return False
        if len(str(self.bd_year)) < 4:
            return False
        return True

    def update_req_display(self):
        if not self.fields_are_valid():
            return

        spartan.update_sex_bd_in_db(self.sex, self.bd_year, self.bd_mon, self.bd_day)

        age_range = req.calculate_age_range(self.bd_year, self.bd_mon, self.bd_day)
        self.macro, self.vit, self.mineral = req.get_reqs(age_range, self.sex)

        self.person.set_nuts(self.macro + self.vit + self.mineral)

        self.display_req()

    def display_req(self):
        self.macro_model = RequirementsModel(
            nutrients=self.macro, nutrient_group='General', person=self.person)
        self.vit_model = RequirementsModel(
            nutrients=self.vit, nutrient_group='Vitamins', person=self.person)
        self.mineral_model = RequirementsModel(
            nutrients=self.mineral, nutrient_group='Minerals', person=self.person)

        self.macro_view.setModel(self.macro_model)
        self.vit_view.setModel(self.vit_model)
        self.mineral_view.setModel(self.mineral_model)

        self.setup_req_view(self.macro_view)
        self.setup_req_view(self.vit_view)
        self.setup_req_view(self.mineral_view)


    def setup_req_view(self, view):
        gui_helpers.hide_view_cols(view, [Req.attr_to_col['nut_id']])
        view.setColumnWidth(Req.attr_to_col['name'], 150)
        #gui_helpers.set_header_font(view, FONT_SECONDARY_SIZE, QFont.DemiBold)
        gui_helpers.vertical_resize_table_view_to_contents(view)

    def update_req(self):
        pass

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

        self.day_edit.textChanged.connect(self.update_req_display)
        self.mon_edit.textChanged.connect(self.update_req_display)
        self.year_edit.textChanged.connect(self.update_req_display)
        self.sex_edit.currentIndexChanged[int].connect(self.update_req_display)

        # Debug
        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        print(self.person.nuts[0])
