# Text based Adventure Game
# Space Adventure Game choose the right answers in order to progress


import sys
#PLayer info
PlayerStats = {"Health": 10,"Shield": 0, "Name": None}


#Ship information stored in dictionary
ShipStats = {"Ship_Shields": 100, "Ship_Integrity": 100, "Ship_Power": 100, "Ship_Weapons": 100, "Ship_Name": None}

#Inventory
Inventory = []


Ship_Interior = {"Ship_Door": 2}

class Enemyship:
    kind = "SpaceShip"


    def __init__(self, name, Affiliation,Ship_Integrity,Ship_Shield,Ship_Power,Ship_Weapons,):
        self.name = name
        self.Affiliation = Affiliation
        self.Ship_Integrity = Ship_Integrity
        self.Ship_Shields = Ship_Shield
        self.Ship_Power = Ship_Power
        self.Ship_Weapons = Ship_Weapons





# from random import randint
#
# EnemyShip = {"name": "Mowader", "Ship_Shields": 60, "Ship_Integrity": 50, Ship_Weapons: 75}




# commands(player, Goblin)

def confirm_choice():
    confirm = input("[c]Confirm or [n]No: ")
    if confirm != 'c' and confirm != 'n':
        print("\n Invalid Option. Please Enter a Valid Option.")
        return confirm_choice()
    print (confirm)
    return confirm


# Time Delay between text
import time

a = 2

b = 0.2

c = 0.08


# Game over command which will exit game
def game_over():
    print()
    print("Maybe next time!!")
    print()
    print("##############")
    print("#     END    #")
    print("##############")
    StartAgain = input("Do You want to start again...Y/N:  ")
    if StartAgain == "Y" or StartAgain == "y":
        startGame()
    elif StartAgain == "N" or StartAgain == "n":
        exit()
# Using else function as a form of error handling
    else:
        print("Not Valid Input...")
        game_over()



#if input == PlayerStats:
    #print(PlayerStats)

#if input == ShipStats:
    #print(ShipStats)

#if input == Inventory:
    #print(Inventory)





# Defining intro to the script extra prints are for added space
def intro():
    print()
    print(PlayerStats)
    print()
    time.sleep(a)
    print()
    intro1 = "~You press the button... You hear the sound of something powering on " \
             "\n~As the power comes on lights surround you \n" \
             "~WHAAATTT! Where am i, You find yourself in cockpit \n~As you you look in front you are shocked in awe..." \
             " \n~How did i get here you thinks to yourself \n~You try to find a way to open the windows or seems to be boarded up" \
             "\nConfused at your situation you begin think. \n\nOption #1: Press Buttons on the cockpit to see if anything happens. " \
             "\n\nOption #2: Look around to see if theres anything to interact with \n\nOption #3: Sleep"
    print()

    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)

    # User choices for the first level

    firtsPath = input("\n\nWhat do you choose? (1/2/3):  ")
    if firtsPath == "1"   :
        print("You randomly press buttons on the ship ")
        print()
        print()
        print("Nothing Happens")
        intro()

    elif firtsPath == "2" :
        print("You begin to look around the ship to find anything that can help you, \nas you walk around you notice a"
              " card... This could be important...")
        time.sleep(a)
        print("What would you like to do ")
        time.sleep(a)
        Nextchoice1 = input("Take the card (Y/N):  ")
        if Nextchoice1 == "y" or Nextchoice1 == "Y":
            Inventory.append("KeyCard")
            print()
            print(Inventory)
            print("KeyCard added to inventory")
        elif Nextchoice1 == "N" or Nextchoice1 == "n":
            print()
            print("You left the card")
            print(Inventory)
        Option2()
    elif firtsPath == "3":
        print()
        print()
        print("You go back to sleep")
        intro()

    else:
        print("Please pick from 1/2/3")
        intro()




def Option2():
    print("You proceed to keep walking through the hallway of the ship. ")
    time.sleep(a)
    print("when walking you come across a Door.")
    time.sleep(a)
    print("You proceed to look at it closely...")
    time.sleep(a)
    print("You notice a small console right beside it.")
    time.sleep(a)
    print("it looks like a card can be slotted their... You think to yourself")
    time.sleep(a)
    print()
    print()
    print()
    secondPath = input("Enter Card... Press Any Key:  ")
