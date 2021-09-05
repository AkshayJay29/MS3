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
cpu_ship_row = cpu_location_row(computer_board)
cpu_ship_col = cpu_location_col(computer_board)


def welcome_instructions():
    """
    Intructions function to explain the how the game is played.
    """
    print("Welcome to battleships!")
    print("Board size: 7x7. Top left corner is row: 0, col: 0")
    print("Number of ships 1")
    print("You have 3 guesses before you lose!")
    print("Warning guessing a spot that you have already guessed will count as a turn.\n")


# Main game logic
print(cpu_ship_row)
print(cpu_ship_col)
welcome_instructions()
print_boards()
for guess in range(3):
    print("Turn: " + str(guess +1))
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    cpu_guess_row = randint(0, len(board) - 1)
    cpu_guess_col = randint(0, len(board) - 1)

    if guess_row == cpu_ship_row and guess_col == cpu_ship_col:
        computer_board[guess_row][guess_col] = "X"
        print("Congratulations! You sank my battleship!")
        guess =+1
        if cpu_guess_row == ship_row and cpu_guess_col == ship_col:
            board[cpu_guess_row][cpu_guess_col] = "X"
            print_boards()
            print(f"The computer guessed row: {cpu_guess_row}, col: {cpu_guess_col}")
            print("The computer sank your battleship!")
        else:
            board[cpu_guess_row][cpu_guess_col] = "O"
            print(f"The computer guessed row: {cpu_guess_row}, col: {cpu_guess_col}")
            print("The computer missed!")
            break
    else:
        if guess_row not in range(7) or guess_col not in range(7):
            print("Oops, value is not in range")
            print_boards()
        elif computer_board[guess_row][guess_col] == "X" or computer_board[guess_row][guess_col] == "O":
            print("You already fired here")
            print_boards()
        else:
            computer_board[guess_row][guess_col] = "O"
            print("You missed!")
            print_boards()
            if cpu_guess_row == ship_row and cpu_guess_col == ship_col:
                board[cpu_guess_row][cpu_guess_col] = "X"
                print_boards()
                print(f"The computer guessed row: {cpu_guess_row}, col: {cpu_guess_col}")
                print("The computer sank your battleship!")
            else:
                board[cpu_guess_row][cpu_guess_col] = "O"
                print(f"The computer guessed row: {cpu_guess_row}, col: {cpu_guess_col}")
                print("The computer missed!")
            guess =+1
    if guess == 2:
        print("Game over! You lost.")
