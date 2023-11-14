from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    # quiz_brain: QuizBrain specifies that we are creating a param of type 'QuizBrain'
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score label
        self.score = Label(text=f"Score: {self.quiz.score}", fg="white", font=FONT)
        self.score.config(bg=THEME_COLOR, highlightthickness=0)
        self.score.grid(row=0, column=1, padx=10, pady=10)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=QuizBrain.next_question(self.quiz),
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #buttons
        correct_image = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=correct_image, highlightthickness=0, command=self.true_btn_clicked)
        self.true_btn.grid(row=3, column=0, padx=5)

        false_image = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_image, highlightthickness=0, command=self.false_btn_clicked)
        self.false_btn.grid(row=3, column=1, padx=5)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
        self.quiz.question_number += 1

    def false_btn_clicked(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def true_btn_clicked(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)
