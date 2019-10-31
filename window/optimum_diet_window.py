import sys

from PySide2.QtCore import Qt, QItemSelectionModel, QSettings
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
        super().__init__(parent)
        self.setupUi(self)
        self.person = person
        self.optimizer = spartan.Optimizer(self.person, type_res, fd_res)

        self.optimizer.optimize_diet()
        self.populate_diet_table()
        self.populate_nutrition_table()

        self.setup_connections()

        self.showMaximized()
        self.read_settings()
        self.set_description()
        self.show()

    def set_description(self):
        title, subtitle = self.optimizer.get_solution_status()
        self.title_label.setText(title)
        self.diet_label.setText(subtitle)

    def populate_diet_table(self):
        foods = self.optimizer.get_diet_report()

        # Insert empty row to give space before totals
        foods.append({'id':'', 'name':'', 'cost':'','quantity':'', 'unit':''})

        num_value, cost_value, mass_value = self.optimizer.get_totals()
        foods.append({'id':-1, 'name':str(num_value) + ' items of food', 'cost':cost_value, 'quantity':mass_value, 'unit':'g'})

        self.diet_model = DietModel(foods=foods)
        self.diet_view.setModel(self.diet_model)
        self.setup_diet_view()

    def setup_diet_view(self):
        cols_to_hide = [O_ID_COL]
        col_to_set_width = [O_NAME_COL, O_COST_COL, O_AMOUNT_COL, O_UNIT_COL]
        if self.optimizer.optimization_type == 'w':
            cols_to_hide.append(O_COST_COL)
            col_to_set_width.remove(O_COST_COL)
            col_widths = o_w_col_widths
        elif self.optimizer.optimization_type == 'p':
            col_widths = o_p_col_widths

        gui_helpers.hide_view_cols(self.diet_view, cols_to_hide)
        gui_helpers.set_header_font(self.diet_view, FONT_SECONDARY_SIZE, QFont.DemiBold)
        gui_helpers.set_column_widths(self.diet_view, col_to_set_width, col_widths)
        self.diet_label.setMaximumWidth(sum(col_widths))
        self.diet_view.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def populate_nutrition_table(self):
        (food_ids, food_amounts) = self.optimizer.get_data_for_nutrition_lookup()
        self.ttl_macros, self.ttl_vits, self.ttl_minerals = spartan.get_nutrition(self.person, food_ids, food_amounts)

        self.setup_nutrition_view_group(
            self.ttl_macros, self.ttl_vits, self.ttl_minerals)

    def display_selected_nutrition(self, selected, deselected):
        total_food_ix = self.diet_model.index(
            self.diet_model.rowCount() - 1, O_ID_COL)

        # If user selects totals row, display nutrition totals
        if selected == [] or selected.contains(total_food_ix):
            macro = self.ttl_macros
            vit = self.ttl_vits
            mineral = self.ttl_minerals
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

            macro, vit, mineral = spartan.get_nutrition(self.person, food_ids, amounts)

        self.setup_nutrition_view_group(macro, vit, mineral)

    def setup_nutrition_view_group(self, macro_data, vit_data, mineral_data):
        self.setup_nutrition_view(self.macro_view, macro_data, 'General')
        self.setup_nutrition_view(self.vit_view, vit_data, 'Vitamins')
        self.setup_nutrition_view(self.mineral_view, mineral_data, 'Minerals')

    # Create model with data and nutrient group, then assign delegate and font, col widths, size
    def setup_nutrition_view(self, view, model_data, nutrient_group):
        model = NutritionTableModel(nutrients=model_data, nutrient_group=nutrient_group)
        view.setModel(model)
        view.setItemDelegate(ProgressBarDelegate(self))

        gui_helpers.set_header_font(view, FONT_SECONDARY_SIZE, QFont.DemiBold)
        gui_helpers.set_column_widths(view, nut_col_to_attr.keys(), on_col_widths)
        view.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        gui_helpers.vertical_resize_table_view_to_contents(view)

    def setup_connections(self):
        self.diet_view.selectionModel().selectionChanged.connect(self.display_selected_nutrition)

    def closeEvent(self, event):
        settings = QSettings("spartan", "spartan")
        settings.setValue("diet/geometry", self.saveGeometry())
        settings.setValue("diet/windowState", self.saveState())
        super().closeEvent(self, event)

    def read_settings(self):
        settings = QSettings("spartan", "spartan")
        self.restoreGeometry(settings.value("diet/geometry"))
        self.restoreState(settings.value("diet/windowState"))
