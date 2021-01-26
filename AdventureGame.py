#Imports
import os
import sys
from random import randrange

#For clearing the console after entering each room
clear = lambda: os.system('clear')

#Directions
North = "1 leading North"
South = "1 leading South"
East = "1 leading East"
West = "1 leading West"

#Enemy Damage info here
goblinAlive = True
monsterAlive = True

#Item
gotItem = False

#Add Health and attack info here
userHealth = 20
multiplier = 1

#Room layouts and what lies within
def room1():
    clear()
    print("You have entered Room 1")
    print("You are currently in a room with a single door " + North)
    while True:
        try:
            userInput = input("What would you like to do? Please enter North: ").lower()
            if userInput == "north":
               room2()
            else:
                print("Please enter the correct command!")
        except ValueError:
            continue

def room2():
    clear()
    print("You have entered Room 2")
    print("You enter a room with 4 doors," + North + ", " + South + ", " + East + ", and " + West)
    while True:
        try:
            userInput = input("What would you like to do? Please enter North, South, East, or West: ").lower()
            if userInput == "north":
                room6()
            elif userInput == "south":
                room1()
            elif userInput == "east":
                room3()
            elif userInput == "west":
                room4()
            else:
                print("Please enter the correct command!")
        except ValueError:
            continue

def room3():
    clear()
    print("You have entered Room 3")
    print("You enter a room with no doors except the one you came through (West)")
    while True:
        try:
            if goblinAlive == True:
                userInput = input("There is an evil Goblin in the room who has a thirst for blood. What would you like to do? Please enter Fight or West: ").lower()
                if userInput == "fight":
                    fightGoblin()
                elif userInput == "west":
                    print("You cannot escape the room without killing the Goblin...")
            else:
                userInput = input("The Goblin has been vanquished! What would you like to do? Please enter West: ").lower()
                if userInput == "west":
                    room2()
                else:
                    print("Please enter the correct command!")
        except ValueError:
            continue

def room4():
    clear()
    print("You have entered Room 4")
    print("You enter a room with 2 doors" + North + ", and " + East)
    while True:
        try:
            userInput = input("What would you like to do? Please enter North or East: ").lower()
            if userInput == "north":
                room5()
            elif userInput == "wast":
                room2()
            else:
                print("Please enter the correct command!")
        except ValueError:
            continue

def room5():
    clear()
    print("You have entered Room 5")
    print("You enter a room with 3 doors " + North+ ", " + South + ", and " + East)
    while True:
        try:
            userInput = input("What would you like to do? Please enter North, South, or East: ").lower()
            if userInput == "north":
                room9()
            elif userInput == "south":
                room4()
            elif userInput == "east":
                room6()
            else:
                print("Please enter the correct command!")
        except ValueError:
            continue

def room6():
    clear()
    print("You have entered Room 6")
    print("You enter a room with 3 doors, " + South+ ", " + East + ", and " + West)
    while True:
        try:
            userInput = input("What would you like to do? Please enter South, East, or West: ").lower()
            if userInput == "south":
                room2()
            elif userInput == "east":
                room7()
            elif userInput == "west":
                room5()
            else:
                print("Please enter the correct command!")
        except ValueError:
            continue

def room7():
    clear()
    print("You have entered Room 7")
    print("You enter a room with 2 doors, " + North + ", and "+ West)
    while True:
        try:
            userInput = input("What would you like to do? Please enter North or West: ").lower()
            if userInput == "north":
                room8()
            elif userInput == "west":
                room6()
            else:
                print("Please enter the correct command!")
        except ValueError:
            continue

def room8():
    clear()
    print("You have entered Room 8")
    print("You enter a room with no doors except the one you came through leading South")
    global gotItem
    global multiplier
    while gotItem == False:
            try:
                userInput = input("You see something an item shining in the corner of the room... What would you like to do? Please enter Item or South: ").lower()
                if userInput == "item":
                    gotItem = True
                    multiplier = 2
                    print("You feel a surge of energy enter you! You have now doubled in strength hitting for x2 damage!")
                elif userInput == "south":
                    room7()
                else:
                    print("Please enter the correct command!")
            except ValueError:
                continue
    else:
        while True:
            try:
                userInput = input("The room is now empty. What would you like to do? Please enter or South: ").lower()
                if userInput == "south":
                    room7()
                else:
                    print("Please enter the correct command!")
            except ValueError:
                continue

