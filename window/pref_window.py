import sys

from PySide2.QtCore import Qt, QSettings
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QStyleFactory)

import spartan
import database
from ui.ui_prefwindow import Ui_PrefWindow
from widget.pref_widget import PrefWidget
from widget.req_widget import ReqWidget
from widget.res_widget import ResWidget


class PrefWindow(QMainWindow, Ui_PrefWindow):
    def __init__(self, parent=None, person=None, type_res=None, fd_res=None):
        super().__init__(parent)
        self.setupUi(self)
        self.person = person
        self.type_res = type_res
        self.fd_res = fd_res

        self.add_widgets()

        self.setup_connections()
        #self.resize(900,600)
        self.read_settings()
        self.show()

    def get_sex_bd(self):
        sex, bd_year, bd_mon, bd_day = spartan.get_sex_bd_from_db()
        return (sex, (bd_year, bd_mon, bd_day))

    def add_widgets(self):
        sex, bd = self.get_sex_bd()
        self.pref_widget = PrefWidget(sex, bd, self.type_res, self.fd_res)
        self.req_widget = ReqWidget(self.person, sex, *bd)
        self.res_widget = ResWidget(self.type_res, self.fd_res)

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.pref_widget)
        self.stacked_widget.addWidget(self.req_widget)
        self.stacked_widget.addWidget(self.res_widget)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        lay = QVBoxLayout(central_widget)
        lay.addWidget(self.stacked_widget)

    def show_req(self):
        self.stacked_widget.setCurrentWidget(self.req_widget)

    def show_res(self):
        self.stacked_widget.setCurrentWidget(self.res_widget)

    def show_pref(self):
        self.pref_widget.sex = self.req_widget.sex
        self.pref_widget.bd = (self.req_widget.bd_year, self.req_widget.bd_mon, self.req_widget.bd_day)
        self.pref_widget.set_preview_text()
        self.stacked_widget.setCurrentWidget(self.pref_widget)

    def setup_connections(self):
        self.pref_widget.req_btn.clicked.connect(self.show_req)
        self.pref_widget.res_btn.clicked.connect(self.show_res)

        self.req_widget.back_btn.clicked.connect(self.show_pref)
        self.res_widget.back_btn.clicked.connect(self.show_pref)

    def closeEvent(self, event):
        settings = QSettings("spartan", "spartan")
        settings.setValue("pref/geometry", self.saveGeometry())
        settings.setValue("pref/windowState", self.saveState())
        super().closeEvent(self, event)

    def read_settings(self):
        settings = QSettings("spartan", "spartan")
        self.restoreGeometry(settings.value("pref/geometry"))
        self.restoreState(settings.value("pref/windowState"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle(QStyleFactory.create('fusion'))
    dialog = PrefWindow()
    sys.exit(app.exec_())
