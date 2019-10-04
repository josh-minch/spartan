# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_prefwindow.ui',
# licensing of 'ui/ui_prefwindow.ui' applies.
#
# Created: Thu Oct  3 18:38:04 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_PrefWindow(object):
    def setupUi(self, PrefWindow):
        PrefWindow.setObjectName("PrefWindow")
        PrefWindow.resize(800, 600)
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
        PrefWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        PrefWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/icon_trimmed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PrefWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PrefWindow)
        self.centralwidget.setObjectName("centralwidget")
        PrefWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PrefWindow)
        QtCore.QMetaObject.connectSlotsByName(PrefWindow)

    def retranslateUi(self, PrefWindow):
        PrefWindow.setWindowTitle(QtWidgets.QApplication.translate("PrefWindow", "Spartan - Preferences", None, -1))

