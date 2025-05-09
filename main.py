from utils import *
from monsters import *
from time import sleep as sleep
import copy

if __name__ == '__main__':
    
    print("\nThe Shattered Dawn v0.0.1")
    print("© 2025 Shattered Media")
    print("\n")
    
    character_name = input("Character name: ")
    
    print(f"Welcome, {character_name}")
    
    sword_name = input("Name your sword (default is \"Bronze Sword\"): ")
    
    person_sword = Sword(sword_name, 10, 0.5)
    person = Being(character_name, 100, 20, 0, 0, [person_sword])
    
    print("Great choice!\n\n")
    print("Are you ready to fight for honor,")
    print("FOR GLORY")
    start_check = input("and for a bit of gold? (y/n): ")
    
    while start_check != "y":
        if start_check == "y":
            break
        elif start_check == "n":
            print("\n" * 100)
            print("No? oh.")
            exit()
        else:
            print("I beg your pardon?")
            start_check = input("Are you ready (y/n): ")

    print("\n Get ready for your first challenge:") 
    AttackSequence(person, zombie)
    end_game = 0
    while end_game != 1:
        print(f"You currently have {person.current_health} of {person.health} health, would you like to heal up for {(person.level - 2) * 5} gold?")
        healer_check = ChoiceMenu(["Yep", "Nope"])
        heal_check = healer_check.run()

        if heal_check == 1: # heal
            person.current_health = person.health
        elif heal_check == 2: # no heal
            print("oh well")
        else:
            print("Menu didn't load")
            break

        print("You hear more calamity coming from where the zombie came from.")
        print("Would you like to investigate it?")
        
        investigation_check = ChoiceMenu(["Yep", "Nope"])
        investigate_check = investigation_check.run()
        
        if investigate_check == 1: # 
            print("You go to investigate the noise and find a rackety skeleton.")
            print("Although he doesn't seem so friendly...")
            print("\n")
            AttackSequence(person, skeleton)
        elif investigate_check == 2: # 
            print("oh well")
        else:
            print("Menu didn't load")
            break