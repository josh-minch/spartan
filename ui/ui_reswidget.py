# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_reswidget.ui',
# licensing of 'ui/ui_reswidget.ui' applies.
#
# Created: Tue Oct 29 21:58:25 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ResWidget(object):
    def setupUi(self, ResWidget):
        ResWidget.setObjectName("ResWidget")
        ResWidget.resize(1101, 803)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResWidget.sizePolicy().hasHeightForWidth())
        ResWidget.setSizePolicy(sizePolicy)
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
        ResWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        ResWidget.setFont(font)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ResWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(ResWidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 912, 888))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setContentsMargins(30, 25, 30, 30)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setVerticalSpacing(30)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.back_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/back-black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(24, 24))
        self.back_btn.setObjectName("back_btn")
        self.gridLayout_3.addWidget(self.back_btn, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.snack = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.snack.setFont(font)
        self.snack.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.snack.setTristate(False)
        self.snack.setObjectName("snack")
        self.food_btn_grp = QtWidgets.QButtonGroup(ResWidget)
        self.food_btn_grp.setObjectName("food_btn_grp")
        self.food_btn_grp.addButton(self.snack)
        self.gridLayout.addWidget(self.snack, 24, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_37.setMinimumSize(QtCore.QSize(24, 24))
        self.label_37.setMaximumSize(QtCore.QSize(24, 24))
        self.label_37.setText("")
        self.label_37.setPixmap(QtGui.QPixmap(":/images/info-outline.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout.addWidget(self.label_38)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.breakfast = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.breakfast.setFont(font)
        self.breakfast.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.breakfast.setTristate(False)
        self.breakfast.setObjectName("breakfast")
        self.food_btn_grp.addButton(self.breakfast)
        self.gridLayout.addWidget(self.breakfast, 13, 0, 1, 2)
        self.fast = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.fast.setFont(font)
        self.fast.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fast.setTristate(False)
        self.fast.setObjectName("fast")
        self.food_btn_grp.addButton(self.fast)
        self.gridLayout.addWidget(self.fast, 21, 2, 1, 1)
        self.fat = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.fat.setFont(font)
        self.fat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fat.setTristate(False)
        self.fat.setObjectName("fat")
        self.food_btn_grp.addButton(self.fat)
        self.gridLayout.addWidget(self.fat, 20, 0, 1, 2)
        self.cereal = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.cereal.setFont(font)
        self.cereal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cereal.setTristate(False)
        self.cereal.setObjectName("cereal")
        self.food_btn_grp.addButton(self.cereal)
        self.gridLayout.addWidget(self.cereal, 12, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 14, 0, 1, 1)
        self.vegan = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.vegan.setAutoExclusive(False)
        self.vegan.setObjectName("vegan")
        self.preset_btn_grp = QtWidgets.QButtonGroup(ResWidget)
        self.preset_btn_grp.setObjectName("preset_btn_grp")
        self.preset_btn_grp.addButton(self.vegan)
        self.gridLayout.addWidget(self.vegan, 4, 0, 1, 2)
        self.fruit = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.fruit.setFont(font)
        self.fruit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fruit.setAutoFillBackground(False)
        self.fruit.setCheckable(True)
        self.fruit.setTristate(False)
        self.fruit.setObjectName("fruit")
        self.food_btn_grp.addButton(self.fruit)
        self.gridLayout.addWidget(self.fruit, 11, 0, 1, 2)
        self.seafood = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.seafood.setFont(font)
        self.seafood.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.seafood.setTristate(False)
        self.seafood.setObjectName("seafood")
        self.food_btn_grp.addButton(self.seafood)
        self.gridLayout.addWidget(self.seafood, 15, 2, 1, 1)
        self.drink = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.drink.setFont(font)
        self.drink.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.drink.setTristate(False)
        self.drink.setObjectName("drink")
        self.food_btn_grp.addButton(self.drink)
        self.gridLayout.addWidget(self.drink, 24, 2, 1, 1)
        self.restaurant = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.restaurant.setFont(font)
        self.restaurant.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.restaurant.setTristate(False)
        self.restaurant.setObjectName("restaurant")
        self.food_btn_grp.addButton(self.restaurant)
        self.gridLayout.addWidget(self.restaurant, 20, 2, 1, 1)
        self.pescatarian = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.pescatarian.setAutoExclusive(False)
        self.pescatarian.setObjectName("pescatarian")
        self.preset_btn_grp.addButton(self.pescatarian)
        self.gridLayout.addWidget(self.pescatarian, 6, 0, 1, 1)
        self.lamb = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lamb.setFont(font)
        self.lamb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lamb.setTristate(False)
        self.lamb.setObjectName("lamb")
        self.food_btn_grp.addButton(self.lamb)
        self.gridLayout.addWidget(self.lamb, 17, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 2)
        self.home = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.home.setAutoExclusive(False)
        self.home.setObjectName("home")
        self.preset_btn_grp.addButton(self.home)
        self.gridLayout.addWidget(self.home, 4, 2, 1, 1)
        self.pork = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pork.setFont(font)
        self.pork.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pork.setTristate(False)
        self.pork.setObjectName("pork")
        self.food_btn_grp.addButton(self.pork)
        self.gridLayout.addWidget(self.pork, 16, 0, 1, 2)
        self.custom = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.custom.setObjectName("custom")
        self.preset_btn_grp.addButton(self.custom)
        self.gridLayout.addWidget(self.custom, 6, 2, 1, 1)
        self.sweet = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.sweet.setFont(font)
        self.sweet.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sweet.setTristate(False)
        self.sweet.setObjectName("sweet")
        self.food_btn_grp.addButton(self.sweet)
        self.gridLayout.addWidget(self.sweet, 25, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 3)
        self.veg = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.veg.setFont(font)
        self.veg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.veg.setTristate(False)
        self.veg.setObjectName("veg")
        self.food_btn_grp.addButton(self.veg)
        self.gridLayout.addWidget(self.veg, 10, 0, 1, 1)
        self.nut = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.nut.setFont(font)
        self.nut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nut.setTristate(False)
        self.nut.setObjectName("nut")
        self.food_btn_grp.addButton(self.nut)
        self.gridLayout.addWidget(self.nut, 11, 2, 1, 1)
        self.search = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.search.setObjectName("search")
        self.type_btn_grp = QtWidgets.QButtonGroup(ResWidget)
        self.type_btn_grp.setObjectName("type_btn_grp")
        self.type_btn_grp.addButton(self.search)
        self.gridLayout.addWidget(self.search, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 19, 0, 1, 1)
        self.spice = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.spice.setFont(font)
        self.spice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spice.setTristate(False)
        self.spice.setObjectName("spice")
        self.food_btn_grp.addButton(self.spice)
        self.gridLayout.addWidget(self.spice, 12, 2, 1, 1)
        self.legume = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.legume.setFont(font)
        self.legume.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.legume.setTristate(False)
        self.legume.setObjectName("legume")
        self.food_btn_grp.addButton(self.legume)
        self.gridLayout.addWidget(self.legume, 10, 2, 1, 1)
        self.american = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.american.setFont(font)
        self.american.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.american.setTristate(False)
        self.american.setObjectName("american")
        self.food_btn_grp.addButton(self.american)
        self.gridLayout.addWidget(self.american, 23, 2, 1, 1)
        self.vegetarian = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.vegetarian.setAutoExclusive(False)
        self.vegetarian.setObjectName("vegetarian")
        self.preset_btn_grp.addButton(self.vegetarian)
        self.gridLayout.addWidget(self.vegetarian, 5, 0, 1, 1)
        self.sausage = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.sausage.setFont(font)
        self.sausage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sausage.setTristate(False)
        self.sausage.setObjectName("sausage")
        self.food_btn_grp.addButton(self.sausage)
        self.gridLayout.addWidget(self.sausage, 16, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.meal = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.meal.setFont(font)
        self.meal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.meal.setTristate(False)
        self.meal.setObjectName("meal")
        self.food_btn_grp.addButton(self.meal)
        self.gridLayout.addWidget(self.meal, 21, 0, 1, 2)
        self.poultry = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.poultry.setFont(font)
        self.poultry.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.poultry.setTristate(False)
        self.poultry.setObjectName("poultry")
        self.food_btn_grp.addButton(self.poultry)
        self.gridLayout.addWidget(self.poultry, 15, 0, 1, 2)
        self.carnivore = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.carnivore.setAutoExclusive(False)
        self.carnivore.setObjectName("carnivore")
        self.preset_btn_grp.addButton(self.carnivore)
        self.gridLayout.addWidget(self.carnivore, 5, 2, 1, 1)
        self.beef = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.beef.setFont(font)
        self.beef.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.beef.setTristate(False)
        self.beef.setObjectName("beef")
        self.food_btn_grp.addButton(self.beef)
        self.gridLayout.addWidget(self.beef, 17, 0, 1, 2)
        self.baby = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.baby.setFont(font)
        self.baby.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.baby.setTristate(False)
        self.baby.setObjectName("baby")
        self.food_btn_grp.addButton(self.baby)
        self.gridLayout.addWidget(self.baby, 22, 2, 1, 1)
        self.baked = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.baked.setFont(font)
        self.baked.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.baked.setTristate(False)
        self.baked.setObjectName("baked")
        self.food_btn_grp.addButton(self.baked)
        self.gridLayout.addWidget(self.baked, 22, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 7, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 9, 0, 1, 1)
        self.generated = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.generated.setObjectName("generated")
        self.type_btn_grp.addButton(self.generated)
        self.gridLayout.addWidget(self.generated, 1, 2, 1, 1)
        self.dairy = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.dairy.setFont(font)
        self.dairy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dairy.setTristate(False)
        self.dairy.setObjectName("dairy")
        self.food_btn_grp.addButton(self.dairy)
        self.gridLayout.addWidget(self.dairy, 18, 0, 1, 1)
        self.soup = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.soup.setFont(font)
        self.soup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.soup.setTristate(False)
        self.soup.setObjectName("soup")
        self.food_btn_grp.addButton(self.soup)
        self.gridLayout.addWidget(self.soup, 23, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(ResWidget)
        QtCore.QMetaObject.connectSlotsByName(ResWidget)

    def retranslateUi(self, ResWidget):
        ResWidget.setWindowTitle(QtWidgets.QApplication.translate("ResWidget", "Spartan - Preferences", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("ResWidget", "Dietary Restrictions", None, -1))
        self.snack.setText(QtWidgets.QApplication.translate("ResWidget", "Snacks", None, -1))
        self.label_38.setText(QtWidgets.QApplication.translate("ResWidget", "Restricted foods won\'t appear in  ", None, -1))
        self.breakfast.setText(QtWidgets.QApplication.translate("ResWidget", "Breakfast cereals", None, -1))
        self.fast.setText(QtWidgets.QApplication.translate("ResWidget", "Fast food", None, -1))
        self.fat.setText(QtWidgets.QApplication.translate("ResWidget", "Fats and oils", None, -1))
        self.cereal.setText(QtWidgets.QApplication.translate("ResWidget", "Cereal grains and pasta", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ResWidget", "Animal products", None, -1))
        self.vegan.setText(QtWidgets.QApplication.translate("ResWidget", "Vegan", None, -1))
        self.fruit.setText(QtWidgets.QApplication.translate("ResWidget", "Fruits and fruit juices", None, -1))
        self.seafood.setText(QtWidgets.QApplication.translate("ResWidget", "Seafood", None, -1))
        self.drink.setText(QtWidgets.QApplication.translate("ResWidget", "Drinks", None, -1))
        self.restaurant.setText(QtWidgets.QApplication.translate("ResWidget", "Restaurant food", None, -1))
        self.pescatarian.setText(QtWidgets.QApplication.translate("ResWidget", "Pescatarian", None, -1))
        self.lamb.setText(QtWidgets.QApplication.translate("ResWidget", "Lamb, veal, and game", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("ResWidget", "Presets", None, -1))
        self.home.setText(QtWidgets.QApplication.translate("ResWidget", "Home-cooked", None, -1))
        self.pork.setText(QtWidgets.QApplication.translate("ResWidget", "Pork", None, -1))
        self.custom.setText(QtWidgets.QApplication.translate("ResWidget", "Custom", None, -1))
        self.sweet.setText(QtWidgets.QApplication.translate("ResWidget", "Sweets", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("ResWidget", "Restricted food groups", None, -1))
        self.veg.setText(QtWidgets.QApplication.translate("ResWidget", "Vegetables", None, -1))
        self.nut.setText(QtWidgets.QApplication.translate("ResWidget", "Nuts and seeds", None, -1))
        self.search.setText(QtWidgets.QApplication.translate("ResWidget", "Search results", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ResWidget", "Miscellaneous", None, -1))
        self.spice.setText(QtWidgets.QApplication.translate("ResWidget", "Spices and herbs", None, -1))
        self.legume.setText(QtWidgets.QApplication.translate("ResWidget", "Legumes", None, -1))
        self.american.setText(QtWidgets.QApplication.translate("ResWidget", "Native American foods", None, -1))
        self.vegetarian.setText(QtWidgets.QApplication.translate("ResWidget", "Ovo-lacto vegetarian", None, -1))
        self.sausage.setText(QtWidgets.QApplication.translate("ResWidget", "Sausages and deli meats", None, -1))
        self.meal.setText(QtWidgets.QApplication.translate("ResWidget", "Prepared meals", None, -1))
        self.poultry.setText(QtWidgets.QApplication.translate("ResWidget", "Poultry", None, -1))
        self.carnivore.setText(QtWidgets.QApplication.translate("ResWidget", "Carnivore", None, -1))
        self.beef.setText(QtWidgets.QApplication.translate("ResWidget", "Beef", None, -1))
        self.baby.setText(QtWidgets.QApplication.translate("ResWidget", "Baby food", None, -1))
        self.baked.setText(QtWidgets.QApplication.translate("ResWidget", "Baked products", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ResWidget", "Plant products", None, -1))
        self.generated.setText(QtWidgets.QApplication.translate("ResWidget", "Generated diets", None, -1))
        self.dairy.setText(QtWidgets.QApplication.translate("ResWidget", "Dairy and eggs", None, -1))
        self.soup.setText(QtWidgets.QApplication.translate("ResWidget", "Soups and sauces", None, -1))

import images_rc
