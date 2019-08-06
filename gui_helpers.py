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

    # Don't call QHeaderView::setSectionResizeMode() for every column. To automatically apply the passed stretch to all columns, 
    # just call that method once without iteratively passing an explicit column index: 
    # e.g., ui->tableView->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);. 
    # The below for loop thus reduces to a simplistic one-liner. 
    # See also thttps://stackoverflow.com/questions/18293403/columns-auto-resize-to-size-of-qtableview/34190094#34190094

    for i in range(1, len(labels)):
        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

    header.setDefaultAlignment(Qt.AlignLeft) 

    header_font = QFont()
    header_font.setWeight(QFont.DemiBold)
    header.setFont(header_font)