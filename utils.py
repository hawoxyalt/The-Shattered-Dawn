import random
from time import sleep as sleep
import copy

def LevelCalc(xp: int): # finds current level
    thingXP = xp
    nextLevel = 10
    level = 0
    counter = 0
    while nextLevel <= thingXP:
        level +=1
        counter += 1
        thingXP = thingXP - nextLevel
        nextLevel *= 1.1 ** counter
        nextLevel = round(nextLevel, 2)
    return level

# base being class
class Being:
    def __init__(self, name: str, health: int, attack: int, xp: int, gold: int, inventory: list):
        self.xp = xp
        self.name = name
        self.base_health = health
        self.base_attack = attack
        self.inventory = inventory
        self.current_health = health
        self.gold = gold
    
    @property
    def level(self):
        return LevelCalc(self.xp)
    
    @property
    def health(self):
        return round(self.base_health * 1.1 ** self.level, 2)
     
    @property
    def attack(self):
        return round(self.base_attack * 1.08 ** self.level, 2)

# base enemy class
class Enemy(Being):
    def __init__(self, level : int, inventory: list, name: str, health: int, attack: int):
        self.inventory = inventory
        self.name = name
        self.base_health = health
        self.current_health = health
        self.monsterLevel = level
        self.baseBaseAttack = attack
    @property
    def health(self):
        return round(self.base_health * 1.1 ** self.level, 2)
     
    @property
    def base_attack(self):
        return round(self.baseBaseAttack * 1.08 ** self.level, 2)
    @property
    def level(self):
        return self.monsterLevel

# base item class
class Item:
    def __init__(self, name: str):
        self.name = name
# base weapon class
class Weapon(Item):
    def __init__(self, name: str, damage: int, accuracy: float):
        super().__init__(name)
        self.damage = damage
        self.accuracy = accuracy
# extension for weapon
class Sword(Weapon):
    def __init__(self, name, damage, accuracy):
        super().__init__(name, damage, accuracy) # different attack types not implemented

# damage calculation function (real)
def damageCalc(thing: Being, weapon: Weapon | Sword):
    damage : int = thing.attack + weapon.damage
    return damage 

""" attack calculation (more like accuracy calculation, could be modified to
incorporate damage bonuses from levels or something) """
def attackCalc(thing: Being, weapon: Weapon | Sword, damage_modifier : float = 1.0, accuracy_modifier : float = 1.0):
    damage = damageCalc(thing, weapon) # calculates damage
    damage = damage * damage_modifier
    hitchance = random.random() # generates random number between 0 and 1
    weapon_accuracy = weapon.accuracy * accuracy_modifier
    if hitchance < weapon.accuracy: # if random number is smaller than weapon accuracy, the attack hits
        print(damage)
        return round(damage, 2)
    else:
        print("MISS")
        return 0
    
# end condition check
def victoryCheck(thing1: Being, thing2: Being):
    if thing2.current_health < 1: # if enemy dies
        print(f"{thing1.name} WINS with {thing1.current_health} health left. \n")
        return 1
    elif thing1.current_health < 1: # if player dies
        print(f"{thing2.name} WINS with {thing2.current_health} health left. \n")
        return 2
    else: # if i messed up the code or a tie somehow happens
        return 3

