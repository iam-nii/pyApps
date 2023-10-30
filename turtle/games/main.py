from turtle import Turtle, Screen


tom = Turtle()
screen = Screen()

def move_forward():
    tom.forward(10)
def move_backward():
    tom.backward(10)
def turn_left():
    tom.left(10)
def turn_right():
    tom.right(10)
def clear():
    tom.clear()
    tom.pu()
    tom.home()
    tom.pd()


screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()