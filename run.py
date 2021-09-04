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


def welcome_instructions():
    print("Welcome to battleships!")
    print("Board size: 7x7. Top left corner is row: 0, col: 0")
    print("Number of ships 1")
    print("You have 3 guesses before you lose!")
    print("Warning guessing a spot that you have already guessed will count as a turn.")


# Main game logic
welcome_instructions()
print_board(board)
for guess in range(3):
    print("Turn: " + str(guess +1))
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
    if guess == 2:
        print("Game over! You lost.")
