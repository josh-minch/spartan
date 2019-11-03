# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_prefwidget.ui',
# licensing of 'ui/ui_prefwidget.ui' applies.
#
# Created: Sat Nov  2 19:15:29 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_PrefWidget(object):
    def setupUi(self, PrefWidget):
        PrefWidget.setObjectName("PrefWidget")
        PrefWidget.resize(753, 502)
        PrefWidget.setMaximumSize(QtCore.QSize(16777215, 16777213))
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
        PrefWidget.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PrefWidget.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(PrefWidget)
        self.formLayout.setContentsMargins(30, 25, 30, 30)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(PrefWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setMargin(0)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.req_btn = QtWidgets.QCommandLinkButton(PrefWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.req_btn.setFont(font)
        self.req_btn.setCursor(QtCore.Qt.PointingHandCursor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/balance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.req_btn.setIcon(icon1)
        self.req_btn.setObjectName("req_btn")
        self.verticalLayout_3.addWidget(self.req_btn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.age_label = QtWidgets.QLabel(PrefWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.age_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.age_label.setFont(font)
        self.age_label.setText("")
        self.age_label.setObjectName("age_label")
        self.verticalLayout.addWidget(self.age_label)
        self.sex_label = QtWidgets.QLabel(PrefWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.sex_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.sex_label.setFont(font)
        self.sex_label.setText("")
        self.sex_label.setObjectName("sex_label")
        self.verticalLayout.addWidget(self.sex_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.res_btn = QtWidgets.QCommandLinkButton(PrefWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.res_btn.setFont(font)
        self.res_btn.setCursor(QtCore.Qt.PointingHandCursor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/food.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.res_btn.setIcon(icon2)
        self.res_btn.setCheckable(False)
        self.res_btn.setAutoRepeat(False)
        self.res_btn.setObjectName("res_btn")
        self.verticalLayout_4.addWidget(self.res_btn)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.res_type_label = QtWidgets.QLabel(PrefWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(59, 59, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 59, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.res_type_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.res_type_label.setFont(font)
        self.res_type_label.setText("")
        self.res_type_label.setWordWrap(False)
        self.res_type_label.setObjectName("res_type_label")
        self.verticalLayout_2.addWidget(self.res_type_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_5)

        self.retranslateUi(PrefWidget)
        QtCore.QMetaObject.connectSlotsByName(PrefWidget)

    def retranslateUi(self, PrefWidget):
        PrefWidget.setWindowTitle(QtWidgets.QApplication.translate("PrefWidget", "Spartan - Preferences", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("PrefWidget", "Settings", None, -1))
        self.req_btn.setText(QtWidgets.QApplication.translate("PrefWidget", " Nutritional requirements", None, -1))
        self.res_btn.setText(QtWidgets.QApplication.translate("PrefWidget", " Dietary restrictions", None, -1))

