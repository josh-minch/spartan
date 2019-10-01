MAX_FOOD_ID_LEN = 5
DB_SCALER = 100

RESTRICT_FDS_FILE = 'restrict_fds.csv'
RESTRICT_TYPES_FILE = 'restrict_types.csv'

# Link restriction selections to unique id
preset_grp = {'vegan': 1, 'vegetarian': 2, 'pescatarian': 3,
              'carnivore': 4, 'home': 5, 'custom': 6}
type_grp = {'search': 1, 'generated': 2}

# Values refer to fd_grp id in food databse sr_legacy
fd_grp = {'dairy': 100, 'spice': 200,
          'baby': 300, 'fat': 400, 'poultry': 500, 'soup': 600, 'sausage': 700,
          'breakfast': 800, 'fruit': 900, 'pork': 1000, 'veg': 1100, 'nut': 1200,
          'beef': 1300, 'drink': 1400, 'seafood': 1500, 'legume': 1600, 'lamb': 1700,
          'baked': 1800,  'sweet': 1900, 'cereal': 2000, 'fast': 2100, 'meal': 2200,
          'snack': 2500, 'american': 3500,  'restaurant': 3600}
