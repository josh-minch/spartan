import sys
from PySide2 import QtGui, QtCore, QtWidgets


class ComboBoxDelegate(QtWidgets.QItemDelegate):
    def __init__(self, food, parent=None):
        super().__init__(parent)
        self.food = food
        self.items = food.selectable_units

    def createEditor(self, widget, option, index):
        editor = QtWidgets.QComboBox(widget)
        editor.addItems(self.items)
        return editor

    def setEditorData(self, editor, index):
        print('setEditorData')
        current_text = index.data(QtCore.Qt.EditRole)
        current_index = editor.findText(current_text)
        if current_index >= 0:
            editor.setCurrentIndex(current_index)

    def setModelData(self, editor, model, index):
        print('setModelData')
        model.setData(index, editor.currentText(), QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def paint(self, painter, option, index):
        text = self.items[index.row()]
        option.text = text
        QtWidgets.QApplication.style().drawControl(QtWidgets.QStyle.CE_ItemViewItem, option, painter)

if __name__ == '__main__':
    pass
