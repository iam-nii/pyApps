from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor()
screen.title("Snake Game test")
screen.tracer(0) # Turning the tracer off until the update method is called

turtle = Turtle()
print(turtle.position)
new_snake = Snake()

screen.exitonclick()