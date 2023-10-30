from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turning the tracer off until the update method is called

new_snake = Snake()
food = Food()
screen.listen()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)  # delay for 0.1 seconds, and refresh the screen
    new_snake.Move()
    screen.onkey(new_snake.TurnLeft, "Left")
    screen.onkey(new_snake.TurnRight, "Right")
    screen.onkey(new_snake.TurnUp, "Up")
    screen.onkey(new_snake.TurnDown, "Down")

    # Checking if the snake has hit the border
    if new_snake.snake[0].xcor() >= 300 or new_snake.snake[0].xcor() <= -300 \
            or new_snake.snake[0].ycor() >= 300 or new_snake.snake[0].xcor() <= 300:
        game_on = False

screen.exitonclick()
