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

colors = [(237, 231, 234), (221, 232, 225), (208, 160, 82), (55, 89, 132), (145, 91, 40), (139, 26, 48),
          (222, 207, 105), (132, 176, 203), (45, 55, 104), (158, 46, 84), (169, 159, 40), (128, 189, 143), (84, 20, 44),
          (38, 43, 66), (187, 93, 106), (188, 138, 167), (84, 123, 182), (59, 39, 30), (79, 153, 165), (88, 157, 90),
          (195, 80, 71), (159, 201, 220), (79, 74, 43), (45, 74, 77), (59, 127, 118), (218, 176, 187), (167, 207, 165),
          (179, 188, 212), (221, 180, 169), (146, 37, 34), (46, 75, 73), (41, 63, 62)]

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
