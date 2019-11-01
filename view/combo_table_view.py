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

from PySide2.QtCore import Qt, QItemSelectionModel, QItemSelection, QTimer, Signal
from PySide2.QtWidgets import QTableView

from delegate.combobox_delegate import ComboBoxDelegate
from delegate.lineedit_delegate import LineEditDelegate
from gui_constants import *
import gui_helpers


class ComboTableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setItemDelegateForColumn(PRICE_UNIT_COL, ComboBoxDelegate(self))
        self.setItemDelegateForColumn(MIN_UNIT_COL, ComboBoxDelegate(self))
        self.setItemDelegateForColumn(MAX_UNIT_COL, ComboBoxDelegate(self))
        self.setItemDelegateForColumn(TARGET_UNIT_COL, ComboBoxDelegate(self))
        self.setItemDelegateForColumn(NUT_QUANT_UNIT_COL, ComboBoxDelegate(self))

        self.setItemDelegateForColumn(PRICE_COL, LineEditDelegate(self))
        self.setItemDelegateForColumn(PRICE_QUANTITY_COL, LineEditDelegate(self))
        self.setItemDelegateForColumn(MIN_COL, LineEditDelegate(self))
        self.setItemDelegateForColumn(MAX_COL, LineEditDelegate(self))
        self.setItemDelegateForColumn(TARGET_COL, LineEditDelegate(self))
        self.setItemDelegateForColumn(NUT_QUANT_COL, LineEditDelegate(self))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            ix = self.indexAt(event.pos())

            # When opening combobox, also select current row
            selection = self.selectionModel()
            if selection:
                # select entire row of currently selected index
                top_left = self.model().index(ix.row(), 0)
                bottom_right = self.model().index(ix.row(), 14)
                item_selection = QItemSelection(top_left, bottom_right)

                selection.select(
                    item_selection, QItemSelectionModel.ClearAndSelect)

            QTimer.singleShot(1, self, self.edit(ix))
            event.setAccepted(True)
            return

        QTableView.mousePressEvent(event)
