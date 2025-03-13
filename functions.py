import random

# base being class
class Being:
    def __init__(self, name: str, health: int, attack: int, inventory: list):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = inventory
        self.current_health = health
# base weapon class
class Weapon:
    def __init__(self, name: str, damage: int, accuracy: float, attacks: list):
        self.name = name
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
