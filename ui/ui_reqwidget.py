# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_reqwidget.ui',
# licensing of 'ui/ui_reqwidget.ui' applies.
#
# Created: Sat Nov  2 19:15:29 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ReqWidget(object):
    def setupUi(self, ReqWidget):
        ReqWidget.setObjectName("ReqWidget")
        ReqWidget.resize(911, 749)
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
        ReqWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        ReqWidget.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReqWidget.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(ReqWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(ReqWidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 893, 731))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(20, 20, -1, -1)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setMargin(0)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mineral_view = ReqView(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.mineral_view.setFont(font)
        self.mineral_view.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.mineral_view.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.mineral_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mineral_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mineral_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mineral_view.setAlternatingRowColors(True)
        self.mineral_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.mineral_view.setShowGrid(False)
        self.mineral_view.setObjectName("mineral_view")
        self.mineral_view.horizontalHeader().setHighlightSections(False)
        self.mineral_view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.mineral_view, 3, 0, 1, 1)
        self.macro_view = ReqView(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.macro_view.setFont(font)
        self.macro_view.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.macro_view.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.macro_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.macro_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.macro_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.macro_view.setAlternatingRowColors(True)
        self.macro_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.macro_view.setShowGrid(False)
        self.macro_view.setObjectName("macro_view")
        self.macro_view.horizontalHeader().setHighlightSections(False)
        self.macro_view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.macro_view, 0, 0, 2, 1)
        self.vit_view = ReqView(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.vit_view.setFont(font)
        self.vit_view.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.vit_view.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.vit_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.vit_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vit_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vit_view.setAlternatingRowColors(True)
        self.vit_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.vit_view.setShowGrid(False)
        self.vit_view.setObjectName("vit_view")
        self.vit_view.horizontalHeader().setHighlightSections(False)
        self.vit_view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.vit_view, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setMaximumSize(QtCore.QSize(20, 20))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/icon/user.svg"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.sex_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.sex_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sex_label)
        self.sex_edit = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.sex_edit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sex_edit.sizePolicy().hasHeightForWidth())
        self.sex_edit.setSizePolicy(sizePolicy)
        self.sex_edit.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.sex_edit.setFont(font)
        self.sex_edit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.sex_edit.setStyleSheet("QComboBox {\n"
"    padding: 2px 0px 2px 2px;\n"
"}\n"
"\n"
"QListView{\n"
"    outline: none;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    color: black;\n"
"    background-color: rgb(204, 232, 255);\n"
"}\n"
"\n"
"QListView::item {\n"
"    min-height: 28px;\n"
"}\n"
"")
        self.sex_edit.setObjectName("sex_edit")
        self.sex_edit.addItem("")
        self.sex_edit.addItem("")
        self.sex_edit.addItem("")
        self.sex_edit.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sex_edit)
        self.birth_label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.birth_label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.birth_label_4.setFont(font)
        self.birth_label_4.setObjectName("birth_label_4")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.birth_label_4)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.mon_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mon_edit.sizePolicy().hasHeightForWidth())
        self.mon_edit.setSizePolicy(sizePolicy)
        self.mon_edit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mon_edit.setFont(font)
        self.mon_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.mon_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.mon_edit.setObjectName("mon_edit")
        self.horizontalLayout_14.addWidget(self.mon_edit)
        self.day_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_edit.sizePolicy().hasHeightForWidth())
        self.day_edit.setSizePolicy(sizePolicy)
        self.day_edit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.day_edit.setFont(font)
        self.day_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.day_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.day_edit.setObjectName("day_edit")
        self.horizontalLayout_14.addWidget(self.day_edit)
        self.year_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year_edit.sizePolicy().hasHeightForWidth())
        self.year_edit.setSizePolicy(sizePolicy)
        self.year_edit.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.year_edit.setFont(font)
        self.year_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.year_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.year_edit.setObjectName("year_edit")
        self.horizontalLayout_14.addWidget(self.year_edit)
        self.formLayout_4.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_14)
        self.verticalLayout_8.addLayout(self.formLayout_4)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(4)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setMaximumSize(QtCore.QSize(20, 20))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/icon/info.svg"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_15.addWidget(self.label_17)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_9)
        self.gridLayout_2.addLayout(self.formLayout, 1, 1, 1, 1)
        self.back_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setMinimumSize(QtCore.QSize(45, 35))
        self.back_btn.setCursor(QtCore.Qt.PointingHandCursor)
        self.back_btn.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"    background-color: #daecf9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0e1f9;\n"
"}\n"
"")
        self.back_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/arrow-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon1)
        self.back_btn.setIconSize(QtCore.QSize(24, 24))
        self.back_btn.setObjectName("back_btn")
        self.gridLayout_2.addWidget(self.back_btn, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(ReqWidget)
        QtCore.QMetaObject.connectSlotsByName(ReqWidget)

    def retranslateUi(self, ReqWidget):
        ReqWidget.setWindowTitle(QtWidgets.QApplication.translate("ReqWidget", "Spartan - Preferences", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ReqWidget", "Nutritional Requirements", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("ReqWidget", "Set requirements according to United States Health Department recommendations", None, -1))
        self.sex_label.setText(QtWidgets.QApplication.translate("ReqWidget", "Sex", None, -1))
        self.sex_edit.setItemText(0, QtWidgets.QApplication.translate("ReqWidget", "Female", None, -1))
        self.sex_edit.setItemText(1, QtWidgets.QApplication.translate("ReqWidget", "Female, lactating", None, -1))
        self.sex_edit.setItemText(2, QtWidgets.QApplication.translate("ReqWidget", "Female, pregnant", None, -1))
        self.sex_edit.setItemText(3, QtWidgets.QApplication.translate("ReqWidget", "Male", None, -1))
        self.birth_label_4.setText(QtWidgets.QApplication.translate("ReqWidget", "Date of birth", None, -1))
        self.mon_edit.setPlaceholderText(QtWidgets.QApplication.translate("ReqWidget", "Month", None, -1))
        self.day_edit.setPlaceholderText(QtWidgets.QApplication.translate("ReqWidget", "Day", None, -1))
        self.year_edit.setPlaceholderText(QtWidgets.QApplication.translate("ReqWidget", "Year", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("ReqWidget", "You can select a recommendation as a guideline then customize it to your needs.", None, -1))

from view.req_view import ReqView
import icon_rc
import icon_rc