# if statement which requires the player to have fulfill the condition
    if "KeyCard" in Inventory:
        print()
        print()
        print("You Inserted KeyCard")
        Option2_1()
    elif "KeyCard" not in Inventory:
        print()
        print()
        print("You do not have a keyCard")
        print("Go back and find the KeyCard")
        Option2_2()




def Option2_1():
    print()
    time.sleep(a)
    print()
    print()
    print("You hear a sound of of pressure being released as you are shaken the doors begin to open")
    time.sleep(a)
    print("As the door opens you proceed to step inside you find your self in front of an engine")
    time.sleep(a)
    print("When coming close to engine you notice a red button... ")
    time.sleep(a)
    print("You think to yourself what could this be for ")
    time.sleep(a)
    thirdChoice = input("Do you want press the button Y/N  : ")
    if thirdChoice == "y" or thirdChoice == "Y":
        print("You pressed the button")
        Option3()

    elif thirdChoice == "N" or thirdChoice == "n":
        print("You left the button")
        Option3_1()

    else:
        print("Please Enter Valid input....Y/N")
        Option2_1()


def Option2_2():
    print()
    time.sleep(a)
    print()
    print("You go back to find the KeyCard but on your way back their is a big rumble and vibration")
    time.sleep(a)
    print("You are shaken to the floor and fall and hit your head")
    time.sleep(a)
    PlayerStats["Health"] -= 3
    print(PlayerStats)
    time.sleep(a)
    ShipStats["Ship_Shields"] -= 20
    ShipStats["Ship_Integrity"] -= 20
    print(ShipStats)
    print()
    print()
    time.sleep(a)
    print("You get up on you feet as things thrash around you ")
    time.sleep(a)
    print("You see the KeyCard get lost in the mess ")
    print()
    print()
    time.sleep(a)
    print("Confused as to what to do you come across an ultimatum")
    time.sleep(a)
    forthChoice = input("1) Do you go towards the cockpit to find out what happening even though there is no power"
                        "\n\nor\n\n2)Do you try find a a way through doors without the KeyCard... 1/2 ")
    if forthChoice == "1":
        print("You attempt to make you way towards the cockpit ")
        Option3_1()
    elif forthChoice == "2":
        print("You attempt to make you're way towards the door")
        Option3_2()
    else:
        print("Please enter valid input...")
        Option2_2()





#Key card option
def Option3():
    print()
    print()
    print("Once you press button the vail of darkness which surrounded the whole ship disappeared ")
    time.sleep(a)
    print("You turned the power on...")
    time.sleep(a)
    print("All of the sudden you hear a bang and feel a big rumble... ")
    print()
    time.sleep(a)
    ShipStats["Ship_Shields"] -= 10
    print(ShipStats)
    print()
    time.sleep(a)
    print("You were hit....")
    time.sleep(a)
    print("As the power on you can see through the window a large explosion in front of yellowish vail ")
    time.sleep(a)
    print("You're shields protected you from the damage")
    time.sleep(a)
    lastChoice = input("Press any key to run towards cockpit:   ")
    if lastChoice == "y" or lastChoice == "Y":
        print("You made you're way to the cockpit")
        Option4()

#Death
def Option3_1():
    print()
    print()
    time.sleep(a)
    print("As you make your way to cockpit you attempt to press any buttons...")
    time.sleep(a)
    print("But nothing seems to work...")
    time.sleep(a)
    print("Your ship keeps getting shot at you being unable to do anything causes you to be in a panic")
    time.sleep(a)
    print("As your unable to do nothing you and your ship are destroyed by the enemy vessel...")
    time.sleep(a)
    print("Health")
    PlayerStats["Health"] -= 10

#No keycard option
def Option3_2():
    print()
    time.sleep(a)
    print()
    print()
    print("When making you're way back to the door you notice a crow bar which has fallen off due to the vibration")
    time.sleep(a)
    nextChoice2 = input("Do you want to pick up the crow bar Y/N:  ")
    if nextChoice2 == "y" or nextChoice2 == "Y":
        Inventory.append("CrowBar")
        print(Inventory)
        print("You picked up a CowBar")
        Option4_1()
    elif nextChoice2 == "n" or nextChoice2 == "N":
        print("You left the CrowBar")



