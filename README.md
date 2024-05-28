# Tic Tac Toe in Python

This is a simple Tic Tac Toe game implemented in Python. It allows two players to play against each other and keeps track of wins, losses, and draws.

## Features:

-Two-player Tic Tac Toe game <br/>
-Tracks wins for X, O, and draws <br/>
-Option to rematch after each game <br/>

## Requirements:

**- Python 3.12.1**

## How to play

-To get started [Clone the repository](https://github.com/git-guides/git-clone) to a convenient location on your local machine. <br/>
You can run the following command on your terminal:

```shell
git clone https://github.com/koshambiB/TicTacToe.git
```
-Run the command `python main.py`  on your terminal.<br/>
-Follow the on-screen prompts to play the game.<br/>
-After a game, choose to rematch or exit.<br/>

## Game Logic:

The game uses a board represented by two lists (xval and oval), each containing 9 elements. A value of 9 indicates an empty space, while X or O represents a marked position. The checkWin function determines the winner based on the board state.

## Code Structure:

The code is organized into several functions:

**Oturn**: Handles O player's turn, taking input, validating it, and updating the board. <br/>
**Xturn**: Handles X player's turn, taking input, validating it, and updating the board. <br/>
**game**: Main game loop that manages turns, win conditions, draws, and restarts.

## Playing the Game:

The game prompts players for their moves by asking for a position on the board (numbered 0-8). The game validates the input and updates the board accordingly. It checks for win conditions after each turn and declares a winner or draw if applicable. After a game, it asks the players if they want to rematch by entering Yes/No input. If the player chooses to exit, the game displays the number of matches each player won along with the number of draws.

## Note from author
I'm actively expanding the capabilities of this project by introducing exciting new features to enhance the functionality and user experience of this project.<br/>
These include:

**Implementation of Multiple Game Modes:** I am currently developing additional game modes to provide users with greater flexibility. This will allow players to choose between competing against AI or engaging in head-to-head competition with another player.<br/>
**Dedicated Website Development:** A dedicated website is under development. This website will further enhance the user experience.
<br/>
This project is a work in progress, and I'm always open to valuable contributions.