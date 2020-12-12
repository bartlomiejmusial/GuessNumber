from replit import clear
import art
from random import randint

game = True
while(game):
    clear()
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'hard':
        attempts = 5
    elif difficulty == 'easy':
        attempts = 10
    else:
        print("\nIt's not one of the options!\nClick enter to start again")
        input()
        continue
    clear()
    print(art.logo)
    while(attempts > 0):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            clear()
            print(art.win)
            print(f"You got it!\nThe answer was {number}")
            break
        elif guess > number:
            print("Too high.\nGuess again")
        elif guess < number:
            print("Too low.\nGuess again.")
        attempts -= 1
    if guess != number:
        clear()
        print(art.lose)
        print(f"You've run out of guesses\nThe answer was: {number}")
    again = input("Do you want to play again? Type 'yes' or 'no': ")
    if again == 'no':
        game = False
