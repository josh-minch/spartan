from PySide2.QtCore import Qt, QItemSelectionModel, QTimer
from PySide2.QtWidgets import QTableView

from delegate.combobox_delegate import ComboBoxDelegate
from gui_constants import *


class ComboTableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setItemDelegateForColumn(PRICE_UNIT_COL, ComboBoxDelegate(self))
        self.setItemDelegateForColumn(MIN_UNIT_COL, ComboBoxDelegate(self))
        self.setItemDelegateForColumn(MAX_UNIT_COL, ComboBoxDelegate(self))
        self.setItemDelegateForColumn(TARGET_UNIT_COL, ComboBoxDelegate(self))
        self.setItemDelegateForColumn(NUT_QUANT_UNIT_COL, ComboBoxDelegate(self))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            ix = self.indexAt(event.pos())

            # When opening combobox, also select current row
            '''
            selection = self.selectionModel()
            if selection:
                row_ix = self.model().index(ix.row(), 0)
                selection.setCurrentIndex(
                    row_ix, QItemSelectionModel.ClearAndSelect)
            '''

            QTimer.singleShot(1, self, self.edit(ix))
            event.setAccepted(True)
            return

        super().mousePressEvent(event)
