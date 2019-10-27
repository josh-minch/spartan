from PySide2.QtCore import Qt, QItemSelectionModel, QItemSelection, QTimer
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

        super().mousePressEvent(event)
