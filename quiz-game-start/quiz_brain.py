class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.list_of_questions = question_list

    def next_question(self):
        current_question = self.list_of_questions[self.question_number]
        self.question_number += 1 # So that the questions start from 1 and not 0
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.checkAnswer(user_answer)

    def checkAnswer(self, user_answer):
        item = self.list_of_questions[self.question_number]
        answer = item.answer

        if answer.lower() == user_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's incorrect :(")

        print(f"The answer was: {answer}")
        print(f"Your score is {self.score}/{self.question_number}")

    def stillHasQuestion(self):
        if self.question_number == len(self.list_of_questions):
            return False
        else:
            return True
        # A simpler way is to just do this:
        # return self.question_number < len(self.list_of_questions)
