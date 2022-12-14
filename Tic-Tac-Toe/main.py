import turtle 
import time

#Contains code for drawing the grid 
def mainGame():
    import turtle 

    t=turtle.Pen()
    t.up()
    t.left(180)
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.down()
    t.forward(150)
    t.up()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.down()
    t.forward(150)                            
    t.up()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.down()
    t.forward(150)
    t.up()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.down()
    t.forward(150)
    
#Contains help documentation text 
def helpDocumentation():
    print("Insert game documentation here")

def A1X():
    print("Place holder")

#Displays welcome message 
print("Welcome to Tic Tac Toe")

#Collects the name of both players 
playerOne = input("Player 1, please enter your name: ")
playerTwo = input("Player 2, please enter your name: ")

#Displays the welcome message with both player names 
print("Welcome,", playerOne, "and", playerTwo)

#Contains code for the start menu 
while True:
    #Asks player to either enter S or H 
    menuOption = input("Ready to begin? Enter 'S' to start, or 'H' for help: ")

    #If the player enters "S", start the game 
    if 'S' == menuOption:
        mainGame()
        break

    #If the player enters "H", display the help documentation and start the loop again 
    if 'H' == menuOption:
        helpDocumentation()

while True: 
    print("Your turn,", playerOne)

    playeroneMove = input("What is your move?: ")

    print("Your turn,", playerTwo)

    playertwoMove = input("What is your move?: ")
    

    if "A1" == playeroneMove:
        print("You moved to A1")
    if "A2" == playeroneMove:
        print("You moved to A2")
    if "A3" == playeroneMove:
        print("You moved to A3")

    if "B1" == playeroneMove:
        print("You moved to B1")
    if "B2" == playeroneMove:
        print("You moved to B2")
    if "B3" == playeroneMove:
        print("You moved to B3")

    if "C1" == playeroneMove:
        print("You moved to C1")
    if "C2" == playeroneMove:
        print("You moved to C2")
    if "C3" == playeroneMove:
        print("You moved to C3")



    if "A1" == playertwoMove:
        print("You moved to A1")
    if "A2" == playertwoMove:
        print("You moved to A2")
    if "A3" == playertwoMove:
        print("You moved to A3")

    if "B1" == playertwoMove:
        print("You moved to B1")
    if "B2" == playertwoMove:
        print("You moved to B2")
    if "B3" == playertwoMove:
        print("You moved to B3")

    if "C1" == playertwoMove:
        print("You moved to C1")
    if "C2" == playertwoMove:
        print("You moved to C2")
    if "C3" == playertwoMove:
        print("You moved to C3")



