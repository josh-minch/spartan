# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_optimumdietwindow.ui',
# licensing of 'ui/ui_optimumdietwindow.ui' applies.
#
# Created: Sat Sep 28 14:28:15 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OptimumDietWindow(object):
    def setupUi(self, OptimumDietWindow):
        OptimumDietWindow.setObjectName("OptimumDietWindow")
        OptimumDietWindow.resize(1287, 600)
        self.centralwidget = QtWidgets.QWidget(OptimumDietWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.diet_label = QtWidgets.QLabel(self.centralwidget)
        self.diet_label.setObjectName("diet_label")
        self.gridLayout.addWidget(self.diet_label, 0, 0, 1, 1)
        self.diet_view = QtWidgets.QTableView(self.centralwidget)
        self.diet_view.setObjectName("diet_view")
        self.gridLayout.addWidget(self.diet_view, 1, 0, 1, 1)
        self.macros_view = QtWidgets.QTableView(self.centralwidget)
        self.macros_view.setObjectName("macros_view")
        self.gridLayout.addWidget(self.macros_view, 1, 1, 1, 1)
        self.vits_view = QtWidgets.QTableView(self.centralwidget)
        self.vits_view.setObjectName("vits_view")
        self.gridLayout.addWidget(self.vits_view, 1, 2, 1, 1)
        self.minerals_view = QtWidgets.QTableView(self.centralwidget)
        self.minerals_view.setObjectName("minerals_view")
        self.gridLayout.addWidget(self.minerals_view, 2, 2, 1, 1)
        OptimumDietWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OptimumDietWindow)
        QtCore.QMetaObject.connectSlotsByName(OptimumDietWindow)

    def retranslateUi(self, OptimumDietWindow):
        OptimumDietWindow.setWindowTitle(QtWidgets.QApplication.translate("OptimumDietWindow", "MainWindow", None, -1))
        self.diet_label.setText(QtWidgets.QApplication.translate("OptimumDietWindow", "Optimum diet", None, -1))

