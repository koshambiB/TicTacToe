# Tic Tac Toe in Python

This is a simple Tic Tac Toe game implemented in Python. It allows two players to play against each other and keeps track of wins, losses, and draws.

## Features:

-Two-player Tic Tac Toe game
-Tracks wins for X, O, and draws
-Option to rematch after each game

## Requirements:

**- Python 3.12.1**

## How to Play:

-Clone this repository.
-Install any required dependencies (likely none in this case).
-Run python `main.py`.
-Follow the on-screen prompts to play the game.
-After a game, choose to rematch or exit.

## Game Logic:

The game uses a board represented by two lists (xval and oval), each containing 9 elements. A value of 9 indicates an empty space, while X or O represents a marked position. The checkWin function determines the winner based on the board state.

## Code Structure:

The code is organized into several functions:

Oturn: Handles O player's turn, taking input, validating it, and updating the board.
Xturn: Similar to Oturn but for X player.
game: Main game loop that manages turns, win conditions, draws, and restarts.

## Playing the Game:

The game prompts players for their moves by asking for a position on the board (numbered 0-8). The game validates the input and updates the board accordingly. It checks for win conditions after each turn and declares a winner or draw if applicable. After a game, it asks the players if they want to rematch by entering Yes/No input. If the player chooses to exit, the game displays the number of matches each player won along with the number of draws.