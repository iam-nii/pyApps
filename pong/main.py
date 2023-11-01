from turtle import Screen
from paddle import Paddle
from scoreBoard import Score
import time
from ball import Ball


# Creating the screen
screen = Screen()

# Turn off the animation and listen for events
screen.tracer(0) # Turn animation off
# Setup
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

# Creating the paddles and score board
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

score = Score()
ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.MoveUp, "Up")
screen.onkeypress(left_paddle.MoveUp, "w")
screen.onkeypress(right_paddle.MoveDown, "Down")
screen.onkeypress(left_paddle.MoveDown, "s")

_time = 0.1
GameOn = True
while GameOn:
    time.sleep(_time)
    screen.update() # Update the screen
    ball.Move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.Bounce_y()
        print(ball.distance(right_paddle))

    # Check for collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or\
            ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.Bounce_x()
        _time *= 0.9 # Increase speed of ball after each collision

    left_score = 0
    if ball.xcor() > 390:
        left_score = score.UpdateScore("right")
        ball.NewGame()
        _time = 0.1

    right_score = 0
    if ball.xcor() < -390:
        right_score = score.UpdateScore("left")
        ball.NewGame()
    if right_score == 10 or left_score == 10:
        GameOn = False
        _time = 0.1


screen.exitonclick()

#TODO - 1 Create the pong board and score sheet
#TODO - 2 Create the paddles for each player
#TODO - 3 Bind the paddles to the control keys
#TODO - 4 Create the ball and position at the center of the screen
#TODO - 5 Get the ball to move in a straight line
#TODO - 6 Detect collision between the ball and the paddles
