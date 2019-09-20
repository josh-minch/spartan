from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget

from ui.ui_reswidget import Ui_ResWidget


class ResWidget(QWidget, Ui_ResWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.back_btn.setIcon(QPixmap("images/back-black.svg"))