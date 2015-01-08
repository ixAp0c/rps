# Rock, Paper, Scissors module - using modulo arithmetic. Difference
# of choices will always be 0 when there is a tie, and the difference 
# modulo 3 will always be 1 when Player One wins, and 2 when Player 
# Two wins.  The seemingly random newline and time.sleep() functions
# are there in order to make the output more readable for the user,
# rather than spitting out all of the information at once.
import random
import getpass
import time

# Basic display of choices for the user(s), what the user sees when
# the program starts up, and what displays everytime the user plays
# another game. Takes one argument (list of choices).
def display_choices(choiceList):
    for choiceNumber,shapeName in enumerate(choiceList):
        print '{0}. {1}'.format(choiceNumber + 1, shapeName)

# Prompt the user for the amount of players (1 or 2 players). Tests
# to see whether or not the input was within valid range, and then
# returns the integer numberOfPlayers for further logic/processing.
def player_selection():
    print '~ Welcome to Rock, Paper, Scissors ~'
    while True:
        numberOfPlayers = raw_input('Enter number of players [1-2]: ')
        try:
            numberOfPlayers = int(numberOfPlayers)
            if 1 <= numberOfPlayers <= 2:
                print # newline
                return numberOfPlayers
            else:
                print 'Invalid input, enter number of players (1 or 2).'
        except ValueError:
            print 'Invalid input, numbers only.'

# Input selection for user(s), testing for valid input.  If the 
# input is invalid, the user is prompted with a hint on the correct
# information, returns an integer value to be used as a list index.
def choice_selection():
    while True:
        selection = getpass.getpass('Choose a shape [1-3]: ')
        try:
           selection = int(selection) - 1
           if 0 <= selection <= 2:
               print # newline
               break
           else:
               print 'Valid options are 1-3.'
        except ValueError:
            print 'Numbers only, please.'
    return selection

# Calculates the winner of the game, using the modulo arithmetic method
# mentioned at the top of the file. The integer variable gameStatus
# tracks the state of the game, and is set to 0 for a tie, 1 for a win,
# and 2 for a loss.  The gameStatus is returned to the main scope of the
# program for further calculation and prompting. Takes two values, the
# shape choices from the user(s) and computer. Takes two arguments,
# the first and second user's choice.
def calculate_winner(choiceOne, choiceTwo):
    choiceDifference = choiceOne - choiceTwo
    gameStatus = 0
    if choiceDifference == 0:
        gameStatus = 0
    else:
        if (choiceDifference % 3) == 1:
            gameStatus = 1
        elif (choiceDifference % 3) == 2:
            gameStatus = 2
        else:
            print 'Error :: calculate_winner() :: notify code maintainer.'
    return gameStatus

# Prints the shapes each user chose for the users to see (similar to when
# hands are first shown in rock paper scissors), then displays the action
# between the shapes.  Takes 5 arguments - the gameState to track win/tie,
# the list of shapes, the list of verbs, and the two user choices (or user
# and computer's choice).
def print_results(gameState, shapesList, actionList, choiceA, choiceB):
    print 'Player 1:', shapesList[choiceA]
    print 'Player 2:', shapesList[choiceB], '\n'
    time.sleep(1)
    if gameState == 0:
        print 'Game is a tie.\n'
    elif gameState == 1:
        print '{0} {1} {2}.\n'.format(shapesList[choiceA],
                                    actionList[choiceA],
                                    shapesList[choiceB])
    elif gameState == 2:
        print '{0} {1} {2}.\n'.format(shapesList[choiceB],
                                    actionList[choiceB],
                                    shapesList[choiceA])
    else:
        print 'Error :: print_results() :: notify code maintainer.'

# Set global score values to be used in update_score() and main().  scoreOne
# represents player one, and scoreTwo represents player two (computer or a
# secondary user).
scoreOne = 0
scoreTwo = 0
# Updates the score values based on the state of the game, if the game is a tie
# no value is updated. If the first user wins, then scoreOne is incremented by 1,
# and if the second user/computer wins, scoreTwo is incremented by 1.
def update_score(gameState):
    global scoreOne, scoreTwo
    if gameState == 0:
        pass
    elif gameState == 1:
        scoreOne = scoreOne + 1
    elif gameState == 2:
        scoreTwo = scoreTwo + 1
    else:
        print 'Error :: update_score() :: notify code maintainer.'
    print 'Player One: ', scoreOne
    print 'Player Two: ', scoreTwo

# Prompt user whether or not they want to coninue the game, returning a boolean
# value of True or False, whether they choose 'Y' or 'N', respectively. Checks
# whether input was a string and then if it was y/n (after setting to lower case
# to make it case insensitive).  If the user's input is invalid they are asked
# again after being given a hint on correct input. 
def continue_game():
    while True:
        playAgain = raw_input('Play another game [y/n]: ')
        if isinstance(playAgain, str):
            if playAgain.lower() == 'y':
                print # newline
                return True
            elif playAgain.lower() == 'n':
                return False
            else:
                print 'Invalid input, "Y" or "N" only'
        else:
            print 'Invalid input, "Y" or "N" only.'
