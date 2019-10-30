import sys
from functools import partial

from PySide2 import QtGui, QtCore, QtWidgets
from gui_constants import *


class ComboBoxDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QComboBox(parent)
        editor.setView(QtWidgets.QListView())
        items_ix = index.model().index(index.row(), SELECTABLE_UNITS_COL)
        items = index.model().data(items_ix)
        editor.addItems(items)

        width = [editor.fontMetrics().boundingRect(item).width() for item in items]
        editor.view().setMinimumWidth(max(width) + 9)

        editor.view().window().setWindowFlags(QtCore.Qt.Popup | QtCore.Qt.NoDropShadowWindowHint )
        # When current item is changed, commit the data and close immedtiately
        editor.currentTextChanged[str].connect(partial(self.commit_and_close, editor))
        return editor

    def commit_and_close(self, editor, text):
        if editor.isVisible():
            self.commitData.emit(editor)
            self.closeEditor.emit(editor)

    def setEditorData(self, editor, index):
        print('setEditorData')
        if not editor:
            return
        current_text = index.data(QtCore.Qt.EditRole)
        current_index = editor.findText(current_text)
        if current_index >= 0:
            editor.setCurrentIndex(current_index)
        if not editor.isVisible():
            editor.showPopup()

    def setModelData(self, editor, model, index):
        print('setModelData')
        if not editor:
            return
        model.setData(index, editor.currentText(), QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def paint(self, painter, option, index):
        box = QtWidgets.QStyleOptionComboBox()
        box.state = option.state
        box.rect = option.rect
        box.currentText = index.data(QtCore.Qt.EditRole)

        QtWidgets.QApplication.style().drawComplexControl(
            QtWidgets.QStyle.CC_ComboBox, box, painter)
        QtWidgets.QApplication.style().drawControl(QtWidgets.QStyle.CE_ComboBoxLabel, box, painter)

    '''
    def sizeHint(self, option, index):
        box = QtWidgets.QStyleOptionComboBox()
        box.state = option.state
        box.rect = option.rect
        size = QtCore.QSize(0, 0)

        items_ix = index.model().index(index.row(), SELECTABLE_UNITS_COL)
        items = index.model().data(items_ix)
        for item in items:
            box.currentText = text
            rect = QtWidgets.QApplication.style().itemTextRect(option.fontMetrics, option.rect, QtCore.Qt.AlignCenter, True, item)
            size = size.expandedTo(QtWidgets.QApplication.style().sizeFromContents(QtWidgets.QStyle.ContentsType.CT_ComboBox,
                box, rect.size(), option.widget))
        return size
    '''
if __name__ == '__main__':
    pass
