# Battleships

## Introduction

Welcome to my third project. This project is a simple battleships game that uses the python programming language, which runs in the terminal on Heroku.

The user will try to beat the CPU by finding all the battleships first. Each battleship is in a 1x1 spot on the board.

A live version of the game can be found [here](placeholder).

## How to play

Battleships is a simple board game that requires 2 players to play. In this case, you will be playing against the CPU.
The user will enter a value between 0-7 to set the guess the location of the ships on the board.
The user gets 3 guesses per ship, if the user has used all guesses on the first ship, the game will end.
The user will see where their ships are marked, indicated an X.
Guess on the opponents board will be marked with an O, hits are indicated by an X.
Once the user has made their guess, the CPU will automatically respond with a guess.
The user and computer will take turn guessing.
The game is finished when either the user or computer has guessed all the opponents ships, or when either player has guessed incorrectly 3 times in a row.

## Features

### Existing Features
- Random ship generation
 - The user and computer ships are generated randomly onto the board.
 - The user's ship location will be printed to the terminal at the start of the game.

[![game_start_terminal](documentation_assets/images/game_start_terminal.png)](documentation_assets/images/game_start_terminal.png)

- Play against the computer, the computer will automatically return with a guess after the users guess
- Accepts user input

[![game_turn1](documentation_assets/images/game_turn1.png)](documentation_assets/images/game_turn1.png)

- Input validation
    - You can only enter numbers/integers
    - You cannot enter values outside the grid size
    - If you enter the same coordinates twice, this counts as a turn
### Future Features
 - Add multiple battleships
 - Allow player to see their own ship on the board
 - Allow player to set grid
 - Allow player to position the ships themselves

## Testing

I have manually tested this project by the following:
- Ran the code through PEP8 validator. I initially ran into a few issues, as you can see in the image below:

However, these issues were rectified by...
- Entered incorrect inputs into the terminal to make sure the correct warning messages are appearing
- During the coding process I ran the project through the terminal each time to make sure the function im creating is working

### Bugs
#### Solved Bugs

### Remaining Bugs

### Validator Testing

## Deployment

## Credits