# import function as fct

# read_file = fct.reader('corredores.txt')
# write_file = fct.writer('output.txt', read_file)

import files as fl

pokedex = fl.read('pokemon.txt')
pokedex_show = fl.write('pokedex.txt', pokedex)