def AttackSequence(thing1_copy: Being, thing2_copy: Being):
    
    # makes copies of fight participants to avoid messing with their set healths
    thing1 = thing1_copy
    thing2 = thing2_copy

    thing1ALT = copy.deepcopy(thing1_copy)
    thing2ALT = copy.deepcopy(thing2_copy)

    # makes copies of fight participants'weapons to avoid messing with their inventories
    thing1_weapon = thing1.inventory[0]
    thing2_weapon = thing2.inventory[0]
    
    enemy_level = thing2.level
    print(f"A level {enemy_level} {thing2.name} is approaching")
    print(f"You draw your {thing1_weapon.name}, ready to fight.")



    # copy of their health variables so that fights actually end
    # thing1_health = thing1.health
    # thing2_health = thing2.health

    # checking weapons are correct, uncomment if they break 
    # print(thing1_weapon.name)
    # print(thing2_weapon.name, "\n")

    end_condition = 0
    while True:

        print("How do you choose to attack?")
        attack_type_menu = ChoiceMenu(["Stab", "Slash"])
        attack_type = attack_type_menu.run()

        if attack_type == 1: # stab
            attack_modifier = 1.2
            accuracy_modifier = 0.8
        elif attack_type == 2: # slash
            attack_modifier = 0.9
            accuracy_modifier = 1.2
        else:
            print("Menu didn't load")
            break

        # first attack: hero attacks creature 
        thing1_attack_damage = attackCalc(thing1, thing1.inventory[0], attack_modifier, accuracy_modifier)
        thing2.current_health = thing2.current_health - thing1_attack_damage
        if thing2.current_health < 0:
            thing2.current_health = 0
        
        print("\n"  * 100)
        # damage statement: first attack
        if thing1_attack_damage != 0 and thing1.current_health > 0:
            print(f"{thing2.name} took {thing1_attack_damage} from {thing1.name}'s {thing1_weapon.name}. They now have {thing2.current_health} health left.")
        else:
            print(f"{thing1.name} MISSED! {thing2.name} still has {thing2.current_health} health.")

        # end check no longer necessary
        #end_condition = victoryCheck(thing1, thing2)
        # if end_condition == 1:
        #    break
        
        # second attack: creature attacks human
        thing2_attack_damage = attackCalc(thing2, thing2.inventory[0])
        thing1.current_health = thing1.current_health - thing2_attack_damage
        if thing1.current_health < 0:
            thing1.current_health = 0

        # damage statement: second attack
        if thing2_attack_damage != 0 and thing2.current_health != 0:
            print(f"{thing1.name} took {thing2_attack_damage} from {thing2.name}'s {thing2_weapon.name}. They now have {thing1.current_health} health left. \n")
        else:
            print(f"{thing2.name} MISSED! {thing1.name} still has {thing1.current_health} health.")
        
        # end check
        end_condition = victoryCheck(thing1, thing2)
        if end_condition == 1:
            print(f"You have killed the {thing2.name}, with {thing1.current_health} health to spare.")
            
            xpGain = ((((thing2.level + 5) ** 1.65) * 3.5) * random.randint(85,115)) / 100
            xpGain = round(xpGain, 2)
            thing1.xp += xpGain  

            goldGain = (thing2.level + 3) * 4
            thing1.gold += goldGain   
            
            if thing1_copy.level != thing1ALT.level:
                print(f"You are now level {thing1.level}, with {remLevelCalc(thing1.xp)} to spare.")
                print(f"Your attack rose from {thing1ALT.attack} to {thing1.attack}")
                print(f"Your max health rose from {thing1ALT.health} to {thing1.health}")
            
            print(f"You gained {xpGain} experience points")
            print(f"You are level {thing1.level}, with {nextLevelCalc(thing1.xp)} until the next level")

            print(f"You gained {goldGain} gold and now have a total of {thing1.gold} gold.")

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

# menu = ChoiceMenu(["Run away", "Attack"])
# out = menu.run()
# print(out)



def remLevelCalc(xp: int): # finds xp in current level (left over after leveling up)
    thingXP = xp
    nextLevel = 10
    level = 0
    while nextLevel <= thingXP:
        level +=1
        thingXP = thingXP - nextLevel
        nextLevel *= 1.1 ** level
        nextLevel = round(nextLevel, 2)
    return round(thingXP, 2)

def nextLevelCalc(xp: int):
    level = LevelCalc(xp)
    x =  10 * 1.1 ** level
    return round(x - remLevelCalc(xp), 3)