import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
options = ["rock", "paper", "scissors"]

play = True
while play:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice < 0 or user_choice > 2:
        print("You typed an invalid number, you lose!")
    else:
        print(game_images[user_choice])
        computer_choice = random.randint(0, 2)
        print(f"Computer chose {options[computer_choice]}")
        print(game_images[computer_choice])

        if computer_choice > user_choice:
            if user_choice == 0 and computer_choice != 1:
                print("You win!")
            else:
                print("You lose!")
        elif user_choice > computer_choice:
            if computer_choice == 0 and user_choice != 1:
                print("You lose!")
            else:
                print("You win!")
        elif user_choice == computer_choice:
            print("It's a draw")

    end_game = input("Do you want to play again? yes or no: ")
    if end_game == "yes":
        play = True
    elif end_game == "no":
        print("Thanks for playing :)")
        play = False