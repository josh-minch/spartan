def enumerate_cols(col_names):
    cols = {}
    for i, col_name in enumerate(col_names):
        cols[col_name] = i
    return cols

# Fridge view
F_NUM_COLS = 13

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

UNIT_COL = (PRICE_UNIT_COL, MIN_UNIT_COL, MAX_UNIT_COL, TARGET_UNIT_COL)

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
VALUE_COL_WIDTH = 50
UNIT_COL_WIDTH = 100

F_COLS_TO_HIDE = [FOOD_ID_COL, PRICE_COL, PER_COL, PRICE_QUANTITY_COL, PRICE_UNIT_COL, MIN_COL,
                  MIN_UNIT_COL, MAX_COL, MAX_UNIT_COL, TARGET_COL, TARGET_UNIT_COL, SELECTABLE_UNITS_COL]
P_COLS_TO_HIDE = [FOOD_ID_COL, NAME_COL, MIN_COL, MIN_UNIT_COL, MAX_COL, MAX_UNIT_COL, TARGET_COL, TARGET_UNIT_COL, SELECTABLE_UNITS_COL]
C_COLS_TO_HIDE = [FOOD_ID_COL, NAME_COL, PRICE_COL, PER_COL, PRICE_QUANTITY_COL, PRICE_UNIT_COL, SELECTABLE_UNITS_COL]

FRIDGE_V_HEADER_SIZE = 32

f_col_to_attr = {FOOD_ID_COL: 'food_id', NAME_COL: 'name',
               PRICE_COL: 'price', PRICE_QUANTITY_COL: 'price_quantity', PRICE_UNIT_COL: 'price_unit',
               MIN_COL: 'min', MIN_UNIT_COL: 'min_unit',
               MAX_COL: 'max', MAX_UNIT_COL: 'max_unit',
               TARGET_COL: 'target', TARGET_UNIT_COL: 'target_unit',
               SELECTABLE_UNITS_COL: 'selectable_units'}


# Nutrition view
NUT_NAME_COL = 0
NUT_AMOUNT_COL = 1
NUT_UNIT_COL = 2
NUT_PERCENT_COL = 3

NUT_NAME_COL_WIDTH = 120
NUT_AMOUNT_COL_WIDTH = 60
NUT_UNIT_COL_WIDTH = 20
NUT_PERCENT_COL_WIDTH = 90

NUT_V_HEADER_SIZE = 22

nut_col_widths = [NUT_NAME_COL_WIDTH, NUT_AMOUNT_COL_WIDTH, NUT_UNIT_COL_WIDTH, NUT_PERCENT_COL_WIDTH]

nut_col_to_attr = {NUT_NAME_COL: 'name', NUT_AMOUNT_COL: 'amount', NUT_UNIT_COL: 'unit',
                    NUT_PERCENT_COL: 'percent'}

# Selected foods view

S_NAME_COL = 0
S_AMOUNT_COL = 1
S_UNIT_COL = 2
S_CALORIES_COL = 3

s_col_to_attr = {S_NAME_COL: 'name', S_AMOUNT_COL: 'amount', S_UNIT_COL: 'unit',
                    S_CALORIES_COL: 'percent'}

# Search view
class Search:
    col_names = ['name', 'fd_grp']
    enumerate_cols(col_names)


# Optimum diet view
O_ID_COL = 0
O_NAME_COL = 1
O_COST_COL = 2
O_AMOUNT_COL= 3
O_UNIT_COL = 4

o_col_to_attr = {O_ID_COL: 'id', O_NAME_COL: 'name', O_COST_COL: 'cost',
                 O_AMOUNT_COL: 'quantity', O_UNIT_COL: 'unit'}

# Requirements window
F_INDEX = 0
L_INDEX = 1
P_INDEX = 2
M_INDEX = 3

F_NAME = ''

index_to_sex = {F_INDEX: 'f', L_INDEX: 'l', P_INDEX: 'p', M_INDEX: 'm'}
sex_to_index = {'f': F_INDEX, 'l': L_INDEX, 'p': P_INDEX, 'm': M_INDEX}

US_INDEX = 0
EU_INDEX = 1
JP_INDEX = 2

index_to_rec = {US_INDEX: 'us', EU_INDEX: 'eu', JP_INDEX: 'jp'}
rec_to_index = {'us': US_INDEX, 'eu': EU_INDEX, 'jp': JP_INDEX}

# Requirements view
R_NAME_COL = 0
R_MIN_COL = 1
R_MIN_UNIT_COL = 2
R_MAX_COL = 3
R_MAX_UNIT_COL = 4

r_col_to_attr = {R_NAME_COL: 'name',
                 R_MIN_COL: 'min', R_MIN_UNIT_COL: 'min_unit',
                 R_MAX_COL: 'max', R_MAX_UNIT_COL: 'max_unit'}

class Res:
    SEARCH_RESTRICT = 1
    GEN_RESTRICT = 2