# Task 5: Number Guessing Game
import random

secret = random.randint(1, 50)
attempts = 5

print("Guess the number between 1 and 50. You have 5 attempts.")

for i in range(attempts):
    guess = input(f"Attempt {i+1}: ")

    if not guess.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    guess = int(guess)

    if guess == secret:
        print("Congratulations! You guessed it right!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Sorry, you're out of attempts. The number was {secret}.")
