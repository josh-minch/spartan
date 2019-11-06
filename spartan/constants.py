SQL_VARIABLE_LIMIT = 999
MAX_FOOD_ID_LEN = 5
DB_SCALER = 100
SEARCH_RESTRICT = 1
GEN_RESTRICT = 2

RESTRICT_FDS_FILE = 'fd_res.csv'
RESTRICT_TYPES_FILE = 'type_res.csv'

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

fd_grp_search_name = {100: 'Dairy and Eggs', 200: 'Spices and Herbs', 300: 'Baby food', 400: 'Fats and Oils',
                       500: 'Poultry', 600: 'Soups and Sauces', 700: 'Sausages and Deli Meats',
                       800: 'Breakfast Cereals', 900: 'Fruits and Fruit juices', 1000: 'Pork', 1100: 'Vegetables', 1200: 'Nuts and Seeds',
                       1300: 'Beef', 1400: 'Drinks', 1500: 'Seafood', 1600: 'Legumes', 1700: 'Lamb, Veal, Game',
                       1800: 'Baked products',  1900: 'Sweets', 2000: 'Cereal grains and Pasta', 2100: 'Fast food', 2200: 'Prepared meals',
                       2500: 'Snacks', 3500: 'Native American foods',  3600: 'Restaurant food'}

