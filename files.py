def read (file):
    with open(file, 'r', encoding='utf8') as infile:
            poke_list = infile.readlines()

            pokedex = []

            for pokemon in poke_list:
                  data = {}

                  num, name, element, stats = pokemon.split(',')

                  data['no.'] = num
                  data['nome'] = name
                  data['elemento'] = element
                  data['status'] = int(stats)

                  pokedex.append(data)

            pokedex.sort(key=lambda data: data['status'], reverse=True)

    return pokedex

def write (file, pokedex):
      with open(file, 'w', encoding = 'utf-8') as output:
            ranking = 0
            for data in pokedex:
                  ranking = ranking + 1
                  output.write(f"{ranking}°lugar: {data['no.']:^15}"
                               f"{data['nome']:^20}{data['elemento']:^20}"
                               f"{data['status']}\n")