from abc import ABC
from random import randint
from life_bar import LifeBar
from equipment import Weapon, Armour, drop_weapon, drop_armour
from outfunc import probability, get_color


class Character(ABC):
   
        
    life_bar: LifeBar

    def __init__(self, 
                 name: str, 
                 health: int, 
                 defense,
                 evade_chance: int = 0,
                 weapon = None) -> None:
        
        self.name = name
        self.health = health
        self.max_health = health
        self.defense = defense
        self.evade_chance = evade_chance
        self.weapon = weapon
        self.life_bar = LifeBar(self, color = "")
        

    @property
    def alive(self) -> bool:
        return self.health > 0
    
    def evade(self) -> bool:
        rolled_evade = randint(1, 100)
        return self.evade_chance >= rolled_evade
        

    def attack(self, target) -> None:
        if not self.alive:
            input(f'{self.name} has fallen in battle...\n')
            return

        if target.evade():
            input(f'{self.name} missed the attack!\n')
            return 

        if self.name == 'hero':
            if self.weapon.wear == 0:
                   return input("You can't use this weapon!\n")
           
            elif self.weapon.wear != 0:
                self.weapon.wear -= 1
                pass
  
        damage_dealt = self.weapon.damage
        damage_dealt = round(target.defense.reduce_demage(damage_dealt))
            
        target.health -= damage_dealt
        target.health = max(target.health, 0)
        target.life_bar.update()
        input(
            f"{self.name} dealt {damage_dealt} damage to "
            f"{target.name} with {self.weapon.name}\n"
        )
        if self.weapon.distancy != "long-distance":
            recoil = target.defense.reflect_damage(damage_dealt)
            recoil_chance = probability(30)

            if recoil_chance:
                self.health -= recoil
                self.life_bar.update()
                print(f"{self.name} sufered {recoil} points of recoil")

        return damage_dealt

class Hero(Character):

    def __init__(self, 
                 name: str, 
                 health: int,
                 defense,
                 evade_chance: int,
                 weapon) -> None:
        
        super().__init__(name, health, defense, evade_chance, weapon)

        self.evade_chance = 25    
        self.life_bar = LifeBar(self, color = 'blue')
        
        self.default_weapon = self.weapon
        self.default_armour = self.defense
        
    def equip_weapon(self, weapon) -> None:
        self.weapon = weapon
        print(f'{self.name} equipped a {self.weapon.name}\n')

    def equip_armour(self, equipped_armour):
        self.armour = equipped_armour
        self.defense = self.armour
        input(f'{self.name} equiped a {self.armour.name}\n')

    def drop_weapon(self) -> None:
        input(f'{self.name} dropped a {self.weapon.name}\n')
        self.weapon = self.default_weapon
        self.weapon.wear = self.weapon.limit
        return self.weapon
    
    def drop_armour(self) -> None:
        input(f'{self.name} dropped a {self.defense.name}\n')
        self.defense = self.default_armour
        return self.defense

    def recover(self):
        if self.health < self.max_health:
            self.health += 20
            self.life_bar.update()
            
            if self.health > self.max_health:
                self.health = self.max_health
                self.life_bar.update()

    def defend(self, target):
        recoil = self.defense.reflect_damage(target.weapon.damage)
        
        target.health -= recoil
        target.life_bar.update()
        
        self.health -= (target.weapon.damage / 2)
        self.life_bar.update()

class Enemy(Character):

    def __init__(self, 
                 name: str, 
                 health: int,
                 defense: int, 
                 evade_chance: int,
                 weapon,
                 rarity) -> None:
        
        super().__init__(name, health, defense, evade_chance)

        self.rarity = rarity
        self.weapon = weapon
        self.evade_chance = 25   
        self.life_bar = LifeBar(self, color = 'red') 
        
        self.dropped_weapon = None
        self.dropped_armour = None

        self.weapon_drop_checked = False
        self.armour_drop_checked = False


    def drop_weapon(self):
        if self.weapon_drop_checked:
            return self.dropped_weapon

        self.drop_checked = True

        if probability(40):
            self.dropped_weapon = drop_weapon(self.rarity)

            if self.dropped_weapon is not None:
                print(
                    f"{self.name} dropped {self.dropped_weapon.name} -> "
                    f"{self.dropped_weapon.damage} points of damage")
                
        else:
            print(f"{self.name} didn't drop any Weapon.")

        return self.dropped_weapon
        
    def drop_armour(self):
        if self.armour_drop_checked:
            return self.dropped_armour

        self.armour_drop_checked = True

        if probability(30):
            self.dropped_armour = drop_armour(self.rarity)

            if self.dropped_armour is not None:
                print(
                    f"{self.name} dropped {self.dropped_armour.name} -> "
                    f"{int(self.dropped_armour.defense * 100)} " 
                    "points of defense\n")
        else:
            print(f"{self.name} didn't drop any Armour.\n")

        return self.dropped_armour

    def revive(self):
        self.health = self.max_health
        self.life_bar.update()
        return self.health

    
def load_enemies(filename="enemies.txt"):
    enemies_list = []
    
    with open(filename, "r", encoding="utf-8") as inline:
    
        for line in inline:
            line = line.strip()
    
            if not line:
                continue
    
            name, health, evade, rarity,\
            damage, attack, armour, defense = line.split(";")
            
            name = get_color(name, rarity)

            enemy_weapon = Weapon(get_color(attack, rarity),
                                  equipment_type='weapon',
                                  rarity=rarity,
                                  distancy='short',
                                  damage=int(damage),
                                  limit=0
                                  )
            
            enemy_armour = Armour(get_color(armour,rarity),
                                  equipment_type='armour',
                                  rarity=rarity,
                                  defense=int(defense)
                                  )
            
            enemy = Enemy(
                name=name,
                health=int(health),
                defense=enemy_armour,
                evade_chance=float(evade),
                weapon=enemy_weapon,
                rarity = rarity
            )
    
            enemies_list.append(enemy)
    
    return enemies_list

enemies = load_enemies()

def generate_enemy(stage, player):
        
    enemy_generated = []

    for enemy in enemies:
        if player.weapon.name != get_color("master-sword", 'legendary')\
           or \
           player.defense.name != get_color("pegasus-armour", "legendary"):

            if enemy.rarity == "common":
                prob_generate = probability(101 - (stage) * 3) 
                
                if prob_generate:
                    enemy_generated.append(enemy)

            elif enemy.rarity == "rare":
                prob_generate = probability(10 - (stage)) 
                
                if prob_generate:
                    enemy_generated.append(enemy)
            
            elif enemy.rarity == "elite":
                prob_generate = probability(stage * 2)
                
                if prob_generate:
                    enemy_generated.append(enemy)
            
            elif enemy.rarity == "boss":
                prob_generate = probability(0)
                
                if prob_generate:
                    enemy_generated.append(enemy)
        
        else:
            if enemy.rarity == "common":
                prob_generate = probability(0) 
    
                if prob_generate:
                    enemy_generated.append(enemy)

            elif enemy.rarity == "rare":
                prob_generate = probability(10) 
    
                if prob_generate:
                    enemy_generated.append(enemy)
            
            elif enemy.rarity == "elite":
                prob_generate = probability(80)
    
                if prob_generate:
                    enemy_generated.append(enemy)
                        
            elif enemy.rarity == "boss":
                prob_generate = probability(100)
    
                if prob_generate:
                    enemy_generated.append(enemy)

    return enemy_generated
      