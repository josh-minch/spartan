# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_optimumdietwindow.ui',
# licensing of 'ui/ui_optimumdietwindow.ui' applies.
#
# Created: Fri Oct 25 13:26:17 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OptimumDietWindow(object):
    def setupUi(self, OptimumDietWindow):
        OptimumDietWindow.setObjectName("OptimumDietWindow")
        OptimumDietWindow.resize(1287, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        OptimumDietWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(OptimumDietWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.diet_view = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.diet_view.setFont(font)
        self.diet_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.diet_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.diet_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.diet_view.setShowGrid(False)
        self.diet_view.setObjectName("diet_view")
        self.diet_view.horizontalHeader().setHighlightSections(False)
        self.diet_view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.diet_view, 2, 0, 2, 1)
        self.vits_view = QtWidgets.QTableView(self.centralwidget)
        self.vits_view.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vits_view.setFont(font)
        self.vits_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.vits_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.vits_view.setShowGrid(False)
        self.vits_view.setObjectName("vits_view")
        self.vits_view.verticalHeader().setVisible(False)
        self.vits_view.verticalHeader().setDefaultSectionSize(25)
        self.gridLayout.addWidget(self.vits_view, 2, 2, 1, 1)
        self.macros_view = QtWidgets.QTableView(self.centralwidget)
        self.macros_view.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.macros_view.setFont(font)
        self.macros_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.macros_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.macros_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.macros_view.setShowGrid(False)
        self.macros_view.setObjectName("macros_view")
        self.macros_view.verticalHeader().setVisible(False)
        self.macros_view.verticalHeader().setDefaultSectionSize(25)
        self.gridLayout.addWidget(self.macros_view, 2, 1, 1, 1)
        self.diet_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.diet_label.setFont(font)
        self.diet_label.setObjectName("diet_label")
        self.gridLayout.addWidget(self.diet_label, 1, 0, 1, 1)
        self.minerals_view = QtWidgets.QTableView(self.centralwidget)
        self.minerals_view.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.minerals_view.setFont(font)
        self.minerals_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.minerals_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minerals_view.setShowGrid(False)
        self.minerals_view.setObjectName("minerals_view")
        self.minerals_view.verticalHeader().setVisible(False)
        self.minerals_view.verticalHeader().setDefaultSectionSize(25)
        self.gridLayout.addWidget(self.minerals_view, 3, 2, 1, 1)
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(18)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 1)
        OptimumDietWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OptimumDietWindow)
        QtCore.QMetaObject.connectSlotsByName(OptimumDietWindow)

    def retranslateUi(self, OptimumDietWindow):
        OptimumDietWindow.setWindowTitle(QtWidgets.QApplication.translate("OptimumDietWindow", "MainWindow", None, -1))
        self.diet_label.setText(QtWidgets.QApplication.translate("OptimumDietWindow", "Optimum diet", None, -1))
        self.title_label.setText(QtWidgets.QApplication.translate("OptimumDietWindow", "Diet", None, -1))

