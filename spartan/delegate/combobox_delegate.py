'''
MIT License

Copyright(c) 2019 Pierre Baillargeon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

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
        if not editor:
            return
        current_text = index.data(QtCore.Qt.EditRole)
        current_index = editor.findText(current_text)
        if current_index >= 0:
            editor.setCurrentIndex(current_index)
        if not editor.isVisible():
            editor.showPopup()

    def setModelData(self, editor, model, index):
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

if __name__ == '__main__':
    pass
