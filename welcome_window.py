import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget

from ui.ui_welcomewindow import Ui_WelcomeWindow


class WelcomeWindow(QMainWindow, Ui_WelcomeWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle(QStyleFactory.create('fusion'))
    welcome_window = WelcomeWindow()
    sys.exit(app.exec_())
