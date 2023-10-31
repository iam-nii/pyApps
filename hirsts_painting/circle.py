import random
from turtle import Turtle, Screen
from Colors import colors
import math


print([values for values in range(10)])

pen = Turtle()
pen.pu()
pen.speed("fastest")
screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)

radius = 250
num_of_dots = 44
for angel in range(10):
    for angle in range(num_of_dots):
        x_cor = radius * math.cos(angle)
        y_cor = radius * math.sin(angle)
        pen.goto(x_cor, y_cor)
        pen.dot(10, random.choice(colors))
        # print(angle)
        # print(f"x={x_cor}, y={y_cor}")
    num_of_dots -= 2
    radius -= 25


screen.exitonclick()
