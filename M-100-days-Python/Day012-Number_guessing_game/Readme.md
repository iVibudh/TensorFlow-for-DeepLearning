# Number Guessing Game
This simple Python program implements a Number Guessing Game where the user tries to guess a randomly generated number between 1 and 100. The game provides different difficulty levels, and the user has a limited number of attempts to guess the correct number.

## Features
- The game has two difficulty levels: easy and hard.
- In the easy level, the player gets 10 attempts to guess the number, while in the hard level, they get 5 attempts.
- After each guess, the program provides feedback on whether the guess was too high or too low.
- If the player runs out of attempts, the game ends, and the correct answer is revealed.

## How to Play
- Run the main.py script.
- Choose the difficulty level by typing 'easy' or 'hard' when prompted.
- Guess the number when prompted and receive feedback.
- Continue guessing until you correctly identify the number or run out of attempts.

## Code Structure
- The check_answer function compares the user's guess with the actual answer and provides feedback.
- The set_difficulty function allows the user to choose between easy and hard levels, determining the number of attempts accordingly.
- The game function initializes the game, generates a random number, and handles the game loop until the user either guesses correctly or runs out of attempts.

## Dependencies
- The game uses the randint function from the random module to generate a random number.
- The game uses ASCII art from the art module for a visually appealing logo.