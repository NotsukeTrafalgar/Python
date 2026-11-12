from random import randint

colors = {'blue': '\u001b[34m',
          'yellow': '\u001b[33m',
          'purple': '\33[95m',
          'red': '\u001b[31m'}

def get_color(text, rarity):
    if rarity == 'common':
       color = colors.get('blue')
       text = f'{color}{text}\033[0m'
    
    elif rarity == 'rare':
        color = colors.get('purple')
        text = f'{color}{text}\033[0m'
    
    elif rarity == 'legendary' or rarity == 'elite':
           color = colors.get('yellow')
           text = f'{color}{text}\033[0m'
    
    elif rarity ==  'boss':
        color = colors.get('red')
        text = f'{color}{text}\033[0m'
    
    return text

def probability(prob):
    miss = randint(0, 100)
    if prob > miss:
        return True
    elif prob < miss:
        return False
