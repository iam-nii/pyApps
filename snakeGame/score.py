from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 18, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.UpdateScore()

    def UpdateScore(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def IncreaseScore(self):
        self.score += 1
        self.UpdateScore()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.UpdateScore()