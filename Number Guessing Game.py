
import random

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")

secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    attempts = attempts + 1

    if guess < secret_number:
        print("Too Low! Try Again.")

    elif guess > secret_number:
        print("Too High! Try Again.")

    else:
        print("Congratulations! You guessed correctly!")
        print("The correct number was:", secret_number)
        print("Total attempts:", attempts)
        break

print("Thank you for playing!")
