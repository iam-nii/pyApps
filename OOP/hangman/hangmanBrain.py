import random
from art import stages

class HangmanBrain:

    def __init__(self, word_list):
        self.word = random.choice(word_list)
        self.word_length = len(self.word)
        self.word_array = []
        self.lives = 6
        self.game_over = False

        for num in range(self.word_length):
            self.word_array.append('_')

    def checkIfLetterInWord(self, guess):
        for position in range(self.word_length):
            if self.word[position] == guess:
                if self.word_array[position] == guess:
                    print(f"You've already guessed '{guess}' :)")
                    break
                else:
                    self.word_array[position] = guess

    def trackLives(self, guess):
        if guess not in self.word:
            print(f"{guess} is not in the word, you lose a life :(")
            print(stages[self.lives])
            self.lives -= 1
        else:
            print(self.word_array)

    def isGameOver(self):
        if "_" not in self.word_array:
            print("You win!")
            self.game_over = False
        elif self.lives < 0:
            print("Game over! you lose!")
            self.game_over = False
        else:
            self.game_over = True
        return self.game_over

