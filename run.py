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