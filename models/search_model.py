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

        if not index.isValid() or not 0 <= index.row() < len(self.foods):
            return None

        if role in (Qt.DisplayRole, Qt.EditRole):
            attr_str = o_col_to_attr[index.column()]
            return self.foods[index.row()][attr_str]

        # A bug in PySide2 requires that we cast the bitwise
        # AlignmentFlag to an int before returning
        # https://bugreports.qt.io/browse/PYSIDE-20
        if role == Qt.TextAlignmentRole:
            if index.column() == O_AMOUNT_COL:
                return int(Qt.AlignRight | Qt.AlignVCenter)

        return None
