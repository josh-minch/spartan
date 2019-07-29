# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui',
# licensing of 'ui_mainwindow.ui' applies.
#
# Created: Sun Jul 28 22:17:55 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(917, 693)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setItalic(False)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.search_layout = QtWidgets.QVBoxLayout()
        self.search_layout.setObjectName("search_layout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.search_box = QtWidgets.QLineEdit(self.centralwidget)
        self.search_box.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_box.setFont(font)
        self.search_box.setObjectName("search_box")
        self.horizontalLayout_4.addWidget(self.search_box)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setMaximumSize(QtCore.QSize(79, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_btn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_4.addWidget(self.search_btn)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.search_layout.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.search_layout.addItem(spacerItem1)
        self.search_list = QDeselectableListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_list.setFont(font)
        self.search_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_list.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.search_list.setAlternatingRowColors(False)
        self.search_list.setWordWrap(True)
        self.search_list.setObjectName("search_list")
        self.search_layout.addWidget(self.search_list)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_custom_food_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_custom_food_btn.setEnabled(True)
        self.add_custom_food_btn.setObjectName("add_custom_food_btn")
        self.horizontalLayout_2.addWidget(self.add_custom_food_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.add_to_fridge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_to_fridge_btn.setEnabled(False)
        self.add_to_fridge_btn.setObjectName("add_to_fridge_btn")
        self.horizontalLayout_2.addWidget(self.add_to_fridge_btn)
        self.search_layout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.search_layout)
        self.fridge_layout = QtWidgets.QVBoxLayout()
        self.fridge_layout.setObjectName("fridge_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(22, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/fridge.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.fridge_layout.addLayout(self.horizontalLayout)
        self.fridge_table = QDeselectableTableWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.fridge_table.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fridge_table.setFont(font)
        self.fridge_table.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QTableWidget::item:focus { \n"
"}")
        self.fridge_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fridge_table.setLineWidth(0)
        self.fridge_table.setAlternatingRowColors(True)
        self.fridge_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fridge_table.setShowGrid(False)
        self.fridge_table.setGridStyle(QtCore.Qt.SolidLine)
        self.fridge_table.setRowCount(0)
        self.fridge_table.setColumnCount(5)
        self.fridge_table.setObjectName("fridge_table")
        self.fridge_table.setColumnCount(5)
        self.fridge_table.setRowCount(0)
        self.fridge_table.horizontalHeader().setVisible(True)
        self.fridge_table.horizontalHeader().setCascadingSectionResizes(False)
        self.fridge_table.horizontalHeader().setHighlightSections(False)
        self.fridge_table.horizontalHeader().setSortIndicatorShown(True)
        self.fridge_table.verticalHeader().setVisible(False)
        self.fridge_layout.addWidget(self.fridge_table)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.remove_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_btn.setEnabled(False)
        self.remove_btn.setObjectName("remove_btn")
        self.gridLayout_2.addWidget(self.remove_btn, 0, 0, 1, 1)
        self.optimize_btn = QtWidgets.QPushButton(self.centralwidget)
        self.optimize_btn.setStyleSheet("")
        self.optimize_btn.setObjectName("optimize_btn")
        self.gridLayout_2.addWidget(self.optimize_btn, 0, 2, 1, 1)
        self.fridge_layout.addLayout(self.gridLayout_2)
        self.horizontalLayout_5.addLayout(self.fridge_layout)
        self.nutrition_layout = QtWidgets.QGridLayout()
        self.nutrition_layout.setObjectName("nutrition_layout")
        self.debug_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debug_btn.sizePolicy().hasHeightForWidth())
        self.debug_btn.setSizePolicy(sizePolicy)
        self.debug_btn.setObjectName("debug_btn")
        self.nutrition_layout.addWidget(self.debug_btn, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(30, 30))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("images/nutrition.png"))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.nutrition_layout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.nutrition_table = QDeselectableTableWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.nutrition_table.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nutrition_table.setFont(font)
        self.nutrition_table.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}")
        self.nutrition_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nutrition_table.setAlternatingRowColors(False)
        self.nutrition_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.nutrition_table.setShowGrid(False)
        self.nutrition_table.setColumnCount(5)
        self.nutrition_table.setObjectName("nutrition_table")
        self.nutrition_table.setColumnCount(5)
        self.nutrition_table.setRowCount(0)
        self.nutrition_table.horizontalHeader().setCascadingSectionResizes(False)
        self.nutrition_table.horizontalHeader().setStretchLastSection(False)
        self.nutrition_table.verticalHeader().setVisible(False)
        self.nutrition_table.verticalHeader().setStretchLastSection(False)
        self.nutrition_layout.addWidget(self.nutrition_table, 1, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.nutrition_layout)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings_2 = QtWidgets.QAction(MainWindow)
        self.actionSettings_2.setObjectName("actionSettings_2")
        self.actionSettings_3 = QtWidgets.QAction(MainWindow)
        self.actionSettings_3.setObjectName("actionSettings_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Spartan", None, -1))
        self.search_box.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Search food database", None, -1))
        self.search_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Search", None, -1))
        self.add_custom_food_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Add custom food", None, -1))
        self.add_to_fridge_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Add to Fridge", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "My fridge", None, -1))
        self.remove_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Remove food", None, -1))
        self.optimize_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Optimize Diet", None, -1))
        self.debug_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Nutrition", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionSettings_2.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionSettings_3.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))

from qdeselectable_list_widget import QDeselectableListWidget
from qdeselectable_table_widget import QDeselectableTableWidget
