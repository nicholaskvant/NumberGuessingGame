# Number Guessing Game in Python

import random
import time

print("*----------------------------------*")
print("Welcome to the number guessing game!")
time.sleep(1)
print("Generating random number...")
time.sleep(1)
print("Almost Done...")
time.sleep(2)
print("Random number generated! Begin Guessing")

randomNumber = random.randint(0, 10)
guesses = 0
guess = int(input("Enter your guess here: "))

while True:
    if guess == randomNumber:
        print("You guessed correctly!")
        print(f"Number Guessed: {guess}. Correct Number: {randomNumber}")
        guesses += 1
        break

    elif guess < randomNumber:
        print("Too low, try again.")
        guess = int(input("Enter your guess here: "))
        guesses += 1

    elif guess > randomNumber:
        print("Too high, try again")
        guess = int(input("Enter your guess here: "))
        guesses += 1


print(f"You got it in {guesses} guesses.")

