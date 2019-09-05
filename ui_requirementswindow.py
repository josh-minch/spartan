# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_requirementswindow.ui',
# licensing of 'ui_requirementswindow.ui' applies.
#
# Created: Thu Sep  5 15:01:11 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_RequirementsWindow(object):
    def setupUi(self, RequirementsWindow):
        RequirementsWindow.setObjectName("RequirementsWindow")
        RequirementsWindow.resize(847, 719)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RequirementsWindow.sizePolicy().hasHeightForWidth())
        RequirementsWindow.setSizePolicy(sizePolicy)
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
        RequirementsWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        RequirementsWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RequirementsWindow.setWindowIcon(icon)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(RequirementsWindow)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(RequirementsWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMargin(0)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(RequirementsWindow)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.req_label = QtWidgets.QLabel(RequirementsWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.req_label.setFont(font)
        self.req_label.setObjectName("req_label")
        self.verticalLayout_5.addWidget(self.req_label)
        self.req_edit = QtWidgets.QComboBox(RequirementsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.req_edit.sizePolicy().hasHeightForWidth())
        self.req_edit.setSizePolicy(sizePolicy)
        self.req_edit.setMinimumSize(QtCore.QSize(200, 0))
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
        self.req_edit.setPalette(palette)
        self.req_edit.setObjectName("req_edit")
        self.req_edit.addItem("")
        self.verticalLayout_5.addWidget(self.req_edit)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sex_label = QtWidgets.QLabel(RequirementsWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")
        self.verticalLayout_4.addWidget(self.sex_label)
        self.sex_edit = QtWidgets.QComboBox(RequirementsWindow)
        self.sex_edit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sex_edit.sizePolicy().hasHeightForWidth())
        self.sex_edit.setSizePolicy(sizePolicy)
        self.sex_edit.setMinimumSize(QtCore.QSize(130, 0))
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
        self.sex_edit.setPalette(palette)
        self.sex_edit.setObjectName("sex_edit")
        self.sex_edit.addItem("")
        self.sex_edit.addItem("")
        self.sex_edit.addItem("")
        self.sex_edit.addItem("")
        self.verticalLayout_4.addWidget(self.sex_edit)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.birth_label = QtWidgets.QLabel(RequirementsWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.birth_label.setFont(font)
        self.birth_label.setObjectName("birth_label")
        self.verticalLayout_3.addWidget(self.birth_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mon_edit = QtWidgets.QLineEdit(RequirementsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mon_edit.sizePolicy().hasHeightForWidth())
        self.mon_edit.setSizePolicy(sizePolicy)
        self.mon_edit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.mon_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.mon_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.mon_edit.setObjectName("mon_edit")
        self.horizontalLayout_2.addWidget(self.mon_edit)
        self.day_edit = QtWidgets.QLineEdit(RequirementsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_edit.sizePolicy().hasHeightForWidth())
        self.day_edit.setSizePolicy(sizePolicy)
        self.day_edit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.day_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.day_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.day_edit.setObjectName("day_edit")
        self.horizontalLayout_2.addWidget(self.day_edit)
        self.year_edit = QtWidgets.QLineEdit(RequirementsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year_edit.sizePolicy().hasHeightForWidth())
        self.year_edit.setSizePolicy(sizePolicy)
        self.year_edit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.year_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.year_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.year_edit.setObjectName("year_edit")
        self.horizontalLayout_2.addWidget(self.year_edit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(RequirementsWindow)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.cust_edit = QtWidgets.QCheckBox(RequirementsWindow)
        self.cust_edit.setObjectName("cust_edit")
        self.verticalLayout_2.addWidget(self.cust_edit)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.macro_view = QtWidgets.QTableView(RequirementsWindow)
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
        self.macro_view.setShowGrid(False)
        self.macro_view.setObjectName("macro_view")
        self.macro_view.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.macro_view)
        self.vit_view = QtWidgets.QTableView(RequirementsWindow)
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
        self.vit_view.setShowGrid(False)
        self.vit_view.setObjectName("vit_view")
        self.vit_view.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.vit_view)
        self.mineral_view = QtWidgets.QTableView(RequirementsWindow)
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
        self.mineral_view.setShowGrid(False)
        self.mineral_view.setObjectName("mineral_view")
        self.mineral_view.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.mineral_view)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(RequirementsWindow)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_6.addWidget(self.buttonBox)
        self.verticalLayout_6.setStretch(1, 1)

        self.retranslateUi(RequirementsWindow)
        QtCore.QMetaObject.connectSlotsByName(RequirementsWindow)
        RequirementsWindow.setTabOrder(self.mon_edit, self.day_edit)
        RequirementsWindow.setTabOrder(self.day_edit, self.year_edit)

    def retranslateUi(self, RequirementsWindow):
        RequirementsWindow.setWindowTitle(QtWidgets.QApplication.translate("RequirementsWindow", "Nutritional Requirements", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("RequirementsWindow", "Nutritional Requirements", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("RequirementsWindow", "Set your nutritional requirements according to national recommendations.", None, -1))
        self.req_label.setText(QtWidgets.QApplication.translate("RequirementsWindow", "Recommendations by", None, -1))
        self.req_edit.setItemText(0, QtWidgets.QApplication.translate("RequirementsWindow", "USDA", None, -1))
        self.sex_label.setText(QtWidgets.QApplication.translate("RequirementsWindow", "Sex", None, -1))
        self.sex_edit.setItemText(0, QtWidgets.QApplication.translate("RequirementsWindow", "Female", None, -1))
        self.sex_edit.setItemText(1, QtWidgets.QApplication.translate("RequirementsWindow", "Female, lactating", None, -1))
        self.sex_edit.setItemText(2, QtWidgets.QApplication.translate("RequirementsWindow", "Female, pregnant", None, -1))
        self.sex_edit.setItemText(3, QtWidgets.QApplication.translate("RequirementsWindow", "Male", None, -1))
        self.birth_label.setText(QtWidgets.QApplication.translate("RequirementsWindow", "Birthdate", None, -1))
        self.mon_edit.setPlaceholderText(QtWidgets.QApplication.translate("RequirementsWindow", "Month", None, -1))
        self.day_edit.setPlaceholderText(QtWidgets.QApplication.translate("RequirementsWindow", "Day", None, -1))
        self.year_edit.setPlaceholderText(QtWidgets.QApplication.translate("RequirementsWindow", "Year", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("RequirementsWindow", "Or, select a recommendation as a guideline then customize it to your needs.", None, -1))
        self.cust_edit.setText(QtWidgets.QApplication.translate("RequirementsWindow", "Allow custom requirements", None, -1))

