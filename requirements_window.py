import sys

from PySide2.QtCore import Qt, QModelIndex
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import (QApplication, QDialog, QHeaderView, QShortcut)

import database
from gui_constants import *
from ui_requirementswindow import Ui_RequirementsWindow
#from requirements_model import RequirementsModel

class RequirementsWindow(QDialog, Ui_RequirementsWindow):
    def __init__(self, parent=None, person=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = RequirementsWindow()
    sys.exit(app.exec_())