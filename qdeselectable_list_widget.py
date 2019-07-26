from PySide2 import QtCore, QtWidgets, QtGui

class QDeselectableListWidget(QtWidgets.QListWidget):
    def mousePressEvent(self, event):
        item = self.indexAt(event.pos())
        if (item.isValid() is not True):
            self.clearSelection()
        QtWidgets.QListWidget.mousePressEvent(self, event)