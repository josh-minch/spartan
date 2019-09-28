from PySide2.QtCore import (Qt, QAbstractTableModel)

class SearchModel(QAbstractTableModel):
    def __init__(self, search_result):
        QAbstractTableModel.__init__(self)
        self.search_result = search_result

    def rowCount(self, parent):
        return len(self.search_result)

    def columnCount(self, parent):
        return 1
        #return len(SEARCH_COLS)

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return Qt.NoItemFlags
        return self.search_result[index.row()]
