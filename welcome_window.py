import sys

from PySide2.QtWidgets import QApplication, QMainWindow

import spartan
import storage
import main_window
from ui.ui_welcomewindow import Ui_WelcomeWindow


class WelcomeWindow(QMainWindow, Ui_WelcomeWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setup_connections()
        self.show()

    def accept(self):
        if not self.req_wiz_widget.fields_are_valid():
            return

        sex = self.req_wiz_widget.sex
        year = self.req_wiz_widget.bd_year
        mon = self.req_wiz_widget.bd_mon
        day = self.req_wiz_widget.bd_day

        spartan.update_sex_bd_in_db(sex, year, mon, day)

        macro_nuts = self.req_wiz_widget.macro_model.nutrients
        vit_nuts = self.req_wiz_widget.vit_model.nutrients
        mineral_nuts = self.req_wiz_widget.mineral_model.nutrients
        nutrients = macro_nuts + vit_nuts + mineral_nuts

        spartan.update_nuts_in_db(nutrients)

        self.update_wel_check()
        self.run_main_window()
        self.hide()

    def update_wel_check(self):
        with open('run_wel_check.csv', 'w') as check_file:
            check_file.write('skip')

    def run_main_window(self):
        self.main_window = main_window.MainWindow()
        self.main_window.show()

    def reject(self):
        self.close()

    def setup_connections(self):
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome_window = WelcomeWindow()
    sys.exit(app.exec_())
