from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget

from ui.ui_prefwidget import Ui_PrefWidget


class PrefWidget(QWidget, Ui_PrefWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.req_btn.setIcon(QPixmap("images/person-outline.png"))
        self.res_btn.setIcon(QPixmap("images/food.png"))

