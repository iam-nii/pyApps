from turtle import Turtle

FONT = ("Courier", 18, "bold")
ALIGNMENT = "center"
POSITION = (-230, 270)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.score = 0
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def level_up(self, player):
        if player.ycor() > 300:
            self.score += 1
            self.clear()
            self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
            return True

    def game_over(self, player, car):
        if car.distance(player) < 30:
            self.goto(0, 0)
            self.write(arg="GAME OVER!", font=FONT, align=ALIGNMENT)
            return True
