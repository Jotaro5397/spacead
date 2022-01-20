# Text based Adventure Game
# Space Adventure Game choose the right answers in order to progress

PlayerHealth = 3
Inventory = []
import time

# Defining intro to the script extra prints are for added space
def intro():
    print()
    time.sleep(3)
    print("You press the button... You hear the sound of something powering on ")
    print("As the power comes on lights surround you  ")
    print("WHAAATTT! Where am i, You find yourself in cockpit")
    print("As you you look in front you are shocked in awe ")
    print("Am i in space?(You cans see the lights of stars as if the vail of darkness was keeping it covered")
    print()
    print("(Confused at your situation you begin think. ")
    print()
    print("Option #1: Press Buttons on the cockpit to see if anything happens. ")
    print("Option #2: Look around the ship to see if theres anything to interact with ")
    print("Option #3: Sleep ")
    print()
    # User choices for the first level
    firtsPath = input("What do you choose? (1/2/3):  ")
    if firtsPath == "1"   :
        print("You randomly press buttons on the ship ")
        print()
        print()
        print("Nothing Happens")
        Option1()
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
    print("it looks like a card can be slotted their... You think to yourself\n\n")
    secondPath = input("Enter Card Y/N?:  ")
    if secondPath.lower == "y" and "KeyCard" in Inventory :
        print("You inserted the card")
    Option3_1()





def Option2_1():
    print()

def Option2_2():
    print()

def Option3():
    print()

def Option3_1():
    print()

def Option3_2():
    print()


# Title screen
print()
print()
print("      ###########################")
print("      #                         #")
print("      #       Space Iseikia     #")
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