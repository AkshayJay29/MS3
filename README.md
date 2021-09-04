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
 - The user cannot see where the computers ships are placed and vice versa.
 