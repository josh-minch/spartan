from datetime import date

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget

import req
from constants import type_grp, fd_grp, fd_grp_display_name
from ui.ui_prefwidget import Ui_PrefWidget


class PrefWidget(QWidget, Ui_PrefWidget):
    def __init__(self, sex, bd, type_res, fd_res, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.sex = sex
        self.bd = bd
        self.type_res = type_res
        self.fd_res = fd_res

        self.set_preview_text()

    def set_preview_text(self):
        self.age_label.setText(self.get_age_text())
        self.sex_label.setText(self.get_sex_text())

        res_type_label_text = get_type_res_text(self.type_res.res)
        self.res_type_label.setText(res_type_label_text)

    def get_age_text(self):
        age = req.calculate_age(*self.bd)
        if age < 1:
            bd_year, bd_mon, bd_day = self.bd
            age_months = req.calculate_age_months(bd_mon, bd_day)
            return str(age_months) + ' months old'
        else:
            return '{:.0f}'.format(age//1) + ' years old'

    def get_sex_text(self):
        if self.sex == 'f':
            return 'Female'
        elif self.sex == 'l':
            return 'Female, lactating'
        elif self.sex == 'p':
            return 'Female, pregnant'
        elif self.sex == 'm':
            return 'Male'

def get_type_res_text(res):
    if len(res) == 0:
        return 'Restricted foods will still appear in search results and generated diets'

    text = 'Restricted foods will not appear in '
    if {type_grp['search']} == res:
        text += 'search results'
    if {type_grp['generated']} == res:
        text += 'generated diets'
    if {type_grp['search'], type_grp['generated']} == res:
        text += 'search results or generated diets'
    return text




