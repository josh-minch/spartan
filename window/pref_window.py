import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QStyleFactory)

import database
from ui.ui_prefwindow import Ui_PrefWindow
from widget.pref_widget import PrefWidget
from widget.req_widget import ReqWidget
from widget.res_widget import ResWidget


class PrefWindow(QMainWindow, Ui_PrefWindow):
    def __init__(self, parent=None, person=None, type_res=None, fd_res=None):
        super().__init__(parent)
        self.setupUi(self)
        self.stacked_widget = QStackedWidget()

        self.pref_widget = PrefWidget(person, type_res, fd_res)
        self.req_widget = ReqWidget(person)
        self.res_widget = ResWidget(person, type_res, fd_res)

        self.stacked_widget.addWidget(self.pref_widget)
        self.stacked_widget.addWidget(self.req_widget)
        self.stacked_widget.addWidget(self.res_widget)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        lay = QVBoxLayout(central_widget)
        lay.addWidget(self.stacked_widget)

        self.setup_connections()
        self.resize(900,600)
        self.show()

    def setup_connections(self):
        self.pref_widget.req_btn.clicked.connect(self.show_req)
        self.pref_widget.res_btn.clicked.connect(self.show_res)

        self.req_widget.back_btn.clicked.connect(self.show_pref)
        self.res_widget.back_btn.clicked.connect(self.show_pref)

    def show_req(self):
        self.stacked_widget.setCurrentWidget(self.req_widget)

    def show_res(self):
        self.stacked_widget.setCurrentWidget(self.res_widget)

    def show_pref(self):
        self.pref_widget.set_preview_text()
        self.stacked_widget.setCurrentWidget(self.pref_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle(QStyleFactory.create('fusion'))
    dialog = PrefWindow()
    sys.exit(app.exec_())