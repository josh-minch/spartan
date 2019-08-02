# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow_tab.ui',
# licensing of 'ui_mainwindow_tab.ui' applies.
#
# Created: Fri Aug  2 15:30:06 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 693)
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
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)
        self.optimize_btn = QtWidgets.QPushButton(self.centralwidget)
        self.optimize_btn.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.optimize_btn.setFont(font)
        self.optimize_btn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/diet_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.optimize_btn.setIcon(icon2)
        self.optimize_btn.setIconSize(QtCore.QSize(20, 20))
        self.optimize_btn.setObjectName("optimize_btn")
        self.gridLayout_2.addWidget(self.optimize_btn, 1, 5, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }")
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.add_foods_btn = QtWidgets.QPushButton(self.tab)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_foods_btn.setIcon(icon3)
        self.add_foods_btn.setObjectName("add_foods_btn")
        self.gridLayout.addWidget(self.add_foods_btn, 0, 0, 1, 1)
        self.remove_btn = QtWidgets.QPushButton(self.tab)
        self.remove_btn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.remove_btn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_btn.setIcon(icon4)
        self.remove_btn.setObjectName("remove_btn")
        self.gridLayout.addWidget(self.remove_btn, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMaximumSize(QtCore.QSize(25, 25))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/nutrition.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 4, 1, 1)
        self.fridge_view = QtWidgets.QTableView(self.tab)
        self.fridge_view.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}")
        self.fridge_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fridge_view.setShowGrid(False)
        self.fridge_view.setObjectName("fridge_view")
        self.gridLayout.addWidget(self.fridge_view, 1, 0, 1, 3)
        self.nutrition_view_1 = QtWidgets.QTableView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nutrition_view_1.sizePolicy().hasHeightForWidth())
        self.nutrition_view_1.setSizePolicy(sizePolicy)
        self.nutrition_view_1.setMinimumSize(QtCore.QSize(480, 0))
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
        self.nutrition_view_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.nutrition_view_1.setFont(font)
        self.nutrition_view_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nutrition_view_1.setAutoFillBackground(False)
        self.nutrition_view_1.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}")
        self.nutrition_view_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nutrition_view_1.setAlternatingRowColors(False)
        self.nutrition_view_1.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.nutrition_view_1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.nutrition_view_1.setShowGrid(False)
        self.nutrition_view_1.setObjectName("nutrition_view_1")
        self.gridLayout.addWidget(self.nutrition_view_1, 1, 3, 1, 2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/fridge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.add_foods_btn_2 = QtWidgets.QPushButton(self.tab_2)
        self.add_foods_btn_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_foods_btn_2.sizePolicy().hasHeightForWidth())
        self.add_foods_btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.add_foods_btn_2.setFont(font)
        self.add_foods_btn_2.setStyleSheet("")
        self.add_foods_btn_2.setIcon(icon3)
        self.add_foods_btn_2.setObjectName("add_foods_btn_2")
        self.gridLayout_3.addWidget(self.add_foods_btn_2, 0, 0, 1, 1)
        self.remove_btn_2 = QtWidgets.QPushButton(self.tab_2)
        self.remove_btn_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.remove_btn_2.setFont(font)
        self.remove_btn_2.setIcon(icon4)
        self.remove_btn_2.setObjectName("remove_btn_2")
        self.gridLayout_3.addWidget(self.remove_btn_2, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setMaximumSize(QtCore.QSize(25, 25))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/nutrition.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 4, 1, 1)
        self.constraints_view = QtWidgets.QTableView(self.tab_2)
        self.constraints_view.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}")
        self.constraints_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.constraints_view.setShowGrid(False)
        self.constraints_view.setObjectName("constraints_view")
        self.gridLayout_3.addWidget(self.constraints_view, 1, 0, 1, 3)
        self.nutrition_view_2 = QtWidgets.QTableView(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nutrition_view_2.sizePolicy().hasHeightForWidth())
        self.nutrition_view_2.setSizePolicy(sizePolicy)
        self.nutrition_view_2.setMinimumSize(QtCore.QSize(480, 0))
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
        self.nutrition_view_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.nutrition_view_2.setFont(font)
        self.nutrition_view_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nutrition_view_2.setAutoFillBackground(False)
        self.nutrition_view_2.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}")
        self.nutrition_view_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nutrition_view_2.setAlternatingRowColors(False)
        self.nutrition_view_2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.nutrition_view_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.nutrition_view_2.setShowGrid(False)
        self.nutrition_view_2.setObjectName("nutrition_view_2")
        self.gridLayout_3.addWidget(self.nutrition_view_2, 1, 3, 1, 2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/balance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon6, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 5)
        self.debug_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debug_btn.sizePolicy().hasHeightForWidth())
        self.debug_btn.setSizePolicy(sizePolicy)
        self.debug_btn.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.debug_btn.setFont(font)
        self.debug_btn.setObjectName("debug_btn")
        self.gridLayout_2.addWidget(self.debug_btn, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings_2 = QtWidgets.QAction(MainWindow)
        self.actionSettings_2.setObjectName("actionSettings_2")
        self.actionSettings_3 = QtWidgets.QAction(MainWindow)
        self.actionSettings_3.setObjectName("actionSettings_3")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Spartan", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.pushButton.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F9", None, -1))
        self.optimize_btn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<p style=\'white-space:pre\'>Generate optimum diet (F5)</p>", None, -1))
        self.optimize_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Generate diet", None, -1))
        self.optimize_btn.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F5", None, -1))
        self.add_foods_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Add food", None, -1))
        self.add_foods_btn.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+F", None, -1))
        self.remove_btn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<p style=\'white-space:pre\'>Remove selected food (delete)</p>", None, -1))
        self.remove_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Remove food", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Nutrition", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "My fridge", None, -1))
        self.add_foods_btn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Add food", None, -1))
        self.add_foods_btn_2.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+F", None, -1))
        self.remove_btn_2.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<p style=\'white-space:pre\'>Remove selected food (delete)</p>", None, -1))
        self.remove_btn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Remove food", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Nutrition", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Constraints", None, -1))
        self.debug_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.debug_btn.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionSettings_2.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionSettings_3.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))

