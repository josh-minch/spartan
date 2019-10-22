from functools import partial

from PySide2.QtCore import Qt
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QWidget, QShortcut, QButtonGroup

import storage
from constants import preset_grp, fd_grp, type_grp, RESTRICT_FDS_FILE, RESTRICT_TYPES_FILE
from ui.ui_reswidget import Ui_ResWidget


class ResWidget(QWidget, Ui_ResWidget):
    def __init__(self, person, type_res, fd_res, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.person = person
        self.type_res = type_res
        self.fd_res = fd_res

        self.list_btns()
        self.assign_id(self.preset_btns, self.preset_btn_grp, preset_grp.values())
        self.assign_id(self.food_btns, self.food_btn_grp, fd_grp.values())
        self.assign_id(self.type_btns, self.type_btn_grp, type_grp.values())

        self.type_btn_grp.setExclusive(False)
        self.food_btn_grp.setExclusive(False)
        self.preset_btn_grp.setExclusive(False)
        self.setup_connections()
        self.init_btn_states()

    def init_btn_states(self):
        self.check_btns(self.type_btn_grp, self.type_res.res)
        self.check_btns(self.food_btn_grp, self.fd_res.res)
        self.update_preset_after_btn_toggle()

    def check_btns(self, btn_grp, restrictions):
        for restriction in restrictions:
            for btn in btn_grp.buttons():
                if btn_grp.id(btn) == restriction:
                    btn_grp.blockSignals(True)
                    btn.setChecked(True)
                    btn_grp.blockSignals(False)

    def update_btns_after_preset_toggle(self, toggled_preset_btn_set, state):
        for btn in self.food_btn_grp.buttons():
            btn.setCheckState(Qt.Unchecked)

        if state == True:
            for btn in toggled_preset_btn_set:
                #self.food_btn_grp.blockSignals(True)
                btn.setCheckState(Qt.Checked)
                #self.food_btn_grp.blockSignals(False)
        '''
        # Then, get all buttons that should still be checked
        btns_to_check = set()
        for preset_btn, btn_set in zip(self.preset_btns, self.preset_btn_sets):
            if preset_btn.isChecked():
                btns_to_check = btns_to_check | btn_set

        for btn_to_check in btns_to_check:
            btn_to_check.setChecked(True)
        '''

    def update_preset_after_btn_toggle(self):
        for preset_btn in self.preset_btn_grp.buttons():
            preset_btn.blockSignals(True)
            preset_btn.setCheckState(Qt.Unchecked)
            preset_btn.blockSignals(False)

        checked_food_btns = {btn for btn in self.food_btn_grp.buttons() if btn.isChecked()}
        for preset_btn, preset_btn_set in zip(self.preset_btns, self.preset_btn_sets):
            if checked_food_btns == preset_btn_set:
                # If currently checked btns match a preset, check that preset
                preset_btn.blockSignals(True)
                preset_btn.setCheckState(Qt.Checked)
                preset_btn.blockSignals(False)
            else:
                preset_btn.blockSignals(True)
                preset_btn.setCheckState(Qt.Unchecked)
                preset_btn.blockSignals(False)

        checked_preset_btns = {btn for btn in self.preset_btns if btn.isChecked()}
        if len(checked_food_btns) > 0 and len(checked_preset_btns) == 0:
            # If btns are checked but no preset matches, set custom
            self.custom.setCheckState(Qt.Checked)

    def change_res(self, res, id, checked):
        if checked:
            res.add_res(id)
        else:
            res.remove_res(id)

    def update_checked_food_btns(self, btn, checked):
        if checked:
            self.checked_food_btns.add(btn)
        else:
            self.checked_food_btns.remove(btn)

    def assign_id(self, btns, group, values):
        for btn, id in zip(btns, values):
            group.setId(btn, id)

    def list_btns(self):
        # List btns in order so their ids can be assigned programmatically
        self.preset_btns = [self.vegan, self.vegetarian, self.pescatarian,
                            self.carnivore, self.home]
        self.food_btns = [self.dairy, self.spice, self.baby, self.fat,
                          self.poultry, self.soup, self.sausage, self.breakfast,
                          self.fruit, self.pork, self.veg, self.nut, self.beef,
                          self.drink, self.seafood, self.legume, self.lamb, self.baked,
                          self.sweet, self.cereal, self.fast, self.meal,
                          self.snack, self.american, self.restaurant]
        self.type_btns = [self.search, self.generated]

        # Qt Designer apparently does not support the creation of intersectiong groups
        # The remaining groups are enumerated here
        self.vegan_btns = {self.dairy, self.poultry, self.sausage,
                           self.pork, self.beef, self.seafood, self.lamb}
        self.vegetarian_btns = self.vegan_btns - {self.dairy}
        self.pesc_btns = self.vegetarian_btns - {self.seafood}
        self.carnivore_btns = {self.spice, self.breakfast, self.fruit,
                               self.veg, self.nut, self.legume, self.cereal, self.baked, self.sweet}
        self.home_btns = {self.restaurant, self.fast, self.meal, self.snack}
        self.preset_btn_sets = [self.vegan_btns, self.vegetarian_btns,
                                self.pesc_btns, self.carnivore_btns, self.home_btns]

    def setup_connections(self):
        # Update restriction values for external use
        self.type_btn_grp.buttonToggled[int, bool].connect(
            partial(self.change_res, self.type_res))
        self.food_btn_grp.buttonToggled[int, bool].connect(
            partial(self.change_res, self.fd_res))

        # Update GUI
        self.food_btn_grp.buttonToggled.connect(
            self.update_preset_after_btn_toggle)

        for btn, preset_btn_set in zip(self.preset_btns, self.preset_btn_sets):
            btn.toggled.connect(
                partial(self.update_btns_after_preset_toggle, preset_btn_set))


        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        for preset_btn in self.preset_btn_grp.buttons():
            self.blockSignals(True)
            preset_btn.setCheckState(Qt.Unchecked)
            self.blockSignals(False)

