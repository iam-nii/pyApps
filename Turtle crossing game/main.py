from turtle import Screen
from turtle_player import Player
from score_board import ScoreBoard
from cars import Cars
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score_board = ScoreBoard()
car_manager = Cars()

screen.listen()
screen.onkeypress(player.Move, "Up")
game_speed = 0.1
game_on = True
while game_on:

    time.sleep(game_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # remove the car from the list if it goes off the screen
    for car in car_manager.game_cars:
        if car.xcor() < -350:
            del car

    # check if the player got to the other side of the screen
    if score_board.level_up(player):
        player.refresh()
        game_speed *= 0.9

    # Check for collision between the car and player
    for car in car_manager.game_cars:
        if score_board.game_over(player=player, car=car):
            play_again = screen.textinput(title="Game Over", prompt="Do you want to play again?").lower()
            if play_again == "yes":
                game_speed = 0.1
                score_board.new_game()
                player.refresh()
                game_on = True
            else:
                game_on = False


screen.exitonclick()