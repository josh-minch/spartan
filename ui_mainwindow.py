# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui',
# licensing of 'ui_mainwindow.ui' applies.
#
# Created: Tue Jun 25 20:08:48 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DatabaseLayout = QtWidgets.QVBoxLayout()
        self.DatabaseLayout.setObjectName("DatabaseLayout")
        self.debug_btn = QtWidgets.QPushButton(self.centralwidget)
        self.debug_btn.setObjectName("debug_btn")
        self.DatabaseLayout.addWidget(self.debug_btn)
        self.DatabaseLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DatabaseLabel.sizePolicy().hasHeightForWidth())
        self.DatabaseLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setWeight(50)
        font.setBold(False)
        self.DatabaseLabel.setFont(font)
        self.DatabaseLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DatabaseLabel.setObjectName("DatabaseLabel")
        self.DatabaseLayout.addWidget(self.DatabaseLabel)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.add_custom_food_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_custom_food_btn.setObjectName("add_custom_food_btn")
        self.gridLayout.addWidget(self.add_custom_food_btn, 4, 1, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setObjectName("search_btn")
        self.gridLayout.addWidget(self.search_btn, 0, 3, 1, 1)
        self.search_list = QtWidgets.QListWidget(self.centralwidget)
        self.search_list.setObjectName("search_list")
        self.gridLayout.addWidget(self.search_list, 1, 1, 1, 4)
        self.add_to_fridge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_to_fridge_btn.setObjectName("add_to_fridge_btn")
        self.gridLayout.addWidget(self.add_to_fridge_btn, 4, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        self.search_box = QtWidgets.QLineEdit(self.centralwidget)
        self.search_box.setObjectName("search_box")
        self.gridLayout.addWidget(self.search_box, 0, 1, 1, 2)
        self.DatabaseLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.DatabaseLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FridgeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.FridgeLabel.setFont(font)
        self.FridgeLabel.setObjectName("FridgeLabel")
        self.verticalLayout.addWidget(self.FridgeLabel)
        self.fridge_table = QtWidgets.QTableWidget(self.centralwidget)
        self.fridge_table.setShowGrid(False)
        self.fridge_table.setGridStyle(QtCore.Qt.SolidLine)
        self.fridge_table.setRowCount(0)
        self.fridge_table.setColumnCount(5)
        self.fridge_table.setObjectName("fridge_table")
        self.fridge_table.setColumnCount(5)
        self.fridge_table.setRowCount(0)
        self.fridge_table.horizontalHeader().setVisible(True)
        self.fridge_table.horizontalHeader().setCascadingSectionResizes(False)
        self.fridge_table.horizontalHeader().setSortIndicatorShown(True)
        self.fridge_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.fridge_table)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.remove_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_btn.setObjectName("remove_btn")
        self.gridLayout_2.addWidget(self.remove_btn, 0, 0, 1, 1)
        self.optimize_btn = QtWidgets.QPushButton(self.centralwidget)
        self.optimize_btn.setObjectName("optimize_btn")
        self.gridLayout_2.addWidget(self.optimize_btn, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.NutriitonLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.NutriitonLabel.setFont(font)
        self.NutriitonLabel.setObjectName("NutriitonLabel")
        self.verticalLayout_2.addWidget(self.NutriitonLabel)
        self.nutrition_table = QtWidgets.QTableView(self.centralwidget)
        self.nutrition_table.setObjectName("nutrition_table")
        self.verticalLayout_2.addWidget(self.nutrition_table)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Frugal Nutrition", None, -1))
        self.debug_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Debug Search List", None, -1))
        self.DatabaseLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Food Database", None, -1))
        self.add_custom_food_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Add custom food", None, -1))
        self.search_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Search", None, -1))
        self.add_to_fridge_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Add to Fridge", None, -1))
        self.FridgeLabel.setText(QtWidgets.QApplication.translate("MainWindow", "My Fridge", None, -1))
        self.remove_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Remove food", None, -1))
        self.optimize_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Optimize Diet", None, -1))
        self.NutriitonLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Nutrition", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))

