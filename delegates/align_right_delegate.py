from PySide2.QtWidgets import QStyledItemDelegate, QLineEdit
from PySide2.QtCore import Qt

from gui_constants import *

class AlignRightDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, *args):
        QStyledItemDelegate.__init__(self, parent, *args)

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setAlignment(Qt.AlignRight)
        return editor

