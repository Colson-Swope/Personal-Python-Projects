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


