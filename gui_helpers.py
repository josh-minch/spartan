from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QHeaderView

import gui_constants

def enumerate_cols(attrs):
    col_to_attr, attr_to_col = {}, {}
    for i, col_attr in enumerate(attrs):
        col_to_attr[i] = col_attr
        attr_to_col[col_attr] = i
    return col_to_attr, attr_to_col

def hide_view_cols(view, cols_to_hide):
    for col in cols_to_hide:
        view.setColumnHidden(col, True)

# by default, Qt doesn't change a table's header to reflect that of its body
def fix_header_font(table_view, font_size, font_weight):
    font = QFont(gui_constants.system_font_family(), font_size, font_weight)
    table_view.horizontalHeader().setFont(font)

def vertical_resize_table_view_to_contents(table_view):
    height = 0

    for i in range(table_view.verticalHeader().count()):
        height += table_view.verticalHeader().sectionSize(i)
    '''
    if table_view.horizontalScrollBar().isHidden() == False:
        height += table_view.horizontalScrollBar().height()
    '''
    if table_view.horizontalHeader().isHidden() == False:
        height += table_view.horizontalHeader().height()

    table_view.setMinimumHeight(height + 3)

def set_column_widths(view, cols, col_widths):
    for col, width in zip(cols, col_widths):
        view.setColumnWidth(col, width)

def set_header_font(table_view, size, weight):
    font = QFont(gui_constants.system_font_family(),
                 size,
                 weight)
    table_view.horizontalHeader().setFont(font)

def set_view_header_weights(view, weight):
    header = view.horizontalHeader()
    set_header_weight(header, weight)

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
