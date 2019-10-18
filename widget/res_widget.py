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
        self.setup_connections()
        self.init_btn_states()

    def init_btn_states(self):
        self.check_btns(self.type_btn_grp, self.type_res.res)
        self.check_btns(self.food_btn_grp, self.fd_res.res)
        self.update_select_all_after_btn_toggle()

    def check_btns(self, btn_grp, restrictions):
        for restriction in restrictions:
            for btn in btn_grp.buttons():
                if btn_grp.id(btn) == restriction:
                    btn_grp.blockSignals(True)
                    btn.setChecked(True)
                    btn_grp.blockSignals(False)

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

    def update_preset_after_btn_toggle(self):
        for preset_btn in self.preset_btns:
            preset_btn.blockSignals(True)
            preset_btn.setChecked(False)
            preset_btn.blockSignals(False)

        checked_btns = {
            btn for btn in self.food_btn_grp.buttons() if btn.isChecked()}
        for preset_btn, preset_btn_set in zip(self.preset_btns, self.preset_btn_sets):
            if checked_btns == preset_btn_set:
                # If currently checked btns match a preset, check that preset
                preset_btn.setCheckState(Qt.Checked)

        '''
        if len(checked_btns) > 0:
            # If btns are checked but no preset matches, set custom
            self.custom.setChecked(True)
        '''
    def update_select_all_after_btn_toggle(self):
        for select_all_btn in self.select_all_btns:
            select_all_btn.blockSignals(True)
            select_all_btn.setChecked(False)
            select_all_btn.blockSignals(False)

        checked_btns = {
            btn for btn in self.food_btn_grp.buttons() if btn.isChecked()}
        for select_all_btn, select_all_btn_set in zip(self.select_all_btns, self.select_all_btn_sets):
            if checked_btns >= select_all_btn_set:
                select_all_btn.setChecked(True)

    def toggle_group(self, btns, state):
        for btn in btns:
            btn.setChecked(state)

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
        self.select_all_btns = [self.plant, self.animal, self.misc]

        # Qt Designer apparently does not support the creation of intersectiong groups
        # The remaining groups are enumerated here
        self.plant_btns = {self.spice, self.breakfast, self.fruit,
                           self.veg, self.nut, self.legume, self.cereal}
        self.animal_btns = {self.dairy, self.poultry, self.sausage,
                            self.pork, self.beef, self.seafood, self.lamb}
        self.misc_btns = {self.baby, self.fat, self.soup, self.drink, self.baked,
                          self.sweet, self.fast, self.meal, self.snack,
                          self.american, self.restaurant}
        self.select_all_btn_sets = [
            self.plant_btns, self.animal_btns, self.misc_btns]

        self.vegan_btns = self.animal_btns
        self.vegetarian_btns = self.vegan_btns - {self.animal, self.dairy}
        self.pesc_btns = self.vegetarian_btns - {self.seafood}
        self.carnivore_btns = self.plant_btns
        self.home_btns = {self.restaurant, self.fast, self.meal, self.snack}
        self.preset_btn_sets = [self.vegan_btns, self.vegetarian_btns,
                                self.pesc_btns, self.carnivore_btns, self.home_btns]

    def setup_connections(self):
        # Update restriction values for external use
        self.type_btn_grp.buttonToggled[int, bool].connect(
            partial(self.change_res, self.type_res))
        self.food_btn_grp.buttonToggled[int, bool].connect(
            partial(self.change_res, self.fd_res))

        # Update permanent storage
        #self.type_btn_grp.buttonToggled.connect(self.write_types_to_csv)
        #self.food_btn_grp.buttonToggled.connect(self.write_fds_to_csv)

        # Update GUI
        self.plant.stateChanged.connect(
            partial(self.toggle_group, self.plant_btns))
        self.animal.stateChanged.connect(
            partial(self.toggle_group, self.animal_btns))
        self.misc.stateChanged.connect(
            partial(self.toggle_group, self.misc_btns))

        for btn, preset_btn_set in zip(self.preset_btns, self.preset_btn_sets):
            btn.stateChanged.connect(
                partial(self.update_btns_after_preset_toggle, preset_btn_set))

        self.food_btn_grp.buttonToggled.connect(
            self.update_preset_after_btn_toggle)
        self.food_btn_grp.buttonToggled.connect(
            self.update_select_all_after_btn_toggle)

        debug_shortcut = QShortcut(QKeySequence(Qt.Key_F1), self)
        debug_shortcut.activated.connect(self.init_btn_states)
