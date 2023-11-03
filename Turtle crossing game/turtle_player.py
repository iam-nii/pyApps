# TODO create a turtle and position it at the bottom of the screen
# TODO Add user controls

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)

    def Move(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(START_POSITION)
