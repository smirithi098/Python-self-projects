from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")

is_game_on = True
while is_game_on:
    time.sleep(car_manager.current_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False

    if player.ycor() == 280:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.change_speed()

screen.exitonclick()
