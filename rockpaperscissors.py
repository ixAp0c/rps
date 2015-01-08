from rps_module import *
import random
import getpass
import time

# First, we initialize all variables/choices to 0/False, for further assignment
# with if/else logic depending on number of players.  The user is then prompted 
# number of players, followed by the display of choices of shapes.  If there is
# 1 player, then the user is asked for his selection, and the computer's choice
# is randomly assigned, and both the userChoice and computerChoice are passed
# to the gameState() and print_results().  If there are two players, both
# are prompted for input, and then the input values are passed to gameState()
# and print_results() accordingly. The update_score() function is independent
# of the scores and uses the gameState's value to update the winner's score.
# Once the game is over, the user is asked if they want to play again, and
# program loops accordingly.
def main():
    # Values for the shapes players use, and the verbs for each
    # shape for use in output.
    shapes = ['Rock', 'Paper', 'Scissors']
    actions = ['crushes', 'covers', 'cuts']
    # Set generic values for user/computer choices/gameState, to assign 
    # within if/else statements depending on player count
    userChoice = 0
    computerChoice = 0
    userOneChoice = 0
    userTwoChoice = 0
    gameState = 0
    # Prompt user for number of players
    playerCount = player_selection()
    time.sleep(1)
    # Set continueGame to True, and then run first loop of program.
    continueGame = True
    while continueGame == True:
        # Display game's first output - shapes for user(s) to choose from.
        display_choices(shapes)
        time.sleep(1)
        # For one player, computer generates second choice at random.
        if playerCount == 1:
            userChoice = choice_selection()
            computerChoice = random.randrange(len(shapes))
            gameState = calculate_winner(userChoice, computerChoice)
            print_results(gameState, shapes, actions, userChoice, 
                            computerChoice)
            update_score(gameState)
        # For two players, both users are prompted for input
        elif playerCount == 2:
            userOneChoice = choice_selection()
            userTwoChoice = choice_selection()
            gameState = calculate_winner(userOneChoice, userTwoChoice)
            print_results(gameState, shapes, actions, userOneChoice, 
                            userTwoChoice)
            update_score(gameState)
        time.sleep(1)
        # Prompt user whether they want to play again
        continueGame = continue_game()

# This makes sure everything isn't run on imports, for module re-use
if __name__ == '__main__':
    main()

