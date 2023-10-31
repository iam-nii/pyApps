from turtle import Turtle
import random



class Food(Turtle):

    def __init__(self):
        super(). __init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("red")
        self.speed("fastest")
        randomx = random.randint(-280, 280)
        randomy = random.randint(-280, 280)
        self.goto(randomx, randomy)

    def refresh(self):
        randomx = random.randint(-280, 280)
        randomy = random.randint(-280, 280)
        self.goto(randomx, randomy)