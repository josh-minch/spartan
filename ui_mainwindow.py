# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui',
# licensing of 'ui_mainwindow.ui' applies.
#
# Created: Tue Jul 30 19:42:56 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 693)
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
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(22, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/fridge.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_foods_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_foods_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_foods_btn.sizePolicy().hasHeightForWidth())
        self.add_foods_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.add_foods_btn.setFont(font)
        self.add_foods_btn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_foods_btn.setIcon(icon1)
        self.add_foods_btn.setObjectName("add_foods_btn")
        self.horizontalLayout.addWidget(self.add_foods_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
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
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.fridge_table.setFont(font)
        self.fridge_table.setAutoFillBackground(False)
        self.fridge_table.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"}\n"
"")
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
        self.verticalLayout.addWidget(self.fridge_table)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.remove_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_btn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.remove_btn.setFont(font)
        self.remove_btn.setObjectName("remove_btn")
        self.gridLayout_2.addWidget(self.remove_btn, 0, 0, 1, 1)
        self.optimize_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.optimize_btn.setFont(font)
        self.optimize_btn.setStyleSheet("")
        self.optimize_btn.setObjectName("optimize_btn")
        self.gridLayout_2.addWidget(self.optimize_btn, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.nutrition_layout = QtWidgets.QGridLayout()
        self.nutrition_layout.setObjectName("nutrition_layout")
        self.debug_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debug_btn.sizePolicy().hasHeightForWidth())
        self.debug_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.debug_btn.setFont(font)
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
        font.setPointSize(12)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.nutrition_layout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.nutrition_table = QDeselectableTableWidget(self.centralwidget)
        self.nutrition_table.setMinimumSize(QtCore.QSize(400, 0))
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
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.nutrition_table.setFont(font)
        self.nutrition_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nutrition_table.setAutoFillBackground(False)
        self.nutrition_table.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}")
        self.nutrition_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nutrition_table.setAlternatingRowColors(False)
        self.nutrition_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.nutrition_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.nutrition_table.setShowGrid(False)
        self.nutrition_table.setColumnCount(5)
        self.nutrition_table.setObjectName("nutrition_table")
        self.nutrition_table.setColumnCount(5)
        self.nutrition_table.setRowCount(0)
        self.nutrition_table.horizontalHeader().setVisible(True)
        self.nutrition_table.horizontalHeader().setCascadingSectionResizes(False)
        self.nutrition_table.horizontalHeader().setStretchLastSection(False)
        self.nutrition_table.verticalHeader().setVisible(False)
        self.nutrition_table.verticalHeader().setStretchLastSection(False)
        self.nutrition_layout.addWidget(self.nutrition_table, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.nutrition_layout)
        self.horizontalLayout_2.setStretch(0, 1)
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
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "My fridge", None, -1))
        self.add_foods_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Add foods", None, -1))
        self.remove_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Remove food", None, -1))
        self.optimize_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Optimize Diet", None, -1))
        self.optimize_btn.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F5", None, -1))
        self.debug_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Nutrition", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionSettings_2.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionSettings_3.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))

from qdeselectable_table_widget import QDeselectableTableWidget
