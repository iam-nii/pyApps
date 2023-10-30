from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.food = Turtle("circle")
        self.food.color("white")
        self.food.pu()
        self.food.shapesize(0.6)
        self.x_cor = random.randint(0, 290)
        self.y_cor = random.randint(0, 290)
        self.position = (self.x_cor, self.y_cor)
        self.food.goto(self.position)
