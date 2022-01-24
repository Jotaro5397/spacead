# Text based Adventure Game
# Space Adventure Game choose the right answers in order to progress

Stats = {"Health": 10,"Shield": 0 }

Inventory = []
import time

def game_over():
    print()
    print("Maybe next time!!")
    print()
    print("##############")
    print("#  You lost  #")
    print("##############")
    exit()

if Stats["Health"] <= 0:
    game_over


# Defining intro to the script extra prints are for added space
def intro():
    print()
    time.sleep(3)
    print(Stats)
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




def Option1():
    print()

def Option1_1():
    print()

def Option1_2():
    print()

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
        print("Go back and find the Keycard")
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

    elif thirdChoice == "N" or thirdChoice == "n":
        print("You left the button")
        Option2_1()




def Option2_2():
    print()
    print()
    print("You go back to find the KeyCard but on your way back their is a big rumble and vibration")
    print("You are shaken to the floor and fall and hit your head")
    Stats["Health"] -= 3
    print(Stats)
    print()
    print()
    print("You get up on you feet as things thrash around you ")
    print("You see the KeyCard get lost in the mess ")
    print()
    print()
    print("Confused as to what to do you come across an ultimatum")
    forthChoice = input("1) Do you go towards the cockpit to find out what happening even though there is no power"
                        "\n\nor 2)Do you try find a a way through doors without the KeyCard... 1/2 ")
    if forthChoice == "1":
        print("You attempt to make you way towards the cockpit ")
        Option3_1()
    elif forthChoice == "2":
        print("You attempt to make you're way towards the door")
        Option3_2()






def Option3():
    print()

def Option3_1():
    print()

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
    elif nextChoice2 == "n" or nextChoice2 == "N":
        print("You left the CrowBar")




# Title screen
print()
print()
print("      ###########################")
print("      #                         #")
print("      #       Space Man         #")
print("      #                         #")
print("      ###########################")
print()
print()
# choice  to start game
print("Whaa... What Happend? Where am I")
print("Its too dark... Buts whats that green light beeping form the distance?\n\n"
      "Maybe i should press it?")
print()
startGame = input("Would you like to start the game? (Y/N):  ")
if startGame == "n" or startGame == "N":
    print()
    print("This must be a dream... Let me sleep so i can wake up...\n\nYou go back to sleep... Maybe Next Time ")
elif  startGame == "y" or startGame == "Y":
    intro()