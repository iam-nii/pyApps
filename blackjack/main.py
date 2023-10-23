import random
from clearScreen import clear
from blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def compare(_userScore, _computerScore):
    if _userScore == _computerScore:
        return "Draw"
    elif _computerScore == 0:
        return "You lose, opponent has Blackjack "
    elif _userScore == 0:
        return "You win with a Blackjack"
    elif _userScore > 21:
        return "You went over. You lose"
    elif _computerScore > 21:
        return "Opponent went over. You win"
    elif _userScore > _computerScore:
        return "You win"
    else:
        return "You lose"

def dealCard():
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card
def calculateScore(_cards):
    """Calculates the total of all the cards in the hand"""
    if sum(_cards) == 21 and len(_cards) == 2:
        return 0

    #Replacing the Ace and taking the user below 21
    if 11 in _cards and sum(_cards) > 21:
        _cards.remove(11)
        _cards.append(1)
    return sum(_cards)

def play_game():

    print(logo)
    users_cards = []
    computers_cards = []
    isGameOver = False
    computer_score = 0
    user_score = 0

    # Setting the users and computers cards
    for _ in range(2):
        users_cards.append(dealCard())
        computers_cards.append(dealCard())

    while not isGameOver:
        user_score = calculateScore(users_cards)
        computer_score = calculateScore(computers_cards)

        print(f"Your cards: {users_cards}, current score: {user_score}")
        print(f"Computer's first card {computers_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isGameOver = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'y':
                users_cards.append(dealCard())
            else:
                isGameOver = True

    while computer_score != 0 and computer_score < 17:
        computers_cards.append(dealCard())
        computer_score = calculateScore(computers_cards)

    print(f"Your final hand: {users_cards}, final score: {user_score}")
    print(f"Computer's final hand {computers_cards}, computers final score {computer_score}")

    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()
