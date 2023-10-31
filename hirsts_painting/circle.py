import random
from turtle import Turtle, Screen
from Colors import colors
import math


pen = Turtle()
pen.pu()
pen.speed("fastest")
screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)

radius = 200
for angle in range(360):
    x_cor = radius * math.cos(angle)
    y_cor = radius * math.sin(angle)
    pen.dot(6, random.choice(colors))
    print(angle)
    print(f"x={x_cor}, y={y_cor}")


screen.exitonclick()
