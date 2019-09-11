# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_optimumdietwindow.ui',
# licensing of 'ui_optimumdietwindow.ui' applies.
#
# Created: Wed Sep 11 16:06:54 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OptimumDietWindow(object):
    def setupUi(self, OptimumDietWindow):
        OptimumDietWindow.setObjectName("OptimumDietWindow")
        OptimumDietWindow.resize(800, 600)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OptimumDietWindow.setWindowIcon(icon)
        OptimumDietWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(OptimumDietWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.diet_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.diet_label.setFont(font)
        self.diet_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.diet_label.setObjectName("diet_label")
        self.verticalLayout.addWidget(self.diet_label)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/opt_diet.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.diet_view = QtWidgets.QTableView(self.centralwidget)
        self.diet_view.setObjectName("diet_view")
        self.horizontalLayout.addWidget(self.diet_view)
        self.nutrition_view = QtWidgets.QTableView(self.centralwidget)
        self.nutrition_view.setObjectName("nutrition_view")
        self.horizontalLayout.addWidget(self.nutrition_view)
        self.verticalLayout.addLayout(self.horizontalLayout)
        OptimumDietWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OptimumDietWindow)
        QtCore.QMetaObject.connectSlotsByName(OptimumDietWindow)

    def retranslateUi(self, OptimumDietWindow):
        OptimumDietWindow.setWindowTitle(QtWidgets.QApplication.translate("OptimumDietWindow", "Spartan - Optimum diet", None, -1))
        self.diet_label.setText(QtWidgets.QApplication.translate("OptimumDietWindow", "Optimum diet is", None, -1))

