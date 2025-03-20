from utils import *


# weapon declarations
person_sword = Sword("Person's Sword", 10, 0.5)
zombie_fist = Weapon("Rotten Fists", 5, 0.5, ["punch"])

# being declarations
person = Being("Person", 100, 20, [person_sword])
zombie = Being("Zombie", 50, 10, [zombie_fist])

# simulated attack sequence
AttackSequence(person, zombie)