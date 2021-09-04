from random import randint #Random Integers

board = []

for x in range(7):
    board.append(["-"] * 7)


def print_board(board):
    """
    Prints the correct format for CPU the board
    """
    for row in board:
        print(" ".join(row))

print_board(board)


def location_col(board):
    """
    Generate a random column for the CPU ship.
    """
    return randint(0, len(board) - 1)

def location_row(board):
    """
    Generate a random row for the CPU ship.
    """
    return randint(0, len(board) - 1)

ship_row = location_row(board)
ship_col = location_col(board)

print(ship_col)
print(ship_row)