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

print(ship_row)
print(ship_col)


print_board(board)
for guess in range(4):
    print("Turn: " + str(guess))
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "X"
        print("Congratulations! You sank my battleship!")
        print_board(board)
        guess =+1
        break
    else:
        if guess_row not in range(7) or guess_col not in range(7):
            print("Oops, value is not in range")
            print_board(board)
        elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "O":
            print("You already fired here")
            print_board(board)
        else:
            board[guess_row][guess_col] = "O"
            print("You missed!")
            print_board(board)
            guess =+1
