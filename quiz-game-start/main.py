from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']

    new_question = Question(text, answer)
    question_bank.append(new_question)
brain = QuizBrain(question_bank)
while brain.stillHasQuestion():
    user_answer = brain.next_question()
    #brain.checkAnswer(user_answer)
