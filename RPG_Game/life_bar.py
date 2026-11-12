class LifeBar:

    symbol_remaining: str = '\u2589'
    symbol_lost: str = '_'

    colors = {'red': '\u001b[31m',
              'blue': '\u001b[34m',
              'green': '\033[92m',
              'yellow': '\u001b[33m',
              'purple': '\33[95m',
              'default': '\033[0m'
              }
       
    def __init__(self, 
                 entity,
                 lenght: int = 20,
                 color: str = '' ) -> None:
        self.entity = entity
        self.lenght = lenght
        self.max_value = entity.max_health
        self.current_value = entity.health
        self.color = LifeBar.colors.get(color) or LifeBar.colors['default']

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw(self) -> None:
        remaining_life = round(self.current_value/self.max_value*self.lenght)
        lost_life = self.lenght - remaining_life

        print(f'{self.entity.name} health: {self.entity.health}/{self.entity.max_health}')
        print(f'{self.color}'
              f'{remaining_life*LifeBar.symbol_remaining}'
              f'{lost_life*LifeBar.symbol_lost}'
              f'{LifeBar.colors["default"]}')