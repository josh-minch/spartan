import sys

from PySide2.QtCore import Qt, QItemSelectionModel
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PySide2.QtGui import QFont

import spartan
import database
import basic_foods
from gui_constants import *
import gui_helpers
from model.diet_model import DietModel
from model.nutrition_model import NutritionTableModel
from delegate.progress_bar_delegate import ProgressBarDelegate
from ui.ui_optimumdietwindow import Ui_OptimumDietWindow


class OptimumDietWindow(QMainWindow, Ui_OptimumDietWindow):
    def __init__(self, person, type_res, fd_res, parent=None):
        super().__init__(parent=None)
        self.setupUi(self)

        self.person = person
        self.optimizier = spartan.Optimizier(self.person, type_res, fd_res)
        self.optimizier.optimize_diet()
        self.set_description()
        self.populate_diet_table()
        self.populate_nutrition_table()

        self.resize(1400, 900)

        self.setup_connections()
        self.show()

    def set_description(self):
        self.diet_label.setText(self.optimizier.get_solution_status())

    def populate_diet_table(self):
        foods = self.optimizier.get_diet_report()

        # Insert empty row to give space before totals
        foods.append({'id':'', 'name':'', 'cost':'','quantity':'', 'unit':''})

        num_value, cost_value, mass_value = self.optimizier.get_totals()
        foods.append({'id':-1, 'name':str(num_value) + ' items of food', 'cost':cost_value, 'quantity':mass_value, 'unit':'g'})

        self.diet_model = DietModel(foods=foods)
        self.diet_view.setModel(self.diet_model)

        gui_helpers.hide_view_cols(self.diet_view, [0])
        gui_helpers.set_column_widths(self.diet_view, [1], [200])

    def populate_nutrition_table(self):
        (food_ids, food_amounts) = self.optimizier.get_data_for_nutrition_lookup()
        self.ttl_macros, self.ttl_vits, self.ttl_minerals = spartan.get_nutrition(self.person, food_ids, food_amounts)

        macros_model = NutritionTableModel(nutrients=self.ttl_macros, nutrient_group='General')
        vits_model = NutritionTableModel(
            nutrients=self.ttl_vits, nutrient_group='Vitamins')
        minerals_model = NutritionTableModel(
            nutrients=self.ttl_minerals, nutrient_group='Minerals')

        self.macros_view.setModel(macros_model)
        self.vits_view.setModel(vits_model)
        self.minerals_view.setModel(minerals_model)

        self.macros_view.setItemDelegate(ProgressBarDelegate(self))
        self.vits_view.setItemDelegate(ProgressBarDelegate(self))
        self.minerals_view.setItemDelegate(ProgressBarDelegate(self))

        self.setup_nutrition()

    def setup_nutrition(self):
        '''
        gui_helpers.hide_view_cols(
            self.macro_view, [Req.attr_to_col['nut_id']])
        gui_helpers.hide_view_cols(self.vit_view, [Req.attr_to_col['nut_id']])
        gui_helpers.hide_view_cols(
            self.mineral_view, [Req.attr_to_col['nut_id']])


        self.macro_view.setColumnWidth(0, 150)
        self.vit_view.setColumnWidth(0, 150)
        self.mineral_view.setColumnWidth(0, 150)
        '''
        gui_helpers.set_column_widths(self.macros_view, nut_col_to_attr.keys(), nut_col_widths)
        gui_helpers.set_column_widths(self.vits_view, nut_col_to_attr.keys(), nut_col_widths)
        gui_helpers.set_column_widths(
            self.minerals_view, nut_col_to_attr.keys(), nut_col_widths)

        #gui_helpers.set_view_header_weights(self.macros_view, QFont.DemiBold)
        #gui_helpers.set_view_header_weights(self.vits_view, QFont.DemiBold)
        #gui_helpers.set_view_header_weights(self.minerals_view, QFont.DemiBold)

        gui_helpers.vertical_resize_table_view_to_contents(self.macros_view)
        gui_helpers.vertical_resize_table_view_to_contents(self.vits_view)
        gui_helpers.vertical_resize_table_view_to_contents(self.minerals_view)

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

            macros, vits, minerals = spartan.get_nutrition(self.person, food_ids, amounts)

        macros_model = NutritionTableModel(
            nutrients=macros, nutrient_group='General')
        vits_model = NutritionTableModel(
            nutrients=vits, nutrient_group='Vitamins')
        minerals_model = NutritionTableModel(
            nutrients=minerals, nutrient_group='Minerals')

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
