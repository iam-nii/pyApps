from turtle import Turtle
STARTING_SEGMENTS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake = []
        self.createSnake()

    def createSnake(self):
        for position in STARTING_SEGMENTS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake.append(new_segment)

    def Move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(DISTANCE)

    def TurnLeft(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def TurnRight(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def TurnDown(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def TurnUp(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
