import random
from turtle import Turtle, Screen


angles = [0, 90, 180, 270, 360]

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b) # This is called a tuple and is similar to a function but cannot be modified in any way.
    return rgb

def randomWalk(turtle):
    turtle.speed(0)
    turtle.pensize(15)
    for _ in range(200):
        turtle.color(randomColor())
        turtle.forward(20)
        turtle.setheading(random.choice(angles))


t = Turtle()
t.shape("turtle")

screen = Screen()
screen.colormode(255)

randomWalk(t)


screen.exitonclick()