from PySide2.QtWidgets import QStyledItemDelegate, QStyle, QApplication, QStyleOptionProgressBar, QStyleOptionViewItem, QProgressBar
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPalette, QColor

import PySide2

from gui_constants import *

class ProgressBarDelegate (QStyledItemDelegate):

    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)

    # Only called when resizing col and row to contents
    #def sizeHint(self, option, index):
    #    return QSize(120, 2)

    def paint(self, painter, option, index):
        if index.column() == NUT_PERCENT_COL:

            progress_bar_option = QStyleOptionProgressBar()
            progress_bar_option.rect = option.rect
            progress_bar_option.minimum = 0
            progress_bar_option.maximum = 100
            progress_bar_option.textVisible = True

            progress = index.data(role=Qt.DisplayRole)

            p = QPalette()

            if progress is None:
                # A bug in the progress bar for the fusion style causes a thin vertical strip
                # of the progress bar chunk to be painted to the left of a progress bar with
                # less than 1% progess while drawn in a table view.
                # This strip is normally covered by the table's grid lines, but I have them disabled.
                # My workaround to display a completely empty progress bar without the strip
                # is to fill the progress bar and simply turn the color to white
                progress_bar_option.progress = 100
                progress_bar_option.text = "No data"
                p.setColor(QPalette.Highlight, QColor(Qt.white))
                p.setColor(QPalette.HighlightedText, Qt.darkGray)
                progress_bar_option.palette = p

            elif round(progress) == 0:
                progress_bar_option.progress = 100
                progress_bar_option.text = "0%"
                p.setColor(QPalette.Highlight, QColor(Qt.white))
                p.setColor(QPalette.HighlightedText, QColor(Qt.black))
                progress_bar_option.palette = p

            elif 0 < progress <= 100:
                progress_bar_option.progress = round(progress)
                progress_bar_option.text = str(round(progress)) + "%"

            elif 100 < progress:
                progress_bar_option.progress = 100
                progress_bar_option.text = str(round(progress)) + "%"

            #p.setColor(QPalette.Highlight, QColor(247, 202, 202))
            #progress_bar_option.palette = p

            QApplication.style().drawControl(QStyle.CE_ProgressBar, progress_bar_option, painter)

        else:
            QStyledItemDelegate.paint(self, painter, option, index)
