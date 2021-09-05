#Import function to generate random integers
from random import randint 

board = []
computer_board = []

for x in range(7):
    """
    Generates the size of the playing board
    """
    board.append(["-"] * 7)
    computer_board.append(["_"] * 7)

def p_board(board):
    """
    Formats the correct layout for the player's board
    """
    for row in board:
        print(" ".join(row))

def c_board(computer_board):
    """
    Formats the correct layout for the computer's board
    """
    for row in computer_board:
        print(" ".join(row))

def print_boards():
    print("Players Board:")
    p_board(board)
    print(" ")
    print("Computers Board:")
    c_board(computer_board)


def location_col(board):
    """
    Generate a random column for the computer's ship
    """
    return randint(0, len(board) - 1)

def location_row(board):
    """
    Generate a random row for the computer's ship
    """
    return randint(0, len(board) - 1)

def cpu_location_row(computer_board):
    """
    Generate a random column for the player's ship
    """
    return randint(0, len(computer_board) - 1)

def cpu_location_col(computer_board):
    """
    Generate a random row for the player's ship
    """
    return randint(0, len(computer_board) - 1)


ship_row = location_row(board)
ship_col = location_col(board)


def welcome_instructions():
    print("Welcome to battleships!")
    print("Board size: 7x7. Top left corner is row: 0, col: 0")
    print("Number of ships 1")
    print("You have 3 guesses before you lose!")
    print("Warning guessing a spot that you have already guessed will count as a turn.\n")


# Main game logic
welcome_instructions()
print_boards()
for guess in range(3):
    print("Turn: " + str(guess +1))
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "X"
        print("Congratulations! You sank my battleship!")
        print_boards()
        guess =+1
        break
    else:
        if guess_row not in range(7) or guess_col not in range(7):
            print("Oops, value is not in range")
            print_boards()
        elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "O":
            print("You already fired here")
            print_boards()
        else:
            board[guess_row][guess_col] = "O"
            print("You missed!")
            print_boards()
            guess =+1
    if guess == 2:
        print("Game over! You lost.")
