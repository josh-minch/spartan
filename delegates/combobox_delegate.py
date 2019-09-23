import sys
from PySide2 import QtGui, QtCore, QtWidgets
from gui_constants import *


class ComboBoxDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, food, parent=None):
        super().__init__(parent)
        self.food = food
        self.items = food.selectable_units

    def createEditor(self, parent, option, index):
        if index.column() in (PRICE_COL, PRICE_QUANTITY_COL):
            editor = QtWidgets.QLineEdit(parent)
        else:
            editor = QtWidgets.QComboBox(parent)
            editor.addItems(self.items)
        return editor

    def setEditorData(self, editor, index):
        if index.column() not in UNIT_COL:
            return
        print('setEditorData')
        current_text = index.data(QtCore.Qt.EditRole)
        current_index = editor.findText(current_text)
        if current_index >= 0:
            editor.setCurrentIndex(current_index)

    def setModelData(self, editor, model, index):
        if index.column() not in UNIT_COL:
            return
        print('setModelData')
        model.setData(index, editor.currentText(), QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def paint(self, painter, option, index):
        if index.column() not in UNIT_COL:
            QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)
            return
        text = index.data(QtCore.Qt.EditRole)
        option.text = text
        QtWidgets.QApplication.style().drawControl(QtWidgets.QStyle.CE_ItemViewItem, option, painter)

if __name__ == '__main__':
    pass
