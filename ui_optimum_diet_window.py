# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_optimum_diet_window.ui',
# licensing of 'ui_optimum_diet_window.ui' applies.
#
# Created: Fri Jul 26 15:57:52 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OptimumDietWindow(object):
    def setupUi(self, OptimumDietWindow):
        OptimumDietWindow.setObjectName("OptimumDietWindow")
        OptimumDietWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OptimumDietWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(OptimumDietWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.diet_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.diet_label.setFont(font)
        self.diet_label.setObjectName("diet_label")
        self.verticalLayout.addWidget(self.diet_label)
        self.optimum_diet_table = QtWidgets.QTableWidget(self.centralwidget)
        self.optimum_diet_table.setAlternatingRowColors(True)
        self.optimum_diet_table.setColumnCount(3)
        self.optimum_diet_table.setObjectName("optimum_diet_table")
        self.optimum_diet_table.setColumnCount(3)
        self.optimum_diet_table.setRowCount(0)
        self.optimum_diet_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.optimum_diet_table)
        self.optimum_diet_totals = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optimum_diet_totals.sizePolicy().hasHeightForWidth())
        self.optimum_diet_totals.setSizePolicy(sizePolicy)
        self.optimum_diet_totals.setMinimumSize(QtCore.QSize(0, 1))
        self.optimum_diet_totals.setMaximumSize(QtCore.QSize(16777215, 30))
        self.optimum_diet_totals.setRowCount(1)
        self.optimum_diet_totals.setColumnCount(3)
        self.optimum_diet_totals.setObjectName("optimum_diet_totals")
        self.optimum_diet_totals.setColumnCount(3)
        self.optimum_diet_totals.setRowCount(1)
        self.optimum_diet_totals.horizontalHeader().setVisible(False)
        self.optimum_diet_totals.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.optimum_diet_totals)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.optimum_nutrition_table = QtWidgets.QTableWidget(self.centralwidget)
        self.optimum_nutrition_table.setObjectName("optimum_nutrition_table")
        self.optimum_nutrition_table.setColumnCount(0)
        self.optimum_nutrition_table.setRowCount(0)
        self.verticalLayout_2.addWidget(self.optimum_nutrition_table)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        OptimumDietWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OptimumDietWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        OptimumDietWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OptimumDietWindow)
        self.statusbar.setObjectName("statusbar")
        OptimumDietWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OptimumDietWindow)
        QtCore.QMetaObject.connectSlotsByName(OptimumDietWindow)

    def retranslateUi(self, OptimumDietWindow):
        OptimumDietWindow.setWindowTitle(QtWidgets.QApplication.translate("OptimumDietWindow", "Optimum Diet", None, -1))
        self.diet_label.setText(QtWidgets.QApplication.translate("OptimumDietWindow", "Optimum diet is ", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("OptimumDietWindow", "Nutrition", None, -1))

