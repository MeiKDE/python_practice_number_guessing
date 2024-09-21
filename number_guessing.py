from art import logo
import random

def greeting():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    easy_or_hard=input("Choose a difficulty level. Type 'easy' or 'hard': ")
    return easy_or_hard
def easy_level():
#Generate a random number between 1 and 100
    random_guess=random.randint(1,100)
    #print(f"Test: random nubmer is {random_guess}")
    print("You have 10 attempts to guess the number.")
    for i in range(10):
        guess_number=input("Make a guess: ")
        if int(guess_number) == random_guess:
            print(f"You got it! The answer was {random_guess}. You guessed the number in {i+1} attempts.")
            break
        elif int(guess_number) < random_guess:
            print("Too low. Guess again.") 
            print(f"Attempts left: {9-i}")
        elif int(guess_number) > random_guess:
            print("Too high. Guess again.")
            print(f"Attempts left: {9-i}")
        else:
            print("You've run out of gusses, you lose.")
            break    
def hard_level():
    #Generate a random number between 1 and 100
    random_guess=random.randint(1,100)
    #print(f"Test: random nubmer is {random_guess}")
    print("You have 5 attempts to guess the number.")
    for i in range(5):
        guess_number=input("Make a guess: ")
        if int(guess_number) == random_guess:
            print(f"You got it! The answer was {random_guess}. You guessed the number in {i+1} attempts.")
            break
        elif int(guess_number) < random_guess:
            print("Too low. Guess again.") 
            print(f"Attempts left: {4-i}")
        elif int(guess_number) > random_guess:
            print("Too high. Guess again.")
            print(f"Attempts left: {4-i}")
        else:
            print("You've run out of gusses, you lose.")
            break    
easy_or_hard=greeting()

if easy_or_hard=="easy":
    easy_level()
else: 
    hard_level()
           
