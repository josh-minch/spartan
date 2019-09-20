MAX_FOOD_ID_LEN = 5
DB_SCALER = 100

# Value refers to food group id in sr_legacy food database
fd_grp = {'dairy': 100, 'spice': 200, 'baby': 300, 'fat': 400, 'poultry': 500, 'soup': 600,
        'sausage': 700, 'breakfast': 800, 'fruit': 900, 'pork': 1000, 'veg': 1100, 'nut': 1200,
        'beef': 1300, 'drink': 1400, 'seafood': 1500, 'legume': 1600, 'lamb': 1700, 'baked': 1800,
        'sweet': 1900, 'cereal': 2000, 'fast': 2100, 'meal': 2200, 'snack': 2500, 'american': 3500,
        'restaurant': 3600}

plant = {fd_grp['veg'], fd_grp['fruit'], fd_grp['cereal'],
        fd_grp['breakfast'], fd_grp['legume'], fd_grp['nut'], fd_grp['spice']}

animal = {fd_grp['poultry'], fd_grp['pork'], fd_grp['beef'], fd_grp['dairy'],
        fd_grp['seafood'], fd_grp['sausage'], fd_grp['lamb']}

misc = {fd_grp['fat'], fd_grp['meal'], fd_grp['baked'], fd_grp['soup'], fd_grp['snack'],
        fd_grp['sweet'], fd_grp['restaurant'], fd_grp['fast'], fd_grp['baby'], fd_grp['american'],
        fd_grp['drink']}