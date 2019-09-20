# Dietary restrictions definitions
from constants import fd_grp, animal, plant, misc

vegan = animal
vegetarian = animal - {fd_grp['dairy']}
pescatarian = animal - {fd_grp['seafood'], fd_grp['dairy']}
carnivore = plant
home = {fd_grp['restaurant'], fd_grp['fast'], fd_grp['meal'], fd_grp['snack']}