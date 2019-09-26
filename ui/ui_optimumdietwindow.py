# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_optimumdietwindow.ui',
# licensing of 'ui/ui_optimumdietwindow.ui' applies.
#
# Created: Wed Sep 25 20:26:48 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OptimumDietWindow(object):
    def setupUi(self, OptimumDietWindow):
        OptimumDietWindow.setObjectName("OptimumDietWindow")
        OptimumDietWindow.resize(1142, 600)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OptimumDietWindow.setWindowIcon(icon)
        OptimumDietWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(OptimumDietWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/opt_diet.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.diet_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.diet_label.setFont(font)
        self.diet_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.diet_label.setObjectName("diet_label")
        self.gridLayout.addWidget(self.diet_label, 0, 1, 1, 1)
        self.diet_view = QtWidgets.QTableView(self.centralwidget)
        self.diet_view.setShowGrid(False)
        self.diet_view.setObjectName("diet_view")
        self.diet_view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.diet_view, 1, 0, 1, 2)
        self.macros_view = QtWidgets.QTableView(self.centralwidget)
        self.macros_view.setShowGrid(False)
        self.macros_view.setObjectName("macros_view")
        self.macros_view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.macros_view, 1, 2, 1, 1)
        self.vits_view = QtWidgets.QTableView(self.centralwidget)
        self.vits_view.setShowGrid(False)
        self.vits_view.setObjectName("vits_view")
        self.vits_view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.vits_view, 1, 3, 1, 1)
        self.minerals_view = QtWidgets.QTableView(self.centralwidget)
        self.minerals_view.setShowGrid(False)
        self.minerals_view.setObjectName("minerals_view")
        self.minerals_view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.minerals_view, 2, 3, 1, 1)
        OptimumDietWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OptimumDietWindow)
        QtCore.QMetaObject.connectSlotsByName(OptimumDietWindow)

    def retranslateUi(self, OptimumDietWindow):
        OptimumDietWindow.setWindowTitle(QtWidgets.QApplication.translate("OptimumDietWindow", "Spartan - Optimum diet", None, -1))
        self.diet_label.setText(QtWidgets.QApplication.translate("OptimumDietWindow", "Optimum diet is", None, -1))

