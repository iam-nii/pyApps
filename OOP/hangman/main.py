from hangmanBrain import HangmanBrain
from data import word_list
from art import logo

new_game = HangmanBrain(word_list)
print(logo)
while new_game.isGameOver():
    guess = input("Guess a letter: ").lower()
    new_game.checkIfLetterInWord(guess)
    new_game.trackLives(guess)