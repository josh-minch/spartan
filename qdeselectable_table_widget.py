from PySide2 import QtCore, QtWidgets, QtGui

class QDeselectableTableWidget(QtWidgets.QTableWidget):
    def mousePressEvent(self, event):
        item = self.indexAt(event.pos())
        if (item.isValid() is not True):
            self.clearSelection()
        QtWidgets.QTableWidget.mousePressEvent(self, event)