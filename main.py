# Text based Adventure Game
# Space Adventure Game choose the right answers in order to progress

#PLayer info
PlayerStats = {"Health": 10,"Shield": 0 }


#Ship information stored in dictionary
ShipStats = {"Ship_Shields": 100, "Ship_Integrity": 100, "Ship_Power": 100, "Ship_Weapons": 100}

#Inventory
Inventory = []


Ship_Interior = {"Ship_Door": 2}



import time

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
    time.sleep(3)
    print(PlayerStats)
    print()
    print()
    print("You press the button... You hear the sound of something powering on ")
    print("As the power comes on lights surround you  ")
    print("WHAAATTT! Where am i, You find yourself in cockpit")
    print("As you you look in front you are shocked in awe ")
    print("How did i get here you thinks to yourself ")
    print("You try to find a way to open the windows or doors but everything seems to be boarded up")
    print()
    print("(Confused at your situation you begin think. ")
    print()
    print("Option #1: Press Buttons on the cockpit to see if anything happens. ")
    print("Option #2: Look around to see if theres anything to interact with ")
    print("Option #3: Sleep ")
    print()
    # User choices for the first level

    firtsPath = input("What do you choose? (1/2/3):  ")
    if firtsPath == "1"   :
        print("You randomly press buttons on the ship ")
        print()
        print()
        print("Nothing Happens")
        intro()

    elif firtsPath == "2" :
        print("You begin to look around the ship to find anything that can help you, \nas you walk around you notice a"
              " card... This could be important...")
        print("What would you like to do ")
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
    print("You proceed to keep walking through the hallway sof the ship. ")
    print("when walking you come across a Door.")
    print("You proceed to look at it closely...")
    print("You notice a small console right beside it.")
    print("it looks like a card can be slotted their... You think to yourself")
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
    print()
    print()
    print("You hear a sound of of pressure being released as you are shaken the doors begin to open")
    print("As the door opens you proceed to step inside you find your self in front of an engine")
    print("When coming close to engine you notice a red button... ")
    print("You think to yourself what could this be for ")
    thirdChoice = input("Do you want press the button: ")
    if thirdChoice == "y" or thirdChoice == "Y":
        print("You pressed the button")
        Option3()

    elif thirdChoice == "N" or thirdChoice == "n":
        print("You left the button")
        Option2_1()

    else:
        print("Please Enter Valid input....")
        Option2_1()


def Option2_2():
    print()
    print()
    print("You go back to find the KeyCard but on your way back their is a big rumble and vibration")
    print("You are shaken to the floor and fall and hit your head")
    PlayerStats["Health"] -= 3
    print(PlayerStats)
    print()
    print()
    print("You get up on you feet as things thrash around you ")
    print("You see the KeyCard get lost in the mess ")
    print()
    print()
    print("Confused as to what to do you come across an ultimatum")
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
    print("You turned the power on...")
    print("All of the sudden you hear a bang and feel a big rumble... ")
    print()
    ShipStats["Ship_Shields"] -= 10
    print(ShipStats)
    print()
    print("You were hit....")
    print("As the power on you can see through the window a large explosion in front of yellowish vail ")
    print("You're shields protected you from the damage")
    lastChoice = input("Press any key to run towards cockpit")
    if lastChoice == "y" or lastChoice == "Y":
        print("You made you're way to the cockpit")
        Option4()


def Option3_1():
    print()
    print()
    print("As yu make your way to cockpit you attempt to press any buttons...")
    print("But nothing seems to work...")
    print("Your ship keeps getting shot at you being unable to do anything causes you to be in a panic")
    print("As your unable to do nothing you and your ship are destroyed by the enemy vessel...")
    PlayerStats["Health"] -= 10

#No keycard option
def Option3_2():
    print()
    print()
    print()
    print("When making you're way back to the door you notice a crow bar which has fallen off due to the vibration")
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
    print("From the cockpit you see all controls on the right of you can see the ship statistics")
    print(ShipStats)
    print()
    print()
    print("From the window you also finally see you situation... ")
    print("It seems that you're surrounded by a bunch of enemy ships")
    print("")




def Option4_1():
    print()
    print()
    print()
    print("You come across the doorway ")
    print("In a rush you place the crowbar in a seem between the door")
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
    else:
        print("Please Enter Valid Input")
        Option4_1()



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
print()
print()
print("      ###########################")
print("      #                         #")
print("      #       Space isekai      #")
print("      #                         #")
print("      ###########################")
print()
print()
# choice  to start game
print("Whaa... What Happend? Where am I")
print("Its too dark... Buts whats that green light beeping form the distance?\n\n"
      "Maybe i should press it?")
print()
startGame()


if PlayerStats["Health"] <= 0:
    game_over()