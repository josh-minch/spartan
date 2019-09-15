import sys

from PySide2.QtCore import *
from PySide2.QtWidgets import *

class ComboDelegate(QItemDelegate):
    editorItems=['Combo_Zero', 'Combo_One','Combo_Two']
    height = 25
    width = 200
    def createEditor(self, parent, option, index):
        editor = QListWidget(parent)
        # editor.addItems(self.editorItems)
        # editor.setEditable(True)
        editor.currentItemChanged.connect(self.currentItemChanged)
        return editor

    def setEditorData(self,editor,index):
        z = 0
        for item in self.editorItems:
            ai = QListWidgetItem(item)
            editor.addItem(ai)
            if item == index.data():
                editor.setCurrentItem(editor.item(z))
            z += 1
        editor.setGeometry(0,index.row()*self.height,self.width,self.height*len(self.editorItems))

    def setModelData(self, editor, model, index):
        editorIndex=editor.currentIndex()
        text=editor.currentItem().text()
        model.setData(index, text)
        # print '\t\t\t ...setModelData() 1', text

    @Slot()
    def currentItemChanged(self):
        self.commitData.emit(self.sender())

class MyModel(QAbstractTableModel):
    def __init__(self, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.items=['Data_Item01','Data_Item02','Data_Item03']

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)
    def columnCount(self, parent=QModelIndex()):
        return 1

    def data(self, index, role):
        if not index.isValid(): return

        row=index.row()
        item=self.items[row]

        if row>len(self.items): return

        if role == Qt.DisplayRole:
            # print ' << >> MyModel.data() returning ...', item
            return item

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled

    def setData(self, index, text):
        self.items[index.row()]=text

if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = MyModel()
    tableView = QTableView()
    tableView.setModel(model)

    delegate = ComboDelegate()

    tableView.setItemDelegate(delegate)
    for i in range(0,tableView.model().rowCount()):
        tableView.setRowHeight(i,tableView.itemDelegate().height)
    for i in range(0,tableView.model().columnCount()):
        tableView.setColumnWidth(i,tableView.itemDelegate().width)

    tableView.show()
    sys.exit(app.exec_())