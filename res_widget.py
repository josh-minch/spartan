from functools import partial

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QKeySequence
from PySide2.QtWidgets import QWidget, QButtonGroup, QShortcut

import res
import constants
from ui.ui_reswidget import Ui_ResWidget


class ResWidget(QWidget, Ui_ResWidget):


    def __init__(self, presets, types, fd_grps, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.presets = presets
        self.types = types
        self.fd_grps = fd_grps

        food_btns = [self.dairy, self.spice, self.baby, self.fat, self.poultry, self.soup,
                self.sausage, self.breakfast, self.fruit, self.pork, self.veg, self.nut,
                self.beef, self.drink, self.seafood, self.legume, self.lamb, self.baked,
                self.sweet, self.cereal, self.fast, self.meal,
                self.snack, self.american, self.restaurant]
        self.assign_id(food_btns, self.food_btn_grp)

        self.preset_btn_grp.setExclusive(False)
        self.type_btn_grp.setExclusive(False)
        self.food_btn_grp.setExclusive(False)
        self.setup_connections()

    def assign_id(self, btns, group):
        for btn, id in zip(btns, constants.fd_grp.values()):
            group.setId(btn, id)

    def change_res(self, res, id, checked):
        if checked:
            res.append(id)
        elif checked is False:
            res.remove(id)

    def connect_btn_grp_toggle(self, btn_grp, res):
        btn_grp.buttonToggled.connect(partial(self.change_res, res))

    def setup_connections(self):
        self.connect_btn_grp_toggle(self.preset_btn_grp, res=self.presets)
        self.connect_btn_grp_toggle(self.type_btn_grp, res=self.types)
        self.connect_btn_grp_toggle(self.food_btn_grp, res=self.fd_grps)

        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        print(self.presets)
        print(self.types)
        print(self.fd_grps)
