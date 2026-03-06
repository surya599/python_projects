import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Dash")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_forward,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    carmanager.createcar()
    carmanager.move_cars()
    for car in carmanager.allcars:
        if car.distance(player) < 20:
            scoreboard.gameover()
            screen.update
            game_is_on = False
    if player.is_at_finish_Line():
        player.reset_position()
        carmanager.level_up()
        scoreboard.increase_level()
    
    
    screen.update()

screen.exitonclick()

