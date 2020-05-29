"""
DONE BY: LEW YONG JIUN
PROGRAM DESCRIPTION: This is a simple Tic-Tac-Toe Game
"""
########################################################################
# Imports

########################################################################

########################################################################
# Constants
########################################################################
theBoard = {'1': "1", '2': "2", '3': "3", '4': "4", '5': "5", '6': "6", '7': "7", '8': "8", '9': "9"}
game_status = 0
game_round = 1
game_on = True


########################################################################
# Function
########################################################################
def game_board():
    """
    This function sets the game board settings/display configuration
    :return: Display Game Board
    """
    print("Player 1 (X)     |     Player 2 (O)")
    print("")
    print("          " + theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])
    print("          " + "-+-+-")
    print("          " + theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])
    print("          " + "-+-+-")
    print("          " + theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])
    print("")


def game_menu():
    """
    This function runs and display the game menu option
    :return: Run Game
    """
    global game_status
    print("1. Start Game    2. Close Game")
    game_option = input("Please select a Game option (1/2): ")
    print(" ")
    if game_option == "1":
        game_status = 1
        game_board()
        print("Player 1 will start first!")
    elif game_option == "2":
        exit()
    else:
        print("Invalid Game Option!")
        game_menu()

    while game_on:
        marking()

    print("Game Over")


def marking():
    """
    This function seeks for user input on index to place his/her marking
    :return: Ask for User Input
    """
    # Player 1
    if game_round % 2 == 1:
        player_input = input("Player 1. please indicate your marking by number: ")
        print("")
        if player_input.isdigit() and (int(player_input) in range(1, 10)):
            marking_check(player_input)
        else:
            print("Invalid Index, please input a valid index!")
            marking()
    # Player 2
    if game_round % 2 == 0:
        player_input = input("Player 2, please indicate your marking by number: ")
        print("")
        if player_input.isdigit() and (int(player_input) in range(1, 10)):
            marking_check(player_input)
        else:
            print("Invalid Index, please input a valid index!")
            marking()


def marking_check(player_input):
    """
    This function checks for winning condition in the game
    :param player_input: (str) User input on index to place
    :return: Game run
    """
    global game_round
    global game_on

    if theBoard[player_input] != "O" and theBoard[player_input] != "X":
        if game_round % 2 == 1:
            theBoard[player_input] = "X"
        if game_round % 2 == 0:
            theBoard[player_input] = "O"

        if winner():
            if game_round % 2 == 1:
                print("Player 1 Wins!")
                game_on = False
            else:
                print("Player 2 Wins!")
                game_on = False
        elif game_round == 9:
            print("Its a Tie! GAME OVER!")
            print("")
            game_menu()

        else:
            game_round += 1
            game_board()
    else:
        print("Spot has been taken! Please select another index")
        marking()


def winner():
    """
    This function sets the condition/configuration for winning the game
    :return: (bool) True/False
    """
    if game_round >= 5:
        return ((theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ') or
                (theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ') or
                (theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ') or
                (theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ') or
                (theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ') or
                (theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ') or
                (theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ') or
                (theBoard['7'] == theBoard['5'] == theBoard['3'] != ' '))


########################################################################
# Main
########################################################################
def main():
    """
    Main program to start run the above function for game start
    :return:
    """
    game_menu()


########################################################################

if "__main__" == __name__:
    main()
