import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QKeySequence, QPalette
from PySide2.QtWidgets import QApplication, QStyleFactory, QDialog, QShortcut

from spartan import *
import req
from gui_constants import *
from requirements_model import RequirementsModel
from ui_requirementswindow import Ui_RequirementsWindow


class RequirementsWindow(QDialog, Ui_RequirementsWindow):
    def __init__(self, parent=None, person=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_defaults()
        self.setup_connections()
        self.show()

    def set_defaults(self):
        self.bd_day = None
        self.bd_mon = None
        self.bd_year = None
        self.sex = 'f'
        self.req = 'us'

    def init_person(self):
        person = Person('name', self.sex, self.bd_day, self.bd_month, self.bd_year) 

        person.set_nuts()

    def display_req(self):
        if None in (self.bd_day, self.bd_mon, self.bd_year):
            return
        
        self.age_range = req.calculate_age_range(self.bd_year, self.bd_mon, self.bd_day)
        nutrients = req.get_min(self.age_range, self.sex)
        self.requirements_model = RequirementsModel(nutrients=nutrients)
        self.req_view.setModel(self.requirements_model)

    def day_edit_changed(self):
        self.bd_day = int(self.day_edit.text())

    def mon_edit_changed(self):
        self.bd_mon = int(self.mon_edit.text())

    def year_edit_changed(self):
        self.bd_year = int(self.year_edit.text())

    def sex_edit_changed(self, index):
        self.sex = INDEX_TO_SEX[index]

    def req_edit_changed(self, req):
        self.req = req

    def cust_edit_changed(self):
        if self.cust_edit.isChecked():
            pass

    def setup_connections(self):
        self.day_edit.textChanged.connect(self.day_edit_changed)
        self.mon_edit.textChanged.connect(self.mon_edit_changed)
        self.year_edit.textChanged.connect(self.year_edit_changed)
        self.sex_edit. currentIndexChanged[int].connect(self.sex_edit_changed)
        self.req_edit. currentIndexChanged[int].connect(self.req_edit_changed)
        self.cust_edit.stateChanged.connect(self.cust_edit_changed)

        self.day_edit.textChanged.connect(self.display_req)
        self.mon_edit.textChanged.connect(self.display_req)
        self.year_edit.textChanged.connect(self.display_req)
        self.sex_edit. currentIndexChanged[int].connect(self.display_req)
        self.req_edit. currentIndexChanged[int].connect(self.display_req)

        # Debug 
        self.debug_btn.clicked.connect(self.print_debug_info)
        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):

        try:
            print("bd_day is {}".format(self.bd_day))
        except AttributeError as e:
            print ("no bd_day")

        try:
            print("mon is {}".format(self.bd_mon))
        except AttributeError as e:
            print ("no mon")

        try:
            print("year is {}".format(self.bd_year))
        except AttributeError as e:
            print ("no year")

        try:
            print("age_range is {}".format(self.age_range))
        except AttributeError as e:
            print ("no age")

        print("sex is " + self.sex)
        print("req is " + self.req)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    app.setStyle(QStyleFactory.create('fusion'))
    p = QPalette()
    p.setColor(QPalette.Highlight, Qt.darkRed)
    app.setPalette(p)

    dialog = RequirementsWindow()
    sys.exit(app.exec_())