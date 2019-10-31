# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_optimumdietwindow.ui',
# licensing of 'ui/ui_optimumdietwindow.ui' applies.
#
# Created: Wed Oct 30 22:38:10 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OptimumDietWindow(object):
    def setupUi(self, OptimumDietWindow):
        OptimumDietWindow.setObjectName("OptimumDietWindow")
        OptimumDietWindow.resize(1090, 600)
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
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        OptimumDietWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OptimumDietWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(OptimumDietWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(12, -1, -1, -1)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(18)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.diet_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diet_label.sizePolicy().hasHeightForWidth())
        self.diet_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.diet_label.setFont(font)
        self.diet_label.setWordWrap(True)
        self.diet_label.setObjectName("diet_label")
        self.verticalLayout.addWidget(self.diet_label)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(528, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.diet_view = QtWidgets.QTableView(self.centralwidget)
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
        self.diet_view.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.diet_view.setFont(font)
        self.diet_view.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.diet_view.setMouseTracking(True)
        self.diet_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"    outline: none;\n"
"}\n"
"")
        self.diet_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.diet_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.diet_view.setShowGrid(False)
        self.diet_view.setObjectName("diet_view")
        self.diet_view.horizontalHeader().setHighlightSections(False)
        self.diet_view.verticalHeader().setVisible(False)
        self.diet_view.verticalHeader().setDefaultSectionSize(40)
        self.diet_view.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.diet_view, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.macro_view = QtWidgets.QTableView(self.centralwidget)
        self.macro_view.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.macro_view.setFont(font)
        self.macro_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.macro_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.macro_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.macro_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.macro_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.macro_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.macro_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.macro_view.setShowGrid(False)
        self.macro_view.setObjectName("macro_view")
        self.macro_view.verticalHeader().setVisible(False)
        self.macro_view.verticalHeader().setDefaultSectionSize(28)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.macro_view)
        self.vit_view = QtWidgets.QTableView(self.centralwidget)
        self.vit_view.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vit_view.setFont(font)
        self.vit_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.vit_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.vit_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.vit_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vit_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vit_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.vit_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.vit_view.setShowGrid(False)
        self.vit_view.setObjectName("vit_view")
        self.vit_view.verticalHeader().setVisible(False)
        self.vit_view.verticalHeader().setDefaultSectionSize(28)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.vit_view)
        self.mineral_view = QtWidgets.QTableView(self.centralwidget)
        self.mineral_view.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mineral_view.setFont(font)
        self.mineral_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mineral_view.setStyleSheet("QHeaderView::section{\n"
"    border: 0px;\n"
"    background-color: white;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.mineral_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mineral_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mineral_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mineral_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.mineral_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.mineral_view.setShowGrid(False)
        self.mineral_view.setObjectName("mineral_view")
        self.mineral_view.verticalHeader().setVisible(False)
        self.mineral_view.verticalHeader().setDefaultSectionSize(28)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mineral_view)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)
        OptimumDietWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OptimumDietWindow)
        QtCore.QMetaObject.connectSlotsByName(OptimumDietWindow)

    def retranslateUi(self, OptimumDietWindow):
        OptimumDietWindow.setWindowTitle(QtWidgets.QApplication.translate("OptimumDietWindow", "Spartan - Generated Diet", None, -1))
        self.title_label.setText(QtWidgets.QApplication.translate("OptimumDietWindow", "Diet", None, -1))
        self.diet_label.setText(QtWidgets.QApplication.translate("OptimumDietWindow", "Optimum diet", None, -1))

import images_rc
