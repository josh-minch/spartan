from PySide2.QtWidgets import QStyledItemDelegate, QStyle, QApplication, QStyleOptionProgressBar
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPalette

import PySide2

from gui_constants import *

class ProgressBarDelegate (QStyledItemDelegate):

    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)

    # Only called when resizing col and row to contents
    def sizeHint(self, option, index):
        return QSize(120, 2)
    

    def paint(self, painter, option, index):
        if index.column() == NUT_PERCENT_COL:
            progress = index.data(role=Qt.DisplayRole)

            progress_bar_option = QStyleOptionProgressBar()
            progress_bar_option.rect = option.rect
            progress_bar_option.minimum = 0
            progress_bar_option.maximum = 100
            if progress is None:
                progress_bar_option.progress = 0
            elif progress <= 100:
                progress_bar_option.progress = progress
            else:
                progress_bar_option.progress = 100
            progress_bar_option.text = str(progress) + "%"
            progress_bar_option.textVisible = True

            # Change color
            #p = QPalette()
            #p.setColor(QPalette.Highlight, Qt.darkRed)
            #progress_bar_option.palette = p

            QApplication.style().drawControl(QStyle.CE_ProgressBar, progress_bar_option, painter)

        else:
            QStyledItemDelegate.paint(self, painter, option, index)