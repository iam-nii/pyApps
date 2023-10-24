import random
from art import logo, vs
from data import data
import os


print(logo)


def getDetails(person):
    person_details = [
        person['name'],
        person['description'],
        person['country'],
        person['follower_count']
    ]
    return person_details


_name = 0
description = 1
country = 2
follower_count = 3

notGameOver = True
score = 0

# The game should continue until the player gets it wrong.
while notGameOver:
    # Create a temporary dictionary to select a random person from the data dictionary - Store it in A
    first_person = getDetails(random.choice(data))

    # Create a temporary dictionary to select another random person from the data dictionary - Store it in B
    second_person = getDetails(random.choice(data))

    # Making sure we don't randomly select the same person
    while second_person == first_person:
        if second_person != first_person:
            second_person = second_person
        else:
            second_person = getDetails(random.choice(data))

    # Display their names
    print(f"Compare A: {first_person[_name]}, a {first_person[description]} from {first_person[country]}")
    print(vs)
    print(f"Against B: {second_person[_name]}, a {second_person[description]} from {second_person[country]}")

    A_followers = first_person[follower_count]
    B_followers = second_person[follower_count]

    invalidAns = True

    # Check for a valid response
    while invalidAns:
        # Ask "who has more followers A or B?"
        guess = input("Who has more followers? Type 'A'  or 'B': ").upper()
        #os.system('cls')
        if guess == 'A':
            if A_followers > B_followers:
                score += 1
                print(f"You are right! Current score: {score}")
            else:
                print(f"Sorry that's wrong. Final score: {score}")
                notGameOver = False
            invalidAns = False
        elif guess == 'B':
            if B_followers > A_followers:
                score += 1
                print(f"You are right! Current score: {score}")
            else:
                print(f"Sorry that's wrong. Final score: {score}")
                notGameOver = False
            invalidAns = False
        else:
            invalidAns = True