from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QHeaderView

def setup_table_header(table, labels):
    header = table.horizontalHeader()
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    for i in range(1, len(labels)):
        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

    header.setDefaultAlignment(Qt.AlignLeft) 

    header_font = QFont()
    header_font.setWeight(QFont.DemiBold)
    header.setFont(header_font)