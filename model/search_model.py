from PySide2.QtCore import (Qt, QAbstractTableModel)

from constants import fd_grp_search_name
from gui_constants import Search

class SearchModel(QAbstractTableModel):
    def __init__(self, search_result):
        QAbstractTableModel.__init__(self)
        self.search_result = search_result

    def rowCount(self, parent):
        return len(self.search_result)

    def columnCount(self, parent):
        return len(Search.attrs)

    def data(self, index, role):
        if not index.isValid() or not 0 <= index.row() < len(self.search_result):
            return None

        if role == Qt.DisplayRole:
            value = self.search_result[index.row()][index.column()]
            if index.column() == Search.attr_to_col['fd_grp']:
                return fd_grp_search_name[value]
            else:
                return value

        return None
