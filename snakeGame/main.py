from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.segments[0].xcor() >= 300 or snake.segments[0].xcor() <= -300 or snake.segments[0].ycor() >= 300 or \
            snake.segments[0].ycor() <= -300:
        game_is_on = False

    snake.move()

screen.exitonclick()
