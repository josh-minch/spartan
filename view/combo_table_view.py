from PySide2.QtCore import Qt, QItemSelectionModel, QTimer
from PySide2.QtWidgets import QTableView

from delegate.combobox_delegate import ComboBoxDelegate
from delegate.lineedit_delegate import LineEditDelegate
from gui_constants import *
import gui_helpers


class ComboTableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        gui_helpers.fix_header_font(self)
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
                row_ix = self.model().index(ix.row(), 0)
                selection.setCurrentIndex(
                    row_ix, QItemSelectionModel.ClearAndSelect)

            QTimer.singleShot(1, self, self.edit(ix))
            event.setAccepted(True)

        super().mousePressEvent(event)
