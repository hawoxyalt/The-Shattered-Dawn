from utils import *


# weapon declarations
person_sword = Sword("Person's Sword", 10, 0.5)
zombie_fist = Weapon("Rotten Fists", 5, 0.5, ["punch"])

# being declarations
person = Player(100, 20, [person_sword], 1)
zombie = Being("Zombie", 50, 10, [zombie_fist])

# simulated attack sequence
AttackSequence(person, zombie)

choice = ChoiceMenu(["Move", "Unmove", "Attack"])
match choice.run():
    case 1:
        print("you want to move")
    case 2:
        print("you want to unmove")
    case 3:
        print("you want to attacky wacky")

person.adopt(Being("Dog", 25, 5, []))

### Make fight
fight = Fight([person] + person.pets, [Being("Zombie", 50, 10, [zombie_fist]), Zombie(2)])

fight.attack(person)
fight.attack(person)
fight.attack(person)
fight.attack(person)