def Option4():
    print()
    print()
    time.sleep(a)
    print("From the cockpit you see all controls on the right of you can see the ship statistics")
    print(ShipStats)
    time.sleep(a)
    print()
    print()
    print("From the window you also finally see you situation... ")
    time.sleep(a)
    print("It seems that you're ambushed by an enemy ship")
    time.sleep(a)
    print()
    print()
    ShipIntroduction()



#To Option 5
def Option4_1():
    print()
    print()
    print()
    time.sleep(a)
    print("You come across the doorway ")
    time.sleep(a)
    print("In a rush you place the crowbar in a seem between the door")
    time.sleep(a)
    print()
    fithChoice = input("Press X To push the crow bar:  ")
    if fithChoice == "X" or fithChoice ==  "x":
        Ship_Interior["Ship_Door"] -= 1
        print(Ship_Interior["Ship_Door"])
        fithChoice1 = input("Press E To push crowbar:  ")
        if fithChoice1 == "E" or fithChoice1 == "e":
            Ship_Interior["Ship_Door"] -= 1
            print(Ship_Interior["Ship_Door"])
            if Ship_Interior["Ship_Door"] <= 0:
                print("Door Opened")

            Option5()
    else:
        print("Please Enter Valid Input")
        Option4_1()

def Option5():
    print()
    print()
    print()
    print("As the doors open you see a large apparatus with a big red button on the side of it ")
    thirdChoice1 = input("Do you want press the button Y/N:  ")
    if thirdChoice1 == "y" or thirdChoice1 == "Y":
        print("You pressed the button")
        Option3()

    elif thirdChoice1 == "N" or thirdChoice1 == "n":
        print("You left the button")
        Option3_1()

    else:
        print("Enter valid input")
        Option5()

def ShipIntroduction():
    print()
    time.sleep(a)
    print("As you sit in the cockpit while in ambush the ship begins to speak to you....")
    time.sleep(b)
    print("Hello in order to begin using the ship i need to know who is our Captain" )
    time.sleep(a)
    PlayerName = input("What is your name:   ")
    if input:
        PlayerStats["Name"] = PlayerName
        confirm_choice()
        print("Hello", PlayerStats["Name"], "in order to be fully booted....")
        time.sleep(a)
        print()
        ShipName = input("Please give me a name...")
        if input:
            ShipStats["Ship_Name"] = ShipName
            confirm_choice()
            print()
            time.sleep(a)
            print()
            print("Thank you i really like the name ", ShipStats["Ship_Name"])
            time.sleep(a)
            print()
            print("We seem to have an enemy trying take advantage of the ship while i was offline" )
            time.sleep(a)
            print()
            print("Assuming Battle stations")
            battle()



def battle():
    print()




def startGame():
    print()
    enterGame = input("Would you like to start the game? (Y/N):  ")
    if enterGame == "n" or enterGame == "N":
        print()
        print("This must be a dream... Let me sleep so i can wake up...\n\nYou go back to sleep...  ")
        game_over()
    elif enterGame == "y" or enterGame == "Y":
        intro()
    else:
        print("Not a Valid Input")
        print()
        print()
        startGame()





# Title screen
print("""
███████╗██████╗  █████╗  ██████╗███████╗    ██╗███████╗███████╗██╗  ██╗ █████╗ ██╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝    ██║██╔════╝██╔════╝██║ ██╔╝██╔══██╗██║
███████╗██████╔╝███████║██║     █████╗      ██║███████╗█████╗  █████╔╝ ███████║██║
╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝      ██║╚════██║██╔══╝  ██╔═██╗ ██╔══██║██║
███████║██║     ██║  ██║╚██████╗███████╗    ██║███████║███████╗██║  ██╗██║  ██║██║
╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝    ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
                                                                                  
""")
time.sleep(a)
# choice  to start game
s1 = "Whaa... What Happend? Where am I"
time.sleep(a)
print("Its too dark... But whats that green light beeping form the distance?\n\n"
      "Maybe i should press it?")
time.sleep(a)
print()
startGame()


if PlayerStats["Health"] <= 0:
    game_over()

if ShipStats["Ship_Integrity"] <= 0:
    game_over()