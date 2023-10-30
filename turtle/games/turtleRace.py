from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
screen = Screen()
screen.setup(width=780, height=400)

turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-350, y=y_positions[turtle_index])
    turtles.append(new_turtle)

isRaceOn = True
winner = "none"

user_bet = screen.textinput(title="Make a bet", prompt="Who do you think will win? Enter a colour")
while isRaceOn:
    for turtle in turtles:
        if turtle.xcor() > 370:
            winner = turtle.pencolor()
            isRaceOn = False
        turtle.forward(random.randint(0, 10))

if winner == user_bet:
    print(f"You win. the {winner} turtle won the race!")
else:
    print(f"You lose. the {winner} turtle won the race")
screen.exitonclick()
