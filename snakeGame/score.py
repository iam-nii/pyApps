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
        self.hideturtle()
        self.UpdateScore()

    def UpdateScore(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def IncreaseScore(self):
        self.score += 1
        self.clear()
        self.UpdateScore()

    def GameOver(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", move=False, align=ALIGNMENT, font=FONT)