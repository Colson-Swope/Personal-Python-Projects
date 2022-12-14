import turtle 

def mainGame():
    print("Insert game here")

def helpDocumentation():
    print("Insert game documentation here")

#Displays welcome message 
print("Welcome to Tic Tac Toe")

#Collects the name of both players 
playerOne = input("Player 1, please enter your name: ")
playerTwo = input("Player 2, please enter your name: ")

#Displays the welcome message with both player names 
print("Welcome,", playerOne, "and", playerTwo)

while True:
    menuOption = input("Ready to begin? Enter 'S' to start, or 'H' for help: ")

    if 'S' == menuOption:
        mainGame()
        break

    if 'H' == menuOption:
        helpDocumentation()
