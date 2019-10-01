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

plant = {fd_grp['veg'], fd_grp['fruit'], fd_grp['cereal'],
         fd_grp['breakfast'], fd_grp['legume'], fd_grp['nut'], fd_grp['spice']}

animal = {fd_grp['poultry'], fd_grp['pork'], fd_grp['beef'], fd_grp['dairy'],
          fd_grp['seafood'], fd_grp['sausage'], fd_grp['lamb']}

misc = {fd_grp['fat'], fd_grp['meal'], fd_grp['baked'], fd_grp['soup'], fd_grp['snack'],
        fd_grp['sweet'], fd_grp['restaurant'], fd_grp['fast'], fd_grp['baby'], fd_grp['american'],
        fd_grp['drink']}

class RestrictionPresets:
    vegan = animal
    vegetarian = animal - {fd_grp['dairy']}
    pescatarian = animal - {fd_grp['seafood'], fd_grp['dairy']}
    carnivore = plant
    home = {fd_grp['restaurant'], fd_grp['fast'], fd_grp['meal'], fd_grp['snack']}

fd_grp_display_name = {100: 'dairy and eggs', 200: 'spices and herbs', 300: 'baby food', 400: 'fats and oils',
                        500: 'poultry', 600: 'soups and sauces', 700: 'sausages and deli meats',
                       800: 'breakfast cereals', 900: 'fruits and fruit juices', 1000: 'pork', 1100: 'vegetables', 1200: 'nuts and seeds',
                       1300: 'beef', 1400: 'drinks', 1500: 'seafood', 1600: 'legumes', 1700: 'lamb, veal, game',
                       1800: 'baked products',  1900: 'sweets', 2000: 'cereal grains and pasta', 2100: 'fast food', 2200: 'prepared meals',
                       2500: 'snacks', 3500: 'Native American foods',  3600: 'restaurant food'}

