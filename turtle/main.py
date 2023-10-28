from turtle import Turtle, Screen
import random

# import turtle as t ...this is another way to import a module

shapes = {
    'TRIANGLE': 3,
    'SQUARE': 4,
    'PENTAGON': 5,
    'HEXAGON': 6,
    'OCTAGON': 8,
    'NONAGON': 9,
    'DECAGON': 10,
}
colors = ["peru", "dark orange", "orchid", "indigo", "lime", "light blue", "slate gray", "gold", "dark red", "pink",
          "old lace"]
index = 0


def drawShape(turtle, shape):
    global index
    sides = shapes[shape.upper()]
    angle = 360 / sides
    turtle.color(colors[index])

    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)
    turtle.color(colors[index])
    index += 1
    if index > len(colors):
        index = 0


t = Turtle()
t.shape("turtle")

# drawSquare(t)

# drawShape(t, "triangle")
# drawShape(t, "square")
# drawShape(t, "pentagon")
# drawShape(t, "hexagon")
# drawShape(t, "octagon")
# drawShape(t, "nonagon")
# drawShape(t, "decagon")

# for _ in range(15):
#     t.forward(10)
#     t.pu()
#     t.forward(10)
#     t.pd()


new_screen = Screen()
new_screen.exitonclick()
