from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget

from ui.ui_prefwidget import Ui_PrefWidget


class PrefWidget(QWidget, Ui_PrefWidget):
    def __init__(self, person, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.person = person
        self.set_preview_text()

        self.req_btn.setIcon(QPixmap("images/person-outline.png"))
        self.res_btn.setIcon(QPixmap("images/food.png"))

    def set_preview_text(self):
        # TODO: acount for age < 1 year
        if self.person.rec and self.person.sex and self.person.age is not None:
            req_label_text = self.person.rec + '\n' + self.person.sex + '\n' + str(self.person.age) + ' years old'
            self.req_label.setText(req_label_text)

        if self.person.food_groups is not None:
            res_label_text = 'No ' + str(self.person.food_groups)
            self.res_food_label.setText(res_label_text)

        if self.person.restrict_types is not None:
            res_type_label_text = 'Restricted foods will not appear in ' + str(self.person.restrict_types)

