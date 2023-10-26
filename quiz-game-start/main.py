from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']

    new_question = Question(text, answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    user_answer = quiz.next_question()

score = quiz.score
print("You've completed the quiz")
print(f"Your final score is: {score}")