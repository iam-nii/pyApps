# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('my_image.jpg', 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

from Colors import colors
from turtle import Turtle, Screen
import random

turtle = Turtle()
myScreen = Screen()
myScreen.colormode(255)
myScreen.title("Hirst's painting")

# Getting the turtle to start from a specific position

turtle.hideturtle()
turtle.penup()
turtle.goto(-300, -300)
turtle.showturtle()
turtle.pendown()
turtle.hideturtle()

turtle.speed("fastest")
def move(t):
    for _ in range(10):
        t.dot(20, random.choice(colors))
        t.penup()
        t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)


for _ in range(10):
    move(turtle)



myScreen.exitonclick()
