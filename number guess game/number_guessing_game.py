from random import randint
from art import logo

EASY = 10
HARD = 5

def attempts(_difficulty):
    if difficulty == "easy":
        return EASY
    elif difficulty == "hard":
        return HARD


print(logo)
print("Welcome to the Number guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

rand_number = randint(1, 100)

attempt = attempts(difficulty)

number_not_guessed = True
while number_not_guessed and attempt != 0:
    print(f"You have {attempt} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess > rand_number:
        print("Too high")
        attempt -= 1
        if attempt == 0:
            print("You've run out of guesses, you lose.")
            break
    elif guess < rand_number:
        print("Too low")
        attempt -= 1
        if attempt == 0:
            print("You've run out of guesses, you lose.")
            break
    else:
        print(f"You got it! the answer was {guess}")
        number_not_guessed = False

