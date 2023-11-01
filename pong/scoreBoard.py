from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 180)
        self.write(arg=f"{self.left_score} {self.right_score}", font=FONT, align=ALIGNMENT)

    def UpdateScore(self, paddle):
        score = 0
        if paddle == "left":
            self.right_score += 1
            self.clear()
            self.write(arg=f"{self.left_score} {self.right_score}", font=FONT, align=ALIGNMENT)
            score = self.right_score
        if paddle == "right":
            self.left_score += 1
            self.clear()
            self.write(arg=f"{self.left_score} {self.right_score}", font=FONT, align=ALIGNMENT)
            score = self.left_score
        return score
