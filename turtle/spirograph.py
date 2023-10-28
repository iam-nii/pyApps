import random
from turtle import Turtle, Screen
def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b) # This is called a tuple and is similar to a function but cannot be modified in any way.
    return rgb

def drawCircle(turtle):
    for _ in range(int(360/5)):
        turtle.color(randomColor())
        turtle.circle(50)
        current_heading = turtle.heading()
        turtle.setheading(current_heading + 5)


t = Turtle()
t.speed(0)
screen = Screen()
screen.colormode(255)

drawCircle(t)

screen.exitonclick()
