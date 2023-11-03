from turtle import Turtle
import random

colors = ["red", "blue", "green", "yellow", "purple",  "orange", "pink", "gray"]
MOVE_DISTANCE = 10

class Cars:
    def __init__(self):
        self.game_cars = []

    def create_car(self):
        # To prevent the cars from being generated too frequently
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.game_cars.append(new_car)

    def move_car(self):
        for car in self.game_cars:
            car.backward(MOVE_DISTANCE)

    def refresh(self):
        pass
