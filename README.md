# Guessing Game

A simple CLI (Command Line Interface) game written in Python where the player tries to guess a randomly generated number.

## Features

- **Random Number Generation**: Generates a secret number between 1 and 10.
- **Dynamic Hints**: Tells the player whether their guess is too high or too low.
- **Attempt Tracker**: Counts and displays how many attempts it took to win.
- **Input Validation**: Safely handles non-numeric inputs (like letters) without crashing.

## Technologies Used

- Python 3.x
- `random` module (built-in)

## Setup and Running

1. Open your terminal or PowerShell.
2. Navigate to the folder containing the project.
3. Run the game using Python:
   ```bash
   python guessing_game.py
   ```

## How to Play

1. The game will prompt you with: `Try to guess a number: `.
2. Enter an integer between 1 and 10.
3. Follow the hints ("slighter than random" or "greater than random") until you guess the correct number!
