# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_reqwidget.ui',
# licensing of 'ui/ui_reqwidget.ui' applies.
#
# Created: Thu Sep 19 18:45:09 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ReqWidget(object):
    def setupUi(self, ReqWidget):
        ReqWidget.setObjectName("ReqWidget")
        ReqWidget.resize(905, 605)
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
        font.setPointSize(10)
        ReqWidget.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReqWidget.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(ReqWidget)
        self.formLayout.setContentsMargins(30, 20, 30, 30)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(ReqWidget)
        self.back_btn.setMinimumSize(QtCore.QSize(45, 35))
        self.back_btn.setCursor(QtCore.Qt.PointingHandCursor)
        self.back_btn.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
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
        icon1.addPixmap(QtGui.QPixmap("../images/back-black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon1)
        self.back_btn.setIconSize(QtCore.QSize(24, 24))
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout.addWidget(self.back_btn)
        self.label = QtWidgets.QLabel(ReqWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setMargin(0)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(ReqWidget)
        self.label_14.setMaximumSize(QtCore.QSize(20, 20))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("../images/person-outline.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(ReqWidget)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_4.setHorizontalSpacing(20)
        self.formLayout_4.setVerticalSpacing(10)
        self.formLayout_4.setObjectName("formLayout_4")
        self.req_label = QtWidgets.QLabel(ReqWidget)
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
        self.req_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.req_label.setFont(font)
        self.req_label.setObjectName("req_label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.req_label)
        self.req_edit = QtWidgets.QComboBox(ReqWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.req_edit.sizePolicy().hasHeightForWidth())
        self.req_edit.setSizePolicy(sizePolicy)
        self.req_edit.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.req_edit.setFont(font)
        self.req_edit.setMouseTracking(False)
        self.req_edit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.req_edit.setStyleSheet("QComboBox {\n"
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
        self.req_edit.setFrame(True)
        self.req_edit.setObjectName("req_edit")
        self.req_edit.addItem("")
        self.req_edit.addItem("")
        self.req_edit.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.req_edit)
        self.sex_label = QtWidgets.QLabel(ReqWidget)
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
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sex_label)
        self.sex_edit = QtWidgets.QComboBox(ReqWidget)
        self.sex_edit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sex_edit.sizePolicy().hasHeightForWidth())
        self.sex_edit.setSizePolicy(sizePolicy)
        self.sex_edit.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
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
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sex_edit)
        self.birth_label_4 = QtWidgets.QLabel(ReqWidget)
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
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.birth_label_4.setFont(font)
        self.birth_label_4.setObjectName("birth_label_4")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.birth_label_4)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.mon_edit = QtWidgets.QLineEdit(ReqWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mon_edit.sizePolicy().hasHeightForWidth())
        self.mon_edit.setSizePolicy(sizePolicy)
        self.mon_edit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.mon_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.mon_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.mon_edit.setObjectName("mon_edit")
        self.horizontalLayout_14.addWidget(self.mon_edit)
        self.day_edit = QtWidgets.QLineEdit(ReqWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_edit.sizePolicy().hasHeightForWidth())
        self.day_edit.setSizePolicy(sizePolicy)
        self.day_edit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.day_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.day_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.day_edit.setObjectName("day_edit")
        self.horizontalLayout_14.addWidget(self.day_edit)
        self.year_edit = QtWidgets.QLineEdit(ReqWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year_edit.sizePolicy().hasHeightForWidth())
        self.year_edit.setSizePolicy(sizePolicy)
        self.year_edit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.year_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.year_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.year_edit.setObjectName("year_edit")
        self.horizontalLayout_14.addWidget(self.year_edit)
        self.formLayout_4.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_14)
        self.verticalLayout_8.addLayout(self.formLayout_4)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(4)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(ReqWidget)
        self.label_16.setMaximumSize(QtCore.QSize(20, 20))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("../images/info-outline.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(ReqWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_15.addWidget(self.label_17)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.cust_edit = QtWidgets.QCheckBox(ReqWidget)
        self.cust_edit.setObjectName("cust_edit")
        self.verticalLayout_9.addWidget(self.cust_edit)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_9)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.macro_view = QtWidgets.QTableView(ReqWidget)
        self.macro_view.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.macro_view.setFont(font)
        self.macro_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.macro_view.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.macro_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.macro_view.setAlternatingRowColors(True)
        self.macro_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.macro_view.setShowGrid(False)
        self.macro_view.setObjectName("macro_view")
        self.macro_view.verticalHeader().setVisible(False)
        self.horizontalLayout_16.addWidget(self.macro_view)
        self.vit_view = QtWidgets.QTableView(ReqWidget)
        self.vit_view.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.vit_view.setFont(font)
        self.vit_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.vit_view.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.vit_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.vit_view.setAlternatingRowColors(True)
        self.vit_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.vit_view.setShowGrid(False)
        self.vit_view.setObjectName("vit_view")
        self.vit_view.verticalHeader().setVisible(False)
        self.horizontalLayout_16.addWidget(self.vit_view)
        self.mineral_view = QtWidgets.QTableView(ReqWidget)
        self.mineral_view.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.mineral_view.setFont(font)
        self.mineral_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mineral_view.setStyleSheet("QHeaderView::section{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QTableView {\n"
"    alternate-background-color: rgb(247, 247, 247);\n"
"}")
        self.mineral_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mineral_view.setAlternatingRowColors(True)
        self.mineral_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.mineral_view.setShowGrid(False)
        self.mineral_view.setObjectName("mineral_view")
        self.mineral_view.verticalHeader().setVisible(False)
        self.horizontalLayout_16.addWidget(self.mineral_view)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_16)

        self.retranslateUi(ReqWidget)
        QtCore.QMetaObject.connectSlotsByName(ReqWidget)

    def retranslateUi(self, ReqWidget):
        ReqWidget.setWindowTitle(QtWidgets.QApplication.translate("ReqWidget", "Spartan - Preferences", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ReqWidget", "Nutritional Requirements", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("ReqWidget", "Set requirements according to national recommendations.", None, -1))
        self.req_label.setText(QtWidgets.QApplication.translate("ReqWidget", "Recommendation by", None, -1))
        self.req_edit.setCurrentText(QtWidgets.QApplication.translate("ReqWidget", "United States (Health Department)", None, -1))
        self.req_edit.setItemText(0, QtWidgets.QApplication.translate("ReqWidget", "United States (Health Department)", None, -1))
        self.req_edit.setItemText(1, QtWidgets.QApplication.translate("ReqWidget", "European Union (Food Safety Authority)", None, -1))
        self.req_edit.setItemText(2, QtWidgets.QApplication.translate("ReqWidget", "Japan (Ministry of Health, Labour and Welfare)", None, -1))
        self.sex_label.setText(QtWidgets.QApplication.translate("ReqWidget", "Sex", None, -1))
        self.sex_edit.setItemText(0, QtWidgets.QApplication.translate("ReqWidget", "Female", None, -1))
        self.sex_edit.setItemText(1, QtWidgets.QApplication.translate("ReqWidget", "Female, lactating", None, -1))
        self.sex_edit.setItemText(2, QtWidgets.QApplication.translate("ReqWidget", "Female, pregnant", None, -1))
        self.sex_edit.setItemText(3, QtWidgets.QApplication.translate("ReqWidget", "Male", None, -1))
        self.birth_label_4.setText(QtWidgets.QApplication.translate("ReqWidget", "Date of birth", None, -1))
        self.mon_edit.setPlaceholderText(QtWidgets.QApplication.translate("ReqWidget", "Month", None, -1))
        self.day_edit.setPlaceholderText(QtWidgets.QApplication.translate("ReqWidget", "Day", None, -1))
        self.year_edit.setPlaceholderText(QtWidgets.QApplication.translate("ReqWidget", "Year", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("ReqWidget", "Select a recommendation as a guideline then customize it to your needs.", None, -1))
        self.cust_edit.setText(QtWidgets.QApplication.translate("ReqWidget", "Allow custom requirements", None, -1))

