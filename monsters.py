from utils import *

# base zombie weapon
zombie_fist = Weapon("Rotten Fists", 5, 0.5)

# base zombie

class Zombie(Enemy):
    def __init__(self, level = 0, inventory = [zombie_fist], name = "Zombie", health = 50, attack = 10):
        super().__init__(level, inventory, name, health, attack)

zombie = Zombie(level=0)

# base skeleton weapon

skeleton_bow = Weapon("Rackety Bow", 20, 0.65)

# base skeleton

class Skeleton(Enemy):
    def __init__(self, level = 0, inventory = [skeleton_bow], name = "Skeleton", health = 75, attack = 20):
        super().__init__(level, inventory, name, health, attack)

skeleton = Skeleton(2)