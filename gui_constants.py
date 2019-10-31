import platform
from PySide2.QtGui import QFont
import gui_helpers

def system_font_family():
    if platform.system() == 'Windows':
        return 'Segoe UI'
    elif platform.system() == 'Darwin':
        return 'SF Pro Text'
    else:
        return QFont.defaultFamily()

FONT_MAIN_SIZE = 10
FONT_SECONDARY_SIZE = 11

# Nutrition view
NUT_NAME_COL = 0
NUT_AMOUNT_COL = 1
NUT_UNIT_COL = 2
NUT_PERCENT_COL = 3

NUT_NAME_COL_WIDTH = 128
NUT_AMOUNT_COL_WIDTH = 60
NUT_UNIT_COL_WIDTH = 29
NUT_PERCENT_COL_WIDTH = 70

NUT_V_HEADER_SIZE = 22

nut_col_widths = [NUT_NAME_COL_WIDTH, NUT_AMOUNT_COL_WIDTH, NUT_UNIT_COL_WIDTH, NUT_PERCENT_COL_WIDTH]

nut_col_to_attr = {NUT_NAME_COL: 'name', NUT_AMOUNT_COL: 'amount', NUT_UNIT_COL: 'unit',
                    NUT_PERCENT_COL: 'percent'}

# Fridge view
F_NUM_COLS = 15

FOOD_ID_COL = 0
NAME_COL = 1
PRICE_COL = 2
PER_COL = 3
PRICE_QUANTITY_COL = 4
PRICE_UNIT_COL = 5
MIN_COL = 6
MIN_UNIT_COL = 7
MAX_COL = 8
MAX_UNIT_COL = 9
TARGET_COL = 10
TARGET_UNIT_COL = 11
SELECTABLE_UNITS_COL = 12
NUT_QUANT_COL = 13
NUT_QUANT_UNIT_COL = 14

UNIT_COL = (PRICE_UNIT_COL, MIN_UNIT_COL, MAX_UNIT_COL,
            TARGET_UNIT_COL, NUT_QUANT_UNIT_COL)

FOOD_ID_COL_WIDTH = 0
NAME_COL_WIDTH = 100
PRICE_COL_WIDTH = 20
PRICE_QUANTITY_COL_WIDTH = 50
PRICE_UNIT_COL_WDITH = 25
MIN_COL_WIDTH = 25
MIN_UNIT_COL_WIDTH = 10
MAX_COL_WIDTH = 25
MAX_UNIT_COL_WIDTH = 10
TARGET_COL_WIDTH = 25
TARGET_UNIT_COL_WIDTH = 10

PER_COL_WIDTH = 1
VALUE_COL_WIDTH = 55
UNIT_COL_WIDTH = 100

F_COLS_TO_HIDE = [FOOD_ID_COL, PRICE_COL, PER_COL, PRICE_QUANTITY_COL, PRICE_UNIT_COL, MIN_COL,
                  MIN_UNIT_COL, MAX_COL, MAX_UNIT_COL, TARGET_COL, TARGET_UNIT_COL, SELECTABLE_UNITS_COL, NUT_QUANT_COL, NUT_QUANT_UNIT_COL]
P_COLS_TO_HIDE = [FOOD_ID_COL, NAME_COL, MIN_COL, MIN_UNIT_COL, MAX_COL,
                  MAX_UNIT_COL, TARGET_COL, TARGET_UNIT_COL, SELECTABLE_UNITS_COL, NUT_QUANT_COL, NUT_QUANT_UNIT_COL]
C_COLS_TO_HIDE = [FOOD_ID_COL, NAME_COL, PRICE_COL, PER_COL,
                  PRICE_QUANTITY_COL, PRICE_UNIT_COL, SELECTABLE_UNITS_COL, NUT_QUANT_COL, NUT_QUANT_UNIT_COL]
N_COLS_TO_HIDE = [FOOD_ID_COL, NAME_COL, PRICE_COL, PER_COL, PRICE_QUANTITY_COL, PRICE_UNIT_COL, MIN_COL,
                  MIN_UNIT_COL, MAX_COL, MAX_UNIT_COL, TARGET_COL, TARGET_UNIT_COL, SELECTABLE_UNITS_COL]

FRIDGE_V_HEADER_SIZE = 34

f_col_to_attr = {FOOD_ID_COL: 'food_id', NAME_COL: 'name',
                 PRICE_COL: 'price', PRICE_QUANTITY_COL: 'price_quantity', PRICE_UNIT_COL: 'price_unit',
                 MIN_COL: 'min', MIN_UNIT_COL: 'min_unit',
                 MAX_COL: 'max', MAX_UNIT_COL: 'max_unit',
                 TARGET_COL: 'target', TARGET_UNIT_COL: 'target_unit',
                 SELECTABLE_UNITS_COL: 'selectable_units',
                 NUT_QUANT_COL: 'nut_quantity', NUT_QUANT_UNIT_COL: 'nut_quantity_unit'}

# Search view
class Search:
    attrs = ['fd_grp', 'name']
    col_to_attr, attr_to_col = gui_helpers.enumerate_cols(attrs)

# Optimum diet view
O_ID_COL = 0
O_NAME_COL = 1
O_COST_COL = 2
O_AMOUNT_COL= 3
O_UNIT_COL = 4

O_NAME_WIDTH = 500
O_COST_WIDTH = 70
O_AMOUNT_WIDTH = 80
O_UNIT_WIDTH = 10

o_p_col_widths = [O_NAME_WIDTH, O_COST_WIDTH, O_AMOUNT_WIDTH, O_UNIT_WIDTH]
o_w_col_widths = [O_NAME_WIDTH, O_AMOUNT_WIDTH, O_UNIT_WIDTH]

o_col_to_attr = {O_ID_COL: 'id', O_NAME_COL: 'name', O_COST_COL: 'cost',
                 O_AMOUNT_COL: 'quantity', O_UNIT_COL: 'unit'}

# Optimum nutrition view
ON_NAME_COL_WIDTH = 160
ON_AMOUNT_COL_WIDTH = 60
ON_UNIT_COL_WIDTH = 25
ON_PERCENT_COL_WIDTH = 80

on_col_widths = [ON_NAME_COL_WIDTH, ON_AMOUNT_COL_WIDTH,
                ON_UNIT_COL_WIDTH, ON_PERCENT_COL_WIDTH]

# Requirements window
F_INDEX = 0
L_INDEX = 1
P_INDEX = 2
M_INDEX = 3

index_to_sex = {F_INDEX: 'f', L_INDEX: 'l', P_INDEX: 'p', M_INDEX: 'm'}
sex_to_index = {'f': F_INDEX, 'l': L_INDEX, 'p': P_INDEX, 'm': M_INDEX}

US_INDEX = 0
EU_INDEX = 1
JP_INDEX = 2

index_to_rec = {US_INDEX: 'us', EU_INDEX: 'eu', JP_INDEX: 'jp'}
rec_to_index = {'us': US_INDEX, 'eu': EU_INDEX, 'jp': JP_INDEX}

# Requirements model
class Req:
    attrs = ['nut_id', 'name', 'min', 'min_unit',
            'max', 'max_unit', 'target', 'target_unit']
    col_to_attr, attr_to_col = gui_helpers.enumerate_cols(attrs)
