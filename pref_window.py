import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QStyleFactory)

import database
from ui.ui_prefwindow import Ui_PrefWindow
from pref_widget import PrefWidget
from req_widget import ReqWidget
from res_widget import ResWidget


class PrefWindow(QMainWindow, Ui_PrefWindow):
    def __init__(self, parent=None, person=None):
        super().__init__(parent)
        self.setupUi(self)
        self.stacked_widget = QStackedWidget()

        presets, types, fd_grps = [], [], []
        self.pref_widget = PrefWidget()
        self.req_widget = ReqWidget()
        self.res_widget = ResWidget(presets, types, fd_grps)

        self.stacked_widget.addWidget(self.pref_widget)
        self.stacked_widget.addWidget(self.req_widget)
        self.stacked_widget.addWidget(self.res_widget)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        lay = QVBoxLayout(central_widget)
        lay.addWidget(self.stacked_widget)

        self.setup_connections()
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
        self.stacked_widget.setCurrentWidget(self.pref_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = PrefWindow()
    sys.exit(app.exec_())