# Dietary restrictions definitions
from constants import fd_grp

plant = {fd_grp['veg'], fd_grp['fruit'], fd_grp['cereal'],
        fd_grp['breakfast'], fd_grp['legume'], fd_grp['nut'], fd_grp['spice']}

animal = {fd_grp['poultry'], fd_grp['pork'], fd_grp['beef'], fd_grp['dairy'],
        fd_grp['seafood'], fd_grp['sausage'], fd_grp['lamb']}

misc = {fd_grp['fat'], fd_grp['meal'], fd_grp['baked'], fd_grp['soup'], fd_grp['snack'],
        fd_grp['sweet'], fd_grp['restaurant'], fd_grp['fast'], fd_grp['baby'], fd_grp['american'],
        fd_grp['drink']}

vegan = animal
vegetarian = animal - {fd_grp['dairy']}
pescatarian = animal - {fd_grp['seafood'], fd_grp['dairy']}
carnivore = plant
home = {fd_grp['restaurant'], fd_grp['fast'], fd_grp['meal'], fd_grp['snack']}

