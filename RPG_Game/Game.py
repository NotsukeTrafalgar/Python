import os
from random import choice
from character import Hero, Enemy, generate_enemy
from equipment import armours, weapons


hero = Hero(name = 'hero',
             health = 200,
             defense = armours[0],
             evade_chance = 30,
             weapon = weapons[0])

class Game:
         
    potions = 10
    stage = 1
    enemy_number = 1
    enemies_list = generate_enemy(stage, hero)
    
    @staticmethod
    def clear() -> None:
        os.system('cls')

    @staticmethod 
    def spawn_enemy() -> Enemy:
        Game.clear()
        
        if not Game.enemies_list:
            input(f'You won the {Game.stage}° Stage!\n')
            Game.stage += 1
            Game.enemy_number = 1
            Game.enemies_list = generate_enemy(Game.stage, hero)
            Game.potions += 1
            
        enemy = choice(Game.enemies_list)
        
        input(f'\nSpawning {enemy.name}...')
        input(f"Stage: {Game.stage}\n"
              f"Enemy: {Game.enemy_number}\n")
        Game.enemy_number += 1

        return enemy
    
    def run():
        enemy = Game.spawn_enemy()
        running = True

        while running:  
            Game.clear()

            hero.life_bar.draw()
            enemy.life_bar.draw()
    
            op = input("\nSelect:\n" 
                        "1.Attack\t2.Recover\n" 
                        "3.Defend\t4.Drop Equipement\n"
                        "5.Info  \t6.Exit\n" 
                        ">")

            match op:
                case '1':
                    hero.attack(enemy)
                    enemy.attack(hero)

                case '2':
                    if hero.health < hero.max_health and Game.potions > 0:
                            hero.recover()
                            Game.potions -= 1
                    
                    else:
                        input("You can't use a potion now!\n")
                    
                case '3':
                    hero.defend(enemy)

                case '4':
                    try:
                        drop = int(input("\nWhat do you want to drop?:\n"
                                         "1.Weapon\n"
                                         "2.Armour\n"
                                         "3.Leave\n"))
                    
                        match drop:

                            case 1:
                                op = input("Are you sure you want to drop:"
                                          f"{hero.weapon.name}?"
                                          "(y or n):").lower()
                                
                                if op == 'y' or op == 'yes':
                                    hero.drop_weapon()
                                
                                else:
                                    continue

                            case 2:
                                op = input("Are you sure you want to drop:"
                                          f"{hero.defense.name}?"
                                          "(y or n):").lower()
                                
                                if op == 'y' or op == 'yes':
                                    hero.drop_armour()
                               
                                else:
                                    continue

                            case 3:
                                continue

                    except ValueError:
                        print("Valor invalido!")
                
                case '5':
                    input(f"Name:{hero.name}\n"
                          f"Armour:{hero.defense.name}\n"
                          f"Weapon:{hero.weapon.name}\n"
                          f"Potions:{Game.potions}\n")

                case '6':
                    break

                case "_":
                    continue

            if not enemy.alive:
                    enemy.drop_weapon()
                    enemy.drop_armour()

                    if enemy.dropped_weapon is not None:
                        answer = input(
                            f"\nPick up {enemy.dropped_weapon.name}?[y/n]"
                        ).lower()

                        if answer == "y":
                            hero.equip_weapon(enemy.dropped_weapon)
                            enemy.dropped_weapon = None

                    if enemy.dropped_armour is not None:
                        answer = input(
                            f"Pick up {enemy.dropped_armour.name}?[y/n]"
                        ).lower()

                        if answer == "y":
                            hero.equip_armour(enemy.dropped_armour)
                            enemy.dropped_armour = None

                    enemy.revive()
                    Game.enemies_list.remove(enemy)
                    enemy = Game.spawn_enemy()

            running = hero.alive

        print('You lost! Game is over')

Game.run()
