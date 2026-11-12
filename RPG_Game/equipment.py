from random import randint, choices
from abc import ABC
from outfunc import get_color, probability



class Equipment(ABC):

    def __init__(self,
                 name: str, 
                 equipment_type: str, 
                 rarity: str):
        
        self.name = name
        self.equipament_type = equipment_type
        self.rarity = rarity


class Weapon(Equipment):

    def __init__(self,
                 name: str, 
                 equipment_type: str, 
                 rarity:str,
                 distancy: str,  
                 damage: int,
                 limit: int) -> None:
        
        super().__init__(name, equipment_type, rarity)

        self.limit = limit
        self.wear = limit
        self.distancy = distancy

        self.min_dmg = max(damage - 2, 1)
        self.max_dmg = damage + 2

    @property
    def damage(self) -> int:
        
        prob = probability(10)
        
        if prob == True:
            critical = randint(self.max_dmg * 2, self.max_dmg * 4)
            return critical            
        else:  
            return randint(self.min_dmg, self.max_dmg)


class Armour(Equipment):

    def __init__(self, 
                 name:str,
                 equipment_type:str, 
                 rarity: str, 
                 defense: int):
       
        super().__init__(name, equipment_type, rarity)

        self.defense = defense / 100

    def reduce_demage(self,damage):
        reduced_damage = damage * self.defense
        final_damage = damage - reduced_damage
        return final_damage

    def reflect_damage(self, damage):
        return damage * 0.25

weapons_list = []   

def load_weapons(filename="equipment.txt"):


    with open(filename, "r", encoding="utf-8") as infile:
        content = infile.read()

        groups = content.split("//")

        for object in groups:
            itens = object.split()

            for item in itens:
                datas = item.split(";")

                if len(datas) == 6:
                    nome, dano, tipo, distancia, raridade, limite = datas

                    nome = get_color(nome, raridade)
                    weapon = Weapon(nome,
                                    tipo,
                                    raridade,
                                    distancia,
                                    int(dano),
                                    int(limite))
                    
                    weapons_list.append(weapon)
            
        return weapons_list


armours_list = []
def load_armours(filename="equipment.txt"):

    with open(filename, "r", encoding="utf-8") as infile:
        content = infile.read()

        groups = content.split("//")

        for object in groups:
            itens = object.split()

            for item in itens:
                datas = item.split(";")

                if len(datas) == 4:
                    nome, defesa, tipo, raridade = datas

                    nome = get_color(nome, raridade)
                    armour = Armour(nome,
                                    tipo,
                                    raridade,
                                    int(defesa))
                    
                    armours_list.append(armour)
            
        return armours_list

armours = load_armours()
weapons = load_weapons()

def random_equipment(objects, common, rare, elite, legendary):
    object_weight = []

    for object in objects:
        if object.rarity == "common":
            object_weight.append(common)
        
        elif object.rarity == "rare":
            object_weight.append(rare)
        
        elif object.rarity == "elite":
            object_weight.append(elite)
        
        elif object.rarity == "legendary":
            object_weight.append(legendary)
        
    return choices(objects,weights=object_weight,k=1)[0]

def drop_weapon(rarity):
    if rarity == 'common':
        return random_equipment(weapons, 100, 30, 1, 0)

    elif rarity == 'rare':
        return random_equipment(weapons, 40, 100, 20, 10)
    
    elif rarity == 'elite':
        return random_equipment(weapons, 10, 80, 100, 50)

    elif rarity == 'boss':
        return random_equipment(weapons, 1, 1, 1, 100)


def drop_armour(rarity):
    if rarity == 'common':
        return random_equipment(armours, 100, 30, 1, 0)

    elif rarity == 'rare':
            return random_equipment(armours, 40, 80, 20, 1)
    
    elif rarity == 'elite':
        return random_equipment(armours, 10, 40, 80, 20)

    elif rarity == 'boss':
        return random_equipment(armours, 1, 1, 1, 100)

def spawn_armour():
    armour_weight = []

    for armour in armours:
        if armour.rarity == "common":
            armour_weight.append(80)
        
        elif armour.rarity == "rare":
            armour_weight.append(10)
        
        elif armour.rarity == "elite":
            armour_weight.append(10)
        
        elif armour.rarity == "legendary":
            armour_weight.append(2)
        
    return choices(armours,weights=armour_weight,k=1)[0]



