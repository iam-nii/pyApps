import random
from turtle import Turtle, Screen
from Colors import colors


pen = Turtle()
pen.pu()
pen.speed("fastest")
screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
x_cor = -0
y_cor = -280

pen.goto(x_cor, y_cor)
length = 1
lines = 50

for line in range(lines):
    for _ in range(length):
        pen.dot(10, random.choice(colors))
        pen.forward(20)
    length += 2
    x_cor -= 20
    y_cor += 20
    print(length)
    print(f"{x_cor}, {y_cor}")
    pen.goto(x_cor, y_cor)
    if y_cor == 0:
        break

for line in range(lines):
    for _ in range(length):
        pen.dot(10, random.choice(colors))
        pen.forward(20)
    length -= 2
    x_cor += 20
    y_cor += 20
    print(length)
    print(f"{x_cor}, {y_cor}")
    pen.goto(x_cor, y_cor)
    if x_cor == 0:
        break
pen.hideturtle()

screen.exitonclick()