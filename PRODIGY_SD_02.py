#Create a Guessing Game

#Build a program that generates a random number and challenges the user to guess it. The program should prompt the user to input their guess, compare it to the generated number, and provide feedback if the guess is too high or too low. It should continue until the user correctly guesses the number and then display the number of attempts it took to win the game.

import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    attempts = 0
    guess = None

    print("Welcome to the Guessing Game!")

    while guess != secret_number:
        try:
            # Prompt the user to input their guess
            guess = int(input("Enter your guess (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Compare the guess to the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")

if __name__ == "__main__":
    guessing_game()
