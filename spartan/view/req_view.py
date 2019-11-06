from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTableView

from delegate.lineedit_delegate import LineEditDelegate

import gui_helpers

class ReqView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setItemDelegate(LineEditDelegate())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            ix = self.indexAt(event.pos())
            self.edit(ix)
        super().mousePressEvent(event)
