class Cell(object):
    def __init__(self, is_mine, is_visible=False, is_flagged=False):
        ''' Set attributes to the class Cell
        Our attributes should tell us if it is visible, if its flagged, and if its visible'''

        ''' After your attributes, define and implement your setters'''


class Board(tuple):
    def __init__(self, tup):
        super().__init__()
        self.is_playing = True

    def mine_repr(self):  # add parameters if needed
        """
        Returns the character that will represent the cell.
        row ID and col ID are provided to the function.
        """
        return "TO-DO"

    def __str__(self):  # add parameters if needed
        """
        Prints the board to the console. Is automatically run when the print() commmand takes a board as a parameter.
        """
        return 'TO-DO'

    def show(self):  # add parameters if needed
        """
        Makes a cell visible, given the right conditions.
        """
        return 'TO-DO'

    def flag(self):  # add parameters if needed
        """
        Flags/unflags a cell if it has not been made visible by the user.
        Also handles edge cases when there are zero remaining mines.
        """
        return 'TO-DO'

    def place_mine(self):  # add parameters if needed
        """
        This function sets a mine in a cell in the grid
        """
        return 'TO-DO'

    def count_surrounding(self):  # add parameters if needed
        """
        this function should return the number of surrounding mines near a cell. Add up the surrounding mines
        and display that number
        """
        return 'TO-DO'

    def get_neighbours(self):  # add parameters if needed
        """
        This function returns all neighbors of a cell
        """
        return 'TO-DO'

    def is_in_range(self):  # add parameters if needed
        """
        This function should determine if a cell's row and column are valid and in range
        """
        return 'TO-DO'

    @property
    def remaining_mines(self):  # add parameters if needed
        """
        This function checks every cell for mines. If a cell is a mine, +1 to mine count. If a cell is flagged,
        we -1 to the mine count. Return the remaining mines.
        """
        return "TO-DO"

    @property
    def is_solved(self):  # add parameters if needed
        """
        Returns whether the game is solved or not.
        """
        return "TO-DO"


def create_board(size, mines):
    """
    Creates the board given the size of the board and the number of mines in the game.
    The Board object is returned
    """
    return 'TO-DO'


def get_move(board):
    """
    Given a Board object, this method prompts the user for a move and then gets it and returns it in the form of a three-element tuple.
    First element of tuple: row ID
    Second element of tuple: column ID
    Third element of tuple: Boolean indicating if the move is to flag or not
    """
    INSTRUCTIONS = ("First, enter the column, followed by the row. To add or "
                    "remove a flag, add \"f\" after the row (for example, 64f "
                    "would place a flag on the 6th column, 4th row). Enter "
                    "your move: ")

    PROMPT_STRING = "Enter your move (for help enter \"H\"): "
    INVALID_STRING = "Invalid input. Enter your move (for help enter \"H\"): "

    return "TO-DO"


def is_valid(move_input, board):
    """
    This function returns whether the move is valid.
    """
    return "TO-DO"


def main():
    SIZE = 10
    MINES = 10
    print("TO-DO")


main()