def room9():
    clear()
    print("You have entered Room 9")
    print("You enter a room with 2 doors, " + South + ", and " + East)
    while True:
        try:
            userInput = input("What would you like to do? Please enter South, or East: ").lower()
            if userInput == "south":
                room5()
            elif userInput == "east":
                room10()
            else:
                print("Please enter the correct command!")
        except ValueError:
            continue

def room10():
    clear()
    print("You have entered Room 10")
    print("You enter a room with 2 doors, " + North + ", and " + West)
    while True:
        try:
            if monsterAlive == True:
                userInput = input("There is a fercious Monster in the room looking to eat you... What would you like to do? Please enter Fight, West, or North: ").lower()
                if userInput == "fight":
                    fightMonster()
                elif userInput == "west":
                    print("You cannot escape the room without killing the Monster...")
                elif userInput == "north":
                    print("You cannot escape the room without killing the Monster...")
                else:
                    print("Please enter the correct command!")
            else:
                userInput = input("The Monster has been vanquished! What would you like to do? Please enter North or West: ").lower()
                if userInput == "west":
                    room2()
                elif userInput == "north":
                    room11()
                else:
                    print("Please enter the correct command!")

        except ValueError:
            continue

def room11():
    clear()
    print("You have made it out of the dungeon! YOU WIN!")
    print("Exiting game...")
    sys.exit()

def fightGoblin():
    clear()
    print("You have decided to fight the Goblin... like you had a choice...")
    goblinHealth = 10
    global goblinAlive
    global userHealth
    while goblinHealth > 0 and userHealth > 0:
        try:
            userInput = input("What would you like to do? Enter Attack: ").lower()
            if userInput == "attack":
                userAttack = userHit(randrange(-2,6))
                if userAttack > 0:
                    print("You hit the Goblin for " + str(userAttack))
                    goblinHealth -= userAttack
                    print("The Goblin has " + str(goblinHealth) + " Hit Points left")
                else:
                    print("You missed the Goblin!")
                    print("The Goblin has " + str(goblinHealth) + " Hit Points left")
                goblinAttack = userHit(randrange(-1,3))
                if goblinAttack > 0:
                    print("The Goblin attacks for " + str(goblinAttack))
                    userHealth -= goblinAttack
                    if userHealth > 0:
                        print("You have " + str(userHealth) + " Hit Points left")
                    else:
                        print("The Goblin's attack pierces your heart!")
                else: 
                    print("The Goblin's attack missed!")
                    print("You have " + str(userHealth) + " Hit Points left")
            else:
                print("Please enter the correct command!")
        except ValueError:
            continue
    if goblinHealth <= 0:
        print("You have vanguished the Goblin! Good job!")
        goblinAlive = False
        room3()
    elif userHealth <= 0:
        print("The Goblin has vanguished you! GAME OVER!")
        sys.exit()

def fightMonster():
    clear()
    print("You have decided to fight the Monster... prepare to DIE!!...")
    monsterHealth = 20
    global monsterAlive
    global userHealth
    while monsterHealth > 0 and userHealth > 0:
        try:
            userInput = input("What would you like to do? Enter Attack: ").lower()
            if userInput == "attack":
                userAttack = userHit(randrange(-2,5))
                if userAttack > 0:
                    print("You hit the Monster for " + str(userAttack))
                    monsterHealth -= userAttack
                    print("The Monster has " + str(monsterHealth) + " Hit Points left")
                else:
                    print("You missed the Monster!")
                    print("The Monster has " + str(monsterHealth) + " Hit Points left")
                monsterAttack = userHit(randrange(-5,5))
                if monsterAttack > 0:
                    print("The Monster attacks for " + str(monsterAttack))
                    userHealth -= monsterAttack
                    if userHealth > 0:
                        print("You have " + str(userHealth) + " Hit Points left")
                    else:
                        print("The Monster rips your head off chewing hungrily!")
                else:
                    print("The Monster's attack missed!")
                    print("You have " + str(userHealth) + " Hit Points left")
            else:
                print("Please enter the correct command!")
        except ValueError:
            continue
    if monsterHealth <= 0:
        print("You have vanguished the Monster! Good job!")
        monsterAlive = False
        room10()
    elif userHealth <= 0:
        print("The Monster has vanguished you! GAME OVER!")
        sys.exit()
        
def userHit(hit):
    return hit * multiplier
    
#Start Adventure text
print("Welcome to the adventure game...")
print("You're currently in a room with a single door leading North")

#Enter Room 1
fightGoblin()