# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_mainwindow.ui',
# licensing of 'ui/ui_mainwindow.ui' applies.
#
# Created: Mon Nov  4 13:09:36 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 705)
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
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(6, 0, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_foods_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_foods_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_foods_btn.sizePolicy().hasHeightForWidth())
        self.add_foods_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.add_foods_btn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_foods_btn.setIcon(icon1)
        self.add_foods_btn.setObjectName("add_foods_btn")
        self.horizontalLayout.addWidget(self.add_foods_btn)
        self.remove_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_btn.sizePolicy().hasHeightForWidth())
        self.remove_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.remove_btn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_btn.setIcon(icon2)
        self.remove_btn.setObjectName("remove_btn")
        self.horizontalLayout.addWidget(self.remove_btn)
        self.optimize_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optimize_btn.sizePolicy().hasHeightForWidth())
        self.optimize_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.optimize_btn.setFont(font)
        self.optimize_btn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/chevron-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.optimize_btn.setIcon(icon3)
        self.optimize_btn.setObjectName("optimize_btn")
        self.horizontalLayout.addWidget(self.optimize_btn)
        self.fridge_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fridge_line_edit.sizePolicy().hasHeightForWidth())
        self.fridge_line_edit.setSizePolicy(sizePolicy)
        self.fridge_line_edit.setMinimumSize(QtCore.QSize(75, 0))
        self.fridge_line_edit.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        self.fridge_line_edit.setFont(font)
        self.fridge_line_edit.setText("")
        self.fridge_line_edit.setObjectName("fridge_line_edit")
        self.horizontalLayout.addWidget(self.fridge_line_edit)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fridge_view = QtWidgets.QTableView(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.fridge_view.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fridge_view.setFont(font)
        self.fridge_view.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fridge_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.fridge_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fridge_view.setAlternatingRowColors(True)
        self.fridge_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fridge_view.setShowGrid(False)
        self.fridge_view.setGridStyle(QtCore.Qt.DashLine)
        self.fridge_view.setObjectName("fridge_view")
        self.fridge_view.horizontalHeader().setVisible(False)
        self.fridge_view.horizontalHeader().setHighlightSections(False)
        self.fridge_view.horizontalHeader().setStretchLastSection(True)
        self.fridge_view.verticalHeader().setVisible(False)
        self.fridge_view.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout.addWidget(self.fridge_view)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(13, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.tab_3.setFont(font)
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setContentsMargins(0, -1, -1, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.nut_quant_view = ComboTableView(self.tab_3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.nut_quant_view.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nut_quant_view.setFont(font)
        self.nut_quant_view.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nut_quant_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QTableView {\n"
"    \n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.nut_quant_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nut_quant_view.setTabKeyNavigation(False)
        self.nut_quant_view.setAlternatingRowColors(True)
        self.nut_quant_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.nut_quant_view.setShowGrid(False)
        self.nut_quant_view.setGridStyle(QtCore.Qt.DashLine)
        self.nut_quant_view.setObjectName("nut_quant_view")
        self.nut_quant_view.horizontalHeader().setVisible(False)
        self.nut_quant_view.horizontalHeader().setHighlightSections(False)
        self.nut_quant_view.horizontalHeader().setStretchLastSection(True)
        self.nut_quant_view.verticalHeader().setVisible(False)
        self.nut_quant_view.verticalHeader().setDefaultSectionSize(23)
        self.gridLayout_4.addWidget(self.nut_quant_view, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.prices_view = ComboTableView(self.tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.prices_view.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.prices_view.setFont(font)
        self.prices_view.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.prices_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.prices_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.prices_view.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.prices_view.setTabKeyNavigation(False)
        self.prices_view.setAlternatingRowColors(True)
        self.prices_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.prices_view.setShowGrid(False)
        self.prices_view.setGridStyle(QtCore.Qt.DashLine)
        self.prices_view.setObjectName("prices_view")
        self.prices_view.horizontalHeader().setVisible(False)
        self.prices_view.horizontalHeader().setHighlightSections(False)
        self.prices_view.horizontalHeader().setStretchLastSection(True)
        self.prices_view.verticalHeader().setVisible(False)
        self.prices_view.verticalHeader().setDefaultSectionSize(23)
        self.verticalLayout_5.addWidget(self.prices_view)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.constraints_view = ComboTableView(self.tab_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.constraints_view.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.constraints_view.setFont(font)
        self.constraints_view.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.constraints_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.constraints_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.constraints_view.setFrameShadow(QtWidgets.QFrame.Plain)
        self.constraints_view.setTabKeyNavigation(False)
        self.constraints_view.setAlternatingRowColors(True)
        self.constraints_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.constraints_view.setShowGrid(False)
        self.constraints_view.setGridStyle(QtCore.Qt.DashLine)
        self.constraints_view.setObjectName("constraints_view")
        self.constraints_view.horizontalHeader().setVisible(False)
        self.constraints_view.horizontalHeader().setHighlightSections(False)
        self.constraints_view.verticalHeader().setVisible(False)
        self.constraints_view.verticalHeader().setDefaultSectionSize(23)
        self.verticalLayout_4.addWidget(self.constraints_view)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.pref_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pref_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pref_btn.setFont(font)
        self.pref_btn.setCursor(QtCore.Qt.PointingHandCursor)
        self.pref_btn.setStyleSheet("QPushButton {\n"
"    border: white;\n"
"}\n"
"")
        self.pref_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/index.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pref_btn.setIcon(icon4)
        self.pref_btn.setIconSize(QtCore.QSize(30, 30))
        self.pref_btn.setObjectName("pref_btn")
        self.horizontalLayout_5.addWidget(self.pref_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.macros_view = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.macros_view.sizePolicy().hasHeightForWidth())
        self.macros_view.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.macros_view.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.macros_view.setFont(font)
        self.macros_view.setFocusPolicy(QtCore.Qt.NoFocus)
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
        self.macros_view.setFrameShadow(QtWidgets.QFrame.Plain)
        self.macros_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.macros_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.macros_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.macros_view.setAlternatingRowColors(False)
        self.macros_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.macros_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.macros_view.setShowGrid(False)
        self.macros_view.setObjectName("macros_view")
        self.macros_view.horizontalHeader().setVisible(True)
        self.macros_view.horizontalHeader().setHighlightSections(False)
        self.macros_view.horizontalHeader().setMinimumSectionSize(0)
        self.macros_view.horizontalHeader().setStretchLastSection(False)
        self.macros_view.verticalHeader().setVisible(False)
        self.macros_view.verticalHeader().setDefaultSectionSize(25)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.macros_view)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.vits_view = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vits_view.sizePolicy().hasHeightForWidth())
        self.vits_view.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.vits_view.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vits_view.setFont(font)
        self.vits_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.vits_view.setAutoFillBackground(False)
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
        self.vits_view.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vits_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vits_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vits_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.vits_view.setAlternatingRowColors(False)
        self.vits_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.vits_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.vits_view.setShowGrid(False)
        self.vits_view.setObjectName("vits_view")
        self.vits_view.horizontalHeader().setVisible(True)
        self.vits_view.horizontalHeader().setHighlightSections(False)
        self.vits_view.horizontalHeader().setMinimumSectionSize(0)
        self.vits_view.horizontalHeader().setStretchLastSection(False)
        self.vits_view.verticalHeader().setVisible(False)
        self.vits_view.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout_6.addWidget(self.vits_view)
        self.minerals_view = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minerals_view.sizePolicy().hasHeightForWidth())
        self.minerals_view.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 236, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.minerals_view.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.minerals_view.setFont(font)
        self.minerals_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.minerals_view.setAutoFillBackground(False)
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
        self.minerals_view.setFrameShadow(QtWidgets.QFrame.Plain)
        self.minerals_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minerals_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minerals_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.minerals_view.setAlternatingRowColors(False)
        self.minerals_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.minerals_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.minerals_view.setShowGrid(False)
        self.minerals_view.setObjectName("minerals_view")
        self.minerals_view.horizontalHeader().setVisible(True)
        self.minerals_view.horizontalHeader().setHighlightSections(False)
        self.minerals_view.horizontalHeader().setMinimumSectionSize(0)
        self.minerals_view.horizontalHeader().setStretchLastSection(False)
        self.minerals_view.verticalHeader().setVisible(False)
        self.minerals_view.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout_6.addWidget(self.minerals_view)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings_2 = QtWidgets.QAction(MainWindow)
        self.actionSettings_2.setObjectName("actionSettings_2")
        self.actionSettings_3 = QtWidgets.QAction(MainWindow)
        self.actionSettings_3.setObjectName("actionSettings_3")
        self.actione = QtWidgets.QAction(MainWindow)
        self.actione.setObjectName("actione")
        self.actionex = QtWidgets.QAction(MainWindow)
        self.actionex.setObjectName("actionex")
        self.actionaa = QtWidgets.QAction(MainWindow)
        self.actionaa.setObjectName("actionaa")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Spartan", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "My fridge", None, -1))
        self.add_foods_btn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Add food (Ctrl+F)</p></body></html>", None, -1))
        self.add_foods_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Add food", None, -1))
        self.add_foods_btn.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+F", None, -1))
        self.remove_btn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\';\">Remove selected food (Ctrl+D)</span></pre></body></html>", None, -1))
        self.remove_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Remove", None, -1))
        self.remove_btn.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+D", None, -1))
        self.optimize_btn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<p style=\'white-space:pre\'>Generate optimum diet (F5)</p>", None, -1))
        self.optimize_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Make diet", None, -1))
        self.optimize_btn.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F5", None, -1))
        self.fridge_line_edit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "🔍 Search fridge (100 items)", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "Nutrition amounts", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Prices", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Constraints", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Nutrition", None, -1))
        self.pref_btn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Settings (Ctrl+S)</p></body></html>", None, -1))
        self.pref_btn.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionSettings_2.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actionSettings_3.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.actione.setText(QtWidgets.QApplication.translate("MainWindow", "e", None, -1))
        self.actionex.setText(QtWidgets.QApplication.translate("MainWindow", "ex", None, -1))
        self.actionaa.setText(QtWidgets.QApplication.translate("MainWindow", "aa[\\", None, -1))

from view.combo_table_view import ComboTableView
import icon_rc
