from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def Move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def Bounce_y(self):
        self.y_move *= -1

    def Bounce_x(self):
        self.x_move *= -1


    def NewGame(self):
        time.sleep(2)
        self.goto(0, 0)
        self.Bounce_x()