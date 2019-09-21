# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_reswidget.ui',
# licensing of 'ui/ui_reswidget.ui' applies.
#
# Created: Sat Sep 21 00:33:43 2019
#      by: pyside2-uic  running on PySide2 5.13.0a1.dev1556284177
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ResWidget(object):
    def setupUi(self, ResWidget):
        ResWidget.setObjectName("ResWidget")
        ResWidget.resize(979, 730)
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
        font.setPointSize(10)
        ResWidget.setFont(font)
        self.formLayout = QtWidgets.QFormLayout(ResWidget)
        self.formLayout.setContentsMargins(30, 20, 30, 30)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.back_btn = QtWidgets.QPushButton(ResWidget)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/back-black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(24, 24))
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_3.addWidget(self.back_btn)
        self.label_4 = QtWidgets.QLabel(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vegetarian = QtWidgets.QCheckBox(ResWidget)
        self.vegetarian.setAutoExclusive(False)
        self.vegetarian.setObjectName("vegetarian")
        self.preset_btn_grp = QtWidgets.QButtonGroup(ResWidget)
        self.preset_btn_grp.setObjectName("preset_btn_grp")
        self.preset_btn_grp.addButton(self.vegetarian)
        self.gridLayout_3.addWidget(self.vegetarian, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 3, 2, 1, 1)
        self.generated = QtWidgets.QCheckBox(ResWidget)
        self.generated.setObjectName("generated")
        self.type_btn_grp = QtWidgets.QButtonGroup(ResWidget)
        self.type_btn_grp.setObjectName("type_btn_grp")
        self.type_btn_grp.addButton(self.generated)
        self.gridLayout_3.addWidget(self.generated, 5, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(ResWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMinimumSize(QtCore.QSize(24, 24))
        self.label_37.setMaximumSize(QtCore.QSize(24, 24))
        self.label_37.setText("")
        self.label_37.setPixmap(QtGui.QPixmap(":/images/info-outline.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setObjectName("label_37")
        self.gridLayout_3.addWidget(self.label_37, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 2)
        self.pescatarian = QtWidgets.QCheckBox(ResWidget)
        self.pescatarian.setAutoExclusive(False)
        self.pescatarian.setObjectName("pescatarian")
        self.preset_btn_grp.addButton(self.pescatarian)
        self.gridLayout_3.addWidget(self.pescatarian, 1, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 5, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(ResWidget)
        self.label_38.setObjectName("label_38")
        self.gridLayout_3.addWidget(self.label_38, 4, 1, 1, 2)
        self.vegan = QtWidgets.QCheckBox(ResWidget)
        self.vegan.setAutoExclusive(False)
        self.vegan.setObjectName("vegan")
        self.preset_btn_grp.addButton(self.vegan)
        self.gridLayout_3.addWidget(self.vegan, 1, 3, 1, 1)
        self.search = QtWidgets.QCheckBox(ResWidget)
        self.search.setObjectName("search")
        self.type_btn_grp.addButton(self.search)
        self.gridLayout_3.addWidget(self.search, 4, 3, 1, 1)
        self.carnivore = QtWidgets.QCheckBox(ResWidget)
        self.carnivore.setAutoExclusive(False)
        self.carnivore.setObjectName("carnivore")
        self.preset_btn_grp.addButton(self.carnivore)
        self.gridLayout_3.addWidget(self.carnivore, 2, 3, 1, 1)
        self.custom = QtWidgets.QCheckBox(ResWidget)
        self.custom.setAutoExclusive(False)
        self.custom.setObjectName("custom")
        self.preset_btn_grp.addButton(self.custom)
        self.gridLayout_3.addWidget(self.custom, 2, 5, 1, 1)
        self.home = QtWidgets.QCheckBox(ResWidget)
        self.home.setAutoExclusive(False)
        self.home.setObjectName("home")
        self.preset_btn_grp.addButton(self.home)
        self.gridLayout_3.addWidget(self.home, 2, 4, 1, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.gridLayout_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plant = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.plant.setFont(font)
        self.plant.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plant.setTristate(False)
        self.plant.setObjectName("plant")
        self.food_btn_grp = QtWidgets.QButtonGroup(ResWidget)
        self.food_btn_grp.setObjectName("food_btn_grp")
        self.food_btn_grp.addButton(self.plant)
        self.gridLayout_4.addWidget(self.plant, 0, 0, 1, 1)
        self.animal = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.animal.setFont(font)
        self.animal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.animal.setTristate(False)
        self.animal.setObjectName("animal")
        self.food_btn_grp.addButton(self.animal)
        self.gridLayout_4.addWidget(self.animal, 0, 2, 1, 1)
        self.veg = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.veg.setFont(font)
        self.veg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.veg.setTristate(False)
        self.veg.setObjectName("veg")
        self.food_btn_grp.addButton(self.veg)
        self.gridLayout_4.addWidget(self.veg, 1, 0, 1, 1)
        self.legume = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.legume.setFont(font)
        self.legume.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.legume.setTristate(False)
        self.legume.setObjectName("legume")
        self.food_btn_grp.addButton(self.legume)
        self.gridLayout_4.addWidget(self.legume, 1, 1, 1, 1)
        self.poultry = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.poultry.setFont(font)
        self.poultry.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.poultry.setTristate(False)
        self.poultry.setObjectName("poultry")
        self.food_btn_grp.addButton(self.poultry)
        self.gridLayout_4.addWidget(self.poultry, 1, 2, 1, 1)
        self.seafood = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.seafood.setFont(font)
        self.seafood.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.seafood.setTristate(False)
        self.seafood.setObjectName("seafood")
        self.food_btn_grp.addButton(self.seafood)
        self.gridLayout_4.addWidget(self.seafood, 1, 3, 1, 1)
        self.fruit = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.fruit.setFont(font)
        self.fruit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fruit.setAutoFillBackground(False)
        self.fruit.setCheckable(True)
        self.fruit.setTristate(False)
        self.fruit.setObjectName("fruit")
        self.food_btn_grp.addButton(self.fruit)
        self.gridLayout_4.addWidget(self.fruit, 2, 0, 1, 1)
        self.nut = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.nut.setFont(font)
        self.nut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nut.setTristate(False)
        self.nut.setObjectName("nut")
        self.food_btn_grp.addButton(self.nut)
        self.gridLayout_4.addWidget(self.nut, 2, 1, 1, 1)
        self.pork = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pork.setFont(font)
        self.pork.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pork.setTristate(False)
        self.pork.setObjectName("pork")
        self.food_btn_grp.addButton(self.pork)
        self.gridLayout_4.addWidget(self.pork, 2, 2, 1, 1)
        self.sausage = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.sausage.setFont(font)
        self.sausage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sausage.setTristate(False)
        self.sausage.setObjectName("sausage")
        self.food_btn_grp.addButton(self.sausage)
        self.gridLayout_4.addWidget(self.sausage, 2, 3, 1, 1)
        self.cereal = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.cereal.setFont(font)
        self.cereal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cereal.setTristate(False)
        self.cereal.setObjectName("cereal")
        self.food_btn_grp.addButton(self.cereal)
        self.gridLayout_4.addWidget(self.cereal, 3, 0, 1, 1)
        self.spice = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.spice.setFont(font)
        self.spice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spice.setTristate(False)
        self.spice.setObjectName("spice")
        self.food_btn_grp.addButton(self.spice)
        self.gridLayout_4.addWidget(self.spice, 3, 1, 1, 1)
        self.beef = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.beef.setFont(font)
        self.beef.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.beef.setTristate(False)
        self.beef.setObjectName("beef")
        self.food_btn_grp.addButton(self.beef)
        self.gridLayout_4.addWidget(self.beef, 3, 2, 1, 1)
        self.lamb = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lamb.setFont(font)
        self.lamb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lamb.setTristate(False)
        self.lamb.setObjectName("lamb")
        self.food_btn_grp.addButton(self.lamb)
        self.gridLayout_4.addWidget(self.lamb, 3, 3, 1, 1)
        self.breakfast = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.breakfast.setFont(font)
        self.breakfast.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.breakfast.setTristate(False)
        self.breakfast.setObjectName("breakfast")
        self.food_btn_grp.addButton(self.breakfast)
        self.gridLayout_4.addWidget(self.breakfast, 4, 0, 1, 1)
        self.dairy = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.dairy.setFont(font)
        self.dairy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dairy.setTristate(False)
        self.dairy.setObjectName("dairy")
        self.food_btn_grp.addButton(self.dairy)
        self.gridLayout_4.addWidget(self.dairy, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem2, 5, 1, 1, 1)
        self.misc = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.misc.setFont(font)
        self.misc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.misc.setTristate(False)
        self.misc.setObjectName("misc")
        self.food_btn_grp.addButton(self.misc)
        self.gridLayout_4.addWidget(self.misc, 6, 0, 1, 1)
        self.fat = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.fat.setFont(font)
        self.fat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fat.setTristate(False)
        self.fat.setObjectName("fat")
        self.food_btn_grp.addButton(self.fat)
        self.gridLayout_4.addWidget(self.fat, 7, 0, 1, 1)
        self.restaurant = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.restaurant.setFont(font)
        self.restaurant.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.restaurant.setTristate(False)
        self.restaurant.setObjectName("restaurant")
        self.food_btn_grp.addButton(self.restaurant)
        self.gridLayout_4.addWidget(self.restaurant, 7, 1, 1, 1)
        self.meal = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.meal.setFont(font)
        self.meal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.meal.setTristate(False)
        self.meal.setObjectName("meal")
        self.food_btn_grp.addButton(self.meal)
        self.gridLayout_4.addWidget(self.meal, 8, 0, 1, 1)
        self.fast = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.fast.setFont(font)
        self.fast.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fast.setTristate(False)
        self.fast.setObjectName("fast")
        self.food_btn_grp.addButton(self.fast)
        self.gridLayout_4.addWidget(self.fast, 8, 1, 1, 1)
        self.baked = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.baked.setFont(font)
        self.baked.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.baked.setTristate(False)
        self.baked.setObjectName("baked")
        self.food_btn_grp.addButton(self.baked)
        self.gridLayout_4.addWidget(self.baked, 9, 0, 1, 1)
        self.baby = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.baby.setFont(font)
        self.baby.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.baby.setTristate(False)
        self.baby.setObjectName("baby")
        self.food_btn_grp.addButton(self.baby)
        self.gridLayout_4.addWidget(self.baby, 9, 1, 1, 1)
        self.soup = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.soup.setFont(font)
        self.soup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.soup.setTristate(False)
        self.soup.setObjectName("soup")
        self.food_btn_grp.addButton(self.soup)
        self.gridLayout_4.addWidget(self.soup, 10, 0, 1, 1)
        self.american = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.american.setFont(font)
        self.american.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.american.setTristate(False)
        self.american.setObjectName("american")
        self.food_btn_grp.addButton(self.american)
        self.gridLayout_4.addWidget(self.american, 10, 1, 1, 1)
        self.snack = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.snack.setFont(font)
        self.snack.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.snack.setTristate(False)
        self.snack.setObjectName("snack")
        self.food_btn_grp.addButton(self.snack)
        self.gridLayout_4.addWidget(self.snack, 11, 0, 1, 1)
        self.drink = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.drink.setFont(font)
        self.drink.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.drink.setTristate(False)
        self.drink.setObjectName("drink")
        self.food_btn_grp.addButton(self.drink)
        self.gridLayout_4.addWidget(self.drink, 11, 1, 1, 1)
        self.sweet = QtWidgets.QCheckBox(ResWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.sweet.setFont(font)
        self.sweet.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sweet.setTristate(False)
        self.sweet.setObjectName("sweet")
        self.food_btn_grp.addButton(self.sweet)
        self.gridLayout_4.addWidget(self.sweet, 12, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)

        self.retranslateUi(ResWidget)
        QtCore.QMetaObject.connectSlotsByName(ResWidget)

    def retranslateUi(self, ResWidget):
        ResWidget.setWindowTitle(QtWidgets.QApplication.translate("ResWidget", "Spartan - Preferences", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("ResWidget", "Dietary Restrictions", None, -1))
        self.vegetarian.setText(QtWidgets.QApplication.translate("ResWidget", "Ovo-lacto vegetarian", None, -1))
        self.generated.setText(QtWidgets.QApplication.translate("ResWidget", "Generated diets", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("ResWidget", "Select all that apply", None, -1))
        self.pescatarian.setText(QtWidgets.QApplication.translate("ResWidget", "Pescatarian", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("ResWidget", "Presets", None, -1))
        self.label_38.setText(QtWidgets.QApplication.translate("ResWidget", "Restricted foods won\'t appear in  ", None, -1))
        self.vegan.setText(QtWidgets.QApplication.translate("ResWidget", "Vegan", None, -1))
        self.search.setText(QtWidgets.QApplication.translate("ResWidget", "Search results", None, -1))
        self.carnivore.setText(QtWidgets.QApplication.translate("ResWidget", "Carnivore", None, -1))
        self.custom.setText(QtWidgets.QApplication.translate("ResWidget", "Custom", None, -1))
        self.home.setText(QtWidgets.QApplication.translate("ResWidget", "Home-cooked", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("ResWidget", "Restricted food groups", None, -1))
        self.plant.setText(QtWidgets.QApplication.translate("ResWidget", "Plant products", None, -1))
        self.animal.setText(QtWidgets.QApplication.translate("ResWidget", "Animal products", None, -1))
        self.veg.setText(QtWidgets.QApplication.translate("ResWidget", "Vegetables", None, -1))
        self.legume.setText(QtWidgets.QApplication.translate("ResWidget", "Legumes", None, -1))
        self.poultry.setText(QtWidgets.QApplication.translate("ResWidget", "Poultry", None, -1))
        self.seafood.setText(QtWidgets.QApplication.translate("ResWidget", "Seafood", None, -1))
        self.fruit.setText(QtWidgets.QApplication.translate("ResWidget", "Fruits and fruit juices", None, -1))
        self.nut.setText(QtWidgets.QApplication.translate("ResWidget", "Nuts and seeds", None, -1))
        self.pork.setText(QtWidgets.QApplication.translate("ResWidget", "Pork", None, -1))
        self.sausage.setText(QtWidgets.QApplication.translate("ResWidget", "Sausages and deli meats", None, -1))
        self.cereal.setText(QtWidgets.QApplication.translate("ResWidget", "Cereal grains and pasta", None, -1))
        self.spice.setText(QtWidgets.QApplication.translate("ResWidget", "Spices and herbs", None, -1))
        self.beef.setText(QtWidgets.QApplication.translate("ResWidget", "Beef", None, -1))
        self.lamb.setText(QtWidgets.QApplication.translate("ResWidget", "Lamb, veal, and game", None, -1))
        self.breakfast.setText(QtWidgets.QApplication.translate("ResWidget", "Breakfast cereals", None, -1))
        self.dairy.setText(QtWidgets.QApplication.translate("ResWidget", "Dairy and eggs", None, -1))
        self.misc.setText(QtWidgets.QApplication.translate("ResWidget", "Miscellaneous", None, -1))
        self.fat.setText(QtWidgets.QApplication.translate("ResWidget", "Fats and oils", None, -1))
        self.restaurant.setText(QtWidgets.QApplication.translate("ResWidget", "Restaurant Foods", None, -1))
        self.meal.setText(QtWidgets.QApplication.translate("ResWidget", "Prepared meals", None, -1))
        self.fast.setText(QtWidgets.QApplication.translate("ResWidget", "Fast Foods", None, -1))
        self.baked.setText(QtWidgets.QApplication.translate("ResWidget", "Baked products", None, -1))
        self.baby.setText(QtWidgets.QApplication.translate("ResWidget", "Baby Foods", None, -1))
        self.soup.setText(QtWidgets.QApplication.translate("ResWidget", "Soups, Sauces, and Gravies", None, -1))
        self.american.setText(QtWidgets.QApplication.translate("ResWidget", "American Indian/Alaska Native foods", None, -1))
        self.snack.setText(QtWidgets.QApplication.translate("ResWidget", "Snacks", None, -1))
        self.drink.setText(QtWidgets.QApplication.translate("ResWidget", "Drinks", None, -1))
        self.sweet.setText(QtWidgets.QApplication.translate("ResWidget", "Sweets", None, -1))

import images_rc
