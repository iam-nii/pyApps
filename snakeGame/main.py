from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.IncreaseScore()

    #Detect collision with wall
    if snake.segments[0].xcor() >= 290 or snake.segments[0].xcor() <= -290 or snake.segments[0].ycor() >= 290 or \
            snake.segments[0].ycor() <= -290:
        score.reset()
        snake.reset()
        score.write_to_file()
    snake.move()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            score.write_to_file()

screen.exitonclick()
