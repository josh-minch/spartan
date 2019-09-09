# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_optimumdietwindow.ui',
# licensing of 'ui_optimumdietwindow.ui' applies.
#
# Created: Sun Sep  8 15:24:55 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OptimumDietWindow(object):
    def setupUi(self, OptimumDietWindow):
        OptimumDietWindow.setObjectName("OptimumDietWindow")
        OptimumDietWindow.resize(800, 600)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/opt_diet.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.diet_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.diet_label.setFont(font)
        self.diet_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.diet_label.setObjectName("diet_label")
        self.horizontalLayout.addWidget(self.diet_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.optimum_diet_table = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.optimum_diet_table.setFont(font)
        self.optimum_diet_table.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"}\n"
"")
        self.optimum_diet_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.optimum_diet_table.setAlternatingRowColors(False)
        self.optimum_diet_table.setShowGrid(False)
        self.optimum_diet_table.setColumnCount(3)
        self.optimum_diet_table.setObjectName("optimum_diet_table")
        self.optimum_diet_table.setColumnCount(3)
        self.optimum_diet_table.setRowCount(0)
        self.optimum_diet_table.horizontalHeader().setVisible(False)
        self.optimum_diet_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.optimum_diet_table)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        OptimumDietWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OptimumDietWindow)
        QtCore.QMetaObject.connectSlotsByName(OptimumDietWindow)

    def retranslateUi(self, OptimumDietWindow):
        OptimumDietWindow.setWindowTitle(QtWidgets.QApplication.translate("OptimumDietWindow", "Spartan - Optimum diet", None, -1))
        self.diet_label.setText(QtWidgets.QApplication.translate("OptimumDietWindow", "Optimum diet is", None, -1))

