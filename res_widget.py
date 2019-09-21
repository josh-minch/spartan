from functools import partial

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QKeySequence
from PySide2.QtWidgets import QWidget, QButtonGroup, QCheckBox, QShortcut, QAbstractButton

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

        self.checked_food_btns = set()
        self.list_btns()
        self.assign_id(self.preset_btns, self.preset_btn_grp,
                       constants.preset_grp.values())
        self.assign_id(self.food_btns, self.food_btn_grp,
                       constants.fd_grp.values())
        self.assign_id(self.type_btns, self.type_btn_grp,
                       constants.type_grp.values())

        self.preset_btn_grp.setExclusive(False)
        self.type_btn_grp.setExclusive(False)
        self.food_btn_grp.setExclusive(False)
        self.setup_connections()

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
        self.plant_btns = {self.spice, self.breakfast, self.fruit,
                           self.veg, self.nut, self.legume, self.cereal}
        self.animal_btns = {self.dairy, self.poultry, self.sausage,
                            self.pork, self.beef, self.seafood, self.lamb}
        self.misc_btns = {self.baby, self.fat, self.soup, self.drink, self.baked,
                          self.sweet, self.fast, self.meal, self.snack,
                          self.american, self.restaurant}

        self.vegan_btns = self.animal_btns
        self.vegetarian_btns = self.vegan_btns - {self.animal, self.dairy}
        self.pesc_btns = self.vegetarian_btns - {self.seafood}
        self.carnivore_btns = self.plant_btns
        self.home_btns = {self.restaurant, self.fast, self.meal, self.snack}

        self.preset_btn_sets = [self.vegan_btns, self.vegetarian_btns, self.pesc_btns, self.carnivore_btns, self.home_btns]

    def assign_id(self, btns, group, values):
        for btn, id in zip(btns, values):
            group.setId(btn, id)

    def toggle_group(self, btns, state):
        for btn in btns:
            btn.setChecked(state)

    # Update which foods are checked in restricted foods each time a preset btn
    # is toggled. This prevents unchecking button sets that should remain checked.
    # For example, if a user checks vegan and vegetarian, then unchecks vegetarian,
    # all vegan entries should remain checked
    def update_btns_after_preset_toggle(self, toggled_preset_btn_set, state):
        # If preset is unchecked, first set its members to unchecked
        if state == False:
            for btn in toggled_preset_btn_set:
                btn.setChecked(False)

        # Then, get all buttons that should still be checked
        btns_to_check = set()
        for preset_btn, btn_set in zip(self.preset_btns, self.preset_btn_sets):
            if preset_btn.isChecked():
                btns_to_check = btns_to_check | btn_set

        for btn_to_check in btns_to_check:
            btn_to_check.setChecked(True)

    def update_preset_after_btn_toggle(self, btn):
        '''
        for preset_btn, preset_btn_set in zip(self.preset_btns, self.preset_btn_sets):
            if btn.isChecked() == False and btn in preset_btn_set:
                preset_btn.blockSignals(True)
                preset_btn.setChecked(False)
                preset_btn.blockSignals(False)
        '''
        for preset_btn in self.preset_btns:
            preset_btn.blockSignals(True)
            preset_btn.setChecked(False)
            preset_btn.blockSignals(False)

        presets_to_check = set()
        for preset_btn, preset_btn_set in zip(self.preset_btns, self.preset_btn_sets):
            if self.checked_food_btns >= preset_btn_set:
                presets_to_check.add(preset_btn)

        for preset_to_check in presets_to_check:
            #preset_btn.blockSignals(True)
            preset_to_check.setChecked(True)
            #preset_btn.blockSignals(False)

    def change_res(self, res, id, checked):
        if checked:
            res.append(id)
        else:
            res.remove(id)

    def update_checked_food_btns(self, btn, checked):
        if checked:
            self.checked_food_btns.add(btn)
        else:
            self.checked_food_btns.remove(btn)

    def setup_connections(self):
        # Update restriction values for external use
        self.preset_btn_grp.buttonToggled[int, bool].connect(partial(self.change_res, self.presets))
        self.type_btn_grp.buttonToggled[int, bool].connect(partial(self.change_res, self.types))
        self.food_btn_grp.buttonToggled[int, bool].connect(partial(self.change_res, self.fd_grps))

        # Update currently checked internal member variable
        self.food_btn_grp.buttonToggled[QAbstractButton, bool].connect(self.update_checked_food_btns)

        # Update GUI
        self.plant.stateChanged.connect(partial(self.toggle_group, self.plant_btns))
        self.animal.stateChanged.connect(partial(self.toggle_group, self.animal_btns))
        self.misc.stateChanged.connect(partial(self.toggle_group, self.misc_btns))

        for btn, preset_btn_set in zip(self.preset_btns, self.preset_btn_sets):
            btn.stateChanged.connect(partial(self.update_btns_after_preset_toggle, preset_btn_set))

        self.food_btn_grp.buttonClicked[QAbstractButton].connect(self.update_preset_after_btn_toggle)

        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.print_debug_info)

    def print_debug_info(self):
        print(self.fd_grps)
        print(self.presets)