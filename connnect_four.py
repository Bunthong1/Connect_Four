"""
Textual interface for playing Connect Four with two player
"""
from pprint import pprint

n_rows_ = 6
n_columns_ = 7

def init_field(rows = n_rows_ , columns = n_columns_):
    """
    Initialize field

    :param rows: number of rows
    :param columns: number of columns
    :return: list of lists
    """

    #create an 2D field array of size 6rows x 7columns
    field = [['.' for x in range(columns)] for y in range(rows)]

    #create an array of size 7 to store the number of tokens in each slot
    tokens = [0 for x in range(columns)]

    return field, tokens

def drop_token(field, col, player, symbol ={True: 'x', False: 'o'}):
    """
    Modify field with player's choice to drop a token into a specific column

    :param field: Two-dimensional object
    :param col:  Column to drop token to
    :param player: Player, whose token is dropped
    :param symbol: dictionary mapping player to token symbol
    :return: None
    """

    # loop through the field from bottom row to top in the column to drop the token to
    for i in range(n_rows_ - 1, -1, -1):
        # check the position availability
        # if yes, place the token and break out from the loop
        if field[i][col] == '.':
            field[i][col] = symbol[player]
            break

def game_is_won(field, void='.'):
    """
    Test if field indicates that one of the player has won the game

    :param field: double indexed object
    :return: bool
    """
    # ckeck for 4 identicle token in the same row
    for row in field:
        for i in range(4):
            if row[i] != void and row[i] == row[i+1] == row[i+2] == row[i+3]:
                return True


    for col in range(n_columns_):
        for i in range(3):
            # check for 4 identical tokens in the same column
            if field[i][col] != void and field[i][col] == field[i+1][col] == field[i+2][col] == field[i+3][col]:
                return True
            # check for 4 identical tokens in the forward diagnal position
            elif field[i][col] != void and field[i][col] == field[i + 1][col+1] == field[i + 2][col+2] == field[i + 3][col+3]:
                return True

    # check for 4 identical tokens in the backward diagnal position
    for col in range(n_columns_-1, -1, -1):
        for i in range(2,-1, -1):
            if field[i][col] != void and field[i][col] == field[i + 1][col-1] == field[i + 2][col-2] == field[i + 3][col-3]:
                return True

    return False

def play(field, tokens):
    """
    Play connect four starting with an initialised field and a coresponding list of token number per column

    :param field: Object with two indexable dimensions
    :param tokens: list of token numbers per row
    :return:  Winner of the game
    """

    active_player = 1

    # keep looping while no winner found
    while not game_is_won(field):

        valid = False
        while not valid:
            # exception handling
            try:
                # Ask for user's choice of column to drop the column
                column = int(input(f"Player {active_player}, please enter the column you want to drop:  "))
                # if the column not full, add one to the value in the position column in token array
                if tokens[column] < 6:
                    tokens[column] += 1
                    break
                # if the column is full, ask the player to input other column instead
                else:
                    print(" The column is full, Please try other column")

            # If user enter letter or bank, print this statement to the user
            except ValueError:
                print("Please enter the whole number only ( NO LETTER or BLANK)")

            # if the user enter the value outside the range, print out htis statement
            except IndexError:
                print("Please enter the column number in range 0 to 6")

        # if active_payer is player 1, drop "x" token (True)
        if active_player == 1:
            # input the column position and player into the drop_token() function
            drop_token(field, column, True)
            active_player = 2

        # if active_payer is player 2, drop "0" token (True)
        else:
            # input the column position and player into the drop_token() function
            drop_token(field, column, False)
            active_player = 1
        pprint(field)

    # switch the player
    if active_player == 1:
        active_player = 2
    else:
        active_player = 1

    return active_player

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # initialise the field
    field, tokens = init_field()
    # print the field to the console
    pprint(field)
    # run the play function until winner found
    winner = play(field, tokens)

    # display the winner to the cosole
    print(f"Player {winner} wins the game. Congratulations!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
