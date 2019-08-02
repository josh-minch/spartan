from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QHeaderView

def hide_view_cols(view, cols_to_hide):
    for col in cols_to_hide:
        view.setColumnHidden(col, True)

def set_header_weight(header, weight):
    header_font = QFont()
    header_font.setWeight(weight)
    header.setFont(header_font)

def set_v_header_height(view, size):
    v_header = view.verticalHeader()
    v_header.setSectionResizeMode(QHeaderView.Fixed)
    v_header.setDefaultSectionSize(size)

def setup_table_header(table, labels):
    header = table.horizontalHeader()
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    for i in range(1, len(labels)):
        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

    header.setDefaultAlignment(Qt.AlignLeft) 

    header_font = QFont()
    header_font.setWeight(QFont.DemiBold)
    header.setFont(header_font)