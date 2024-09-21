# Number Guessing Game

This is a Python-based **Number Guessing Game** where the player tries to guess a randomly generated number between 1 and 100. The game offers two difficulty levels: **easy** and **hard**.

## Features

- The computer generates a random number between 1 and 100.
- The player chooses a difficulty level:
  - **Easy**: 10 attempts to guess the number.
  - **Hard**: 5 attempts to guess the number.
- After each guess, the game provides feedback:
  - **Too low**: The guessed number is lower than the target number.
  - **Too high**: The guessed number is higher than the target number.
  - **Correct**: The guessed number matches the randomly generated number.
- The game tracks the number of remaining attempts and ends when the player either guesses the correct number or runs out of attempts.

## How to Play

1. Run the Python script.
2. The game will greet you and ask you to choose a difficulty level: **'easy'** or **'hard'**.
3. Based on your choice:
   - If you choose **easy**, you'll have 10 attempts to guess the number.
   - If you choose **hard**, you'll have 5 attempts to guess the number.
4. After each guess, the game will tell you whether your guess is too low or too high.
5. Keep guessing until you either:
   - Guess the correct number (you win!).
   - Run out of attempts (you lose!).

## Code Overview

- **`greeting()`**: 
  - Displays a welcome message and prompts the user to choose a difficulty level (easy or hard).
  
- **`easy_level(easy)`**:
  - This function runs the game in easy mode, giving the player 10 attempts to guess the number. It checks each guess and provides feedback on whether the guess was too high, too low, or correct.

- **`hard_level(hard)`**:
  - This function runs the game in hard mode, giving the player 5 attempts to guess the number. Similar to the easy level, it provides feedback on each guess.

## Example Game Play

