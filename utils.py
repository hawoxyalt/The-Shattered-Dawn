import random
from typing import List

# base being class
class Being:
    def __init__(self, name: str, health: int, attack: int, inventory: list):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = inventory
        self.current_health = health

    def __str__(self):
        return f"Being named {self.name} with {self.current_health}/{self.health} health that does {self.attack} damage with an inventory of {self.inventory}"

class Player(Being):
    def __init__(self, health, attack, inventory, level, pets=[]):
        super().__init__("Player", health, attack, inventory)
        self.level = level
        self.pets = pets
    def adopt(self, pet:Being):
        self.pets.append(pet)

class Zombie(Being):
    def __init__(self, level):
        super().__init__(f"Level {level} zombie", 10*level, 2*level, [Weapon("Zombie Fist", 3*level, 0.8, ['Punch', 'Claw'])])

# base item class
class Item:
    def __init__(self, name: str):
        self.name = name
# base weapon class
class Weapon(Item):
    def __init__(self, name: str, damage: int, accuracy: float, attacks: list):
        super().__init__(name)
        self.damage = damage
        self.accuracy = accuracy
        self.attacks = attacks
# extension for weapon
class Sword(Weapon):
    def __init__(self, name, damage, accuracy):
        super().__init__(name, damage, accuracy, attacks=["stab", "slash"]) # different attack types not yet implemented

# damage calculation function (real)
def damageCalc(thing: Being, weapon: Weapon | Sword):
    damage : int = thing.attack + weapon.damage
    return damage 

""" attack calculation (more like accuracy calculation, could be modified to
incorporate damage bonuses from levels or something) """
def attackCalc(thing: Being, weapon: Weapon | Sword):
    damage = damageCalc(thing, weapon) # calculates damage
    hitchance = random.random() # generates random number between 0 and 1
    if hitchance < weapon.accuracy: # if random number is smaller than weapon accuracy, the attack hits
        print(damage)
        return damage
    else:
        print("MISS")
        return 0
    
# end condition check
def victoryCheck(thing1: Being, thing2: Being):
    if thing2.current_health < 1: # if enemy dies
        print(f"{thing1.name} WINS with {thing1.current_health} health left.")
        return 1
    elif thing1.current_health < 1: # if player dies
        print(f"{thing2.name} WINS with {thing2.current_health} health left.")
        return 1
    else: # if i messed up the code or a tie somehow happens
        return 0

def AttackSequence(thing1_copy: Being, thing2_copy: Being):
    
    # makes copies of fight participants to avoid messing with their set healths
    thing1 = thing1_copy
    thing2 = thing2_copy

    # makes copies of fight participants'weapons to avoid messing with their inventories
    thing1_weapon = thing1.inventory[0]
    thing2_weapon = thing2.inventory[0]

    # copy of their health variables so that fights actually end
    # thing1_health = thing1.health
    # thing2_health = thing2.health

    # checking weapons are correct, uncomment if they break 
    # print(thing1_weapon.name)
    # print(thing2_weapon.name, "\n")

    end_condition = 0
    while end_condition != 1:

        # first attack: hero attacks creature 
        thing1_attack_damage = attackCalc(thing1, thing1.inventory[0])
        thing2.current_health = thing2.current_health - thing1_attack_damage

        # damage statement: first attack
        if thing1_attack_damage != 0:
            print(f"{thing2.name} took {thing1_attack_damage} from {thing1.name}'s {thing1_weapon.name}. They now have {thing2.current_health} health left.")
        else:
            print(f"{thing1.name} MISSED! {thing2.name} still has {thing2.current_health} health.")

        # end check
        end_condition = victoryCheck(thing1, thing2)
        if end_condition == 1:
            break
        
        # second attack: creature attacks human
        thing2_attack_damage = attackCalc(thing2, thing2.inventory[0])
        thing1.current_health = thing1.current_health - thing2_attack_damage

        # damage statement: second attack
        if thing2_attack_damage != 0:
            print(f"{thing1.name} took {thing2_attack_damage} from {thing2.name}'s {thing2_weapon.name}. They now have {thing1.current_health} health left. \n")
        else:
            print(f"{thing2.name} MISSED! {thing1.name} still has {thing1.current_health} health.")
        
        # end check
        end_condition = victoryCheck(thing1, thing2)
        if end_condition == 1:
            break


class ChoiceMenu:
    def __init__(self, choices:list):
        self.choices = choices
    def run(self):
        choices = [f"[{i}] {self.choices[i-1]}" for i in range(1, len(self.choices)+1)]
        while True:
            for c in choices:
                print(c)
            try:
                choice = int(input())
            except:
                print("Please enter a number.")
                continue
            if 0 < choice <= len(self.choices):
                break
            print("Please choose a valid option.")
        return choice

class Fight:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def damage(self, damaged:int, index:int, damage:int):
        if damaged == 0:
            self.team1[index].health -= damage
        else:
            self.team2[index].health -= damage
        self.completeDamage()
        
    def attack(self, being:Being):
        attackMenu = ChoiceMenu([b.name for b in self.team2])
        print('Who would you like to attack?')
        self.damage(1, attackMenu.run()-1, being.attack)
        self.completeDamage()

    def completeDamage(self):
        team1copy = self.team1
        team2copy = self.team2
        for i in range(len(self.team1)):
            if self.team1[i].health <= 0:
                print(f'{self.team1[i].name} died.')
                del team1copy[i]
        for i in range(0, len(self.team2)):
            print(i)
            if self.team2[i-1].health <= 0:
                print(f'{self.team2[i-1].name} died.')
                del team2copy[i-1]
        self.team1 = team1copy
        self.team2 = team2copy