from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QIntValidator, QRegExpValidator
from PySide2.QtWidgets import QStyledItemDelegate, QLineEdit


class LineEditDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setAlignment(Qt.AlignRight)
        regex = QRegExp('^[0-9]*$')
        editor.setValidator(QRegExpValidator(regex, self))
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        if (value == '-'):
            value = ''
        editor.setText(str(value))

    def setModelData(self, editor, model, index):
        value = editor.text()
        if value in ('', '-', 'None'):
             model.setData(index, None, Qt.EditRole)
        else:
            model.setData(index, int(value), Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

if __name__ == "__main__":
    import sys
    from PySide2 import *

    app = QtWidgets.QApplication(sys.argv)
    line_edit_delegate = LineEditDelegate()

    model = QtGui.QStandardItemModel(3, 1)
    table_view = QtWidgets.QTableView()
    table_view.setModel(model)

    delegate = LineEditDelegate()
    table_view.setItemDelegate(delegate)

    for row in range(4):
        index = model.index(row, 1, QtCore.QModelIndex())
        model.setData(index, row)

    table_view.show()
    sys.exit(app.exec_())
