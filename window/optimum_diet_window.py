import sys

from PySide2.QtCore import Qt, QItemSelectionModel
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PySide2.QtGui import QFont

import spartan
import database
import basic_foods
from gui_constants import *
from gui_helpers import *
from model.diet_model import DietModel
import model.nutrition_model as nutrition_model
from delegate.progress_bar_delegate import ProgressBarDelegate
from ui.ui_optimumdietwindow import Ui_OptimumDietWindow


class OptimumDietWindow(QMainWindow, Ui_OptimumDietWindow):
    def __init__(self, parent=None, person=None):
        super().__init__(parent=None)
        self.setupUi(self)

        self.person = person
        self.optimizier = spartan.Optimizier(self.person)
        self.optimizier.optimize_diet()
        self.optimizier.describe_solution()
        self.populate_title()
        self.populate_diet_table()
        self.populate_nutrition_table()

        self.resize(1400, 900)

        self.setup_connections()
        self.show()

    def populate_title(self):
        self.diet_label.setText(self.optimizier.get_solution_status())

    def populate_diet_table(self):
        foods = self.optimizier.get_diet_report()

        # Insert empty row to give space before totals
        foods.append({'id':'', 'name':'', 'cost':'','quantity':'', 'unit':''})

        num_value, cost_value, mass_value = self.optimizier.get_totals()
        foods.append({'id':-1, 'name':str(num_value) + ' items of food', 'cost':cost_value, 'quantity':mass_value, 'unit':'g'})

        self.diet_model = DietModel(foods=foods)
        self.diet_view.setModel(self.diet_model)
        self.diet_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def populate_nutrition_table(self):
        (food_ids, food_amounts) = self.optimizier.get_data_for_nutrition_lookup()
        self.ttl_macros, self.ttl_vits, self.ttl_minerals = spartan.get_nutrition(self.person, food_ids, food_amounts)

        macros_model = nutrition_model.MacroModel(nutrients=self.ttl_macros)
        vits_model = nutrition_model.VitModel(nutrients=self.ttl_vits)
        minerals_model = nutrition_model.MineralModel(
            nutrients=self.ttl_minerals)

        self.macros_view.setModel(macros_model)
        self.vits_view.setModel(vits_model)
        self.minerals_view.setModel(minerals_model)

        self.macros_view.setItemDelegate(ProgressBarDelegate(self))
        self.vits_view.setItemDelegate(ProgressBarDelegate(self))
        self.minerals_view.setItemDelegate(ProgressBarDelegate(self))

        self.setup_nutrition()

    def setup_nutrition(self):
        set_column_widths(self.macros_view, nut_col_to_attr.keys(), nut_col_widths)
        set_column_widths(self.vits_view, nut_col_to_attr.keys(), nut_col_widths)
        set_column_widths(self.minerals_view, nut_col_to_attr.keys(), nut_col_widths)

        set_view_header_weights(self.macros_view, QFont.DemiBold)
        set_view_header_weights(self.vits_view, QFont.DemiBold)
        set_view_header_weights(self.minerals_view, QFont.DemiBold)

    def display_selected_nutrition(self, selected, deselected):
        total_food_ix = self.diet_model.index(
            self.diet_model.rowCount() - 1, O_ID_COL)

        # If user selects totals row, display nutrition totals
        if selected.contains(total_food_ix):
            macros = self.ttl_macros
            vits = self.ttl_vits
            minerals = self.ttl_minerals
        # Otherwise display selected foods' nutrition
        else:
            food_ids, amounts = [], []
            # Diet model selects every column in a row, but we only need one index per
            # row. Therefore, skip over redundant indices
            selected_row_ixs = self.diet_view.selectionModel().selectedRows()
            for ix in selected_row_ixs:
                food_id_ix = ix.sibling(ix.row(), O_ID_COL)
                amount_ix = ix.sibling(ix.row(), O_AMOUNT_COL)

                food_ids.append(food_id_ix.data(Qt.DisplayRole))
                amounts.append(amount_ix.data(Qt.DisplayRole))

            print(food_ids)
            print(amounts)
            macros, vits, minerals = spartan.get_nutrition(self.person, food_ids, amounts)

        macros_model = nutrition_model.MacroModel(nutrients=macros)
        vits_model = nutrition_model.VitModel(nutrients=vits)
        minerals_model = nutrition_model.MineralModel(nutrients=minerals)

        self.macros_view.setModel(macros_model)
        self.vits_view.setModel(vits_model)
        self.minerals_view.setModel(minerals_model)

        self.macros_view.setItemDelegate(ProgressBarDelegate(self))
        self.vits_view.setItemDelegate(ProgressBarDelegate(self))
        self.minerals_view.setItemDelegate(ProgressBarDelegate(self))

        self.setup_nutrition()

    def setup_connections(self):
        self.diet_view.selectionModel().selectionChanged.connect(self.display_selected_nutrition)

if __name__ == '__main__':
    person = spartan.Person(19, 'm')

    app = QApplication(sys.argv)
    window = OptimumDietWindow(person=person)
    sys.exit(app.exec_())