from datetime import date

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget

from constants import type_grp, fd_grp, fd_grp_display_name
from ui.ui_prefwidget import Ui_PrefWidget


class PrefWidget(QWidget, Ui_PrefWidget):
    def __init__(self, person, type_res, fd_res, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.person = person
        self.type_res = type_res
        self.fd_res = fd_res
        self.set_preview_text()

        self.req_btn.setIcon(QPixmap("images/person-outline.png"))
        self.res_btn.setIcon(QPixmap("images/food.png"))

    def set_preview_text(self):
        self.age_label.setText((get_age_text(self.person)))
        self.sex_label.setText((get_sex_text(self.person.sex)))

        res_label_text = self.get_fd_res_text(self.fd_res.res)
        self.res_food_label.setText(res_label_text)

        res_type_label_text = self.get_type_res_text(self.type_res.res)
        self.res_type_label.setText(res_type_label_text)

    def get_type_res_text(self, res):
        if len(res) == 0:
            #self.res_food_label.hide()
            return 'Restricted foods will still appear in search results and generated diets'

        #self.res_food_label.show()
        text = 'Restricted foods will not appear in '
        if {type_grp['search']} == res:
            text += 'search results'
        if {type_grp['generated']} == res:
            text += 'generated diets'
        if {type_grp['search'], type_grp['generated']} == res:
            text += 'search results or generated diets'
        return text

    def get_fd_res_text(self, restrictions):
        if len(restrictions) == 0:
            #self.res_type_label.hide()
            return 'No restricted foods'

        #self.res_type_label.show()
        text = 'Restricted food groups: '
        res_fds = []
        for restriction in restrictions:
            res_fds.append(fd_grp_display_name[restriction])
        text += ", ".join(res_fds)
        return text

def get_age_text(person):
    if person.age < 1:
        age_months = req.calculate_age_months(
            person.bd_mon, person.bd_day)
        return str(age_months) + ' months old'
    else:
        return '{:.0f}'.format(person.age//1) + ' years old'

def get_sex_text(sex):
    if sex == 'f':
        return 'Female'
    elif sex == 'l':
        return 'Female, lactating'
    elif sex == 'p':
        return 'Female, pregnant'
    elif sex == 'm':
        return 'Male'


