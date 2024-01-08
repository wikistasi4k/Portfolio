""" It is my version of the well known Crossing Game. The turtle can not only go forward, but also can turn left
and right. However, if you hit the wall, there will be a game over. This rule is set to prevent cheating
like going out of the line, going upwards and wining the level without getting hit by a car.
 Also, I have added a special power feature. On screen, there are appearing dark blue squares, which are treasures
 that allows you to win the level. To get the special power, you have to get hit by a treasure."""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from power import Power


player = Player()
screen = Screen()
car_manager = CarManager()
scoreboard = Scoreboard()
power = Power()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()
    power.special_power()
    power.move_treasure()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    if player.xcor() > 280 or player.xcor() < -280:
        game_is_on = False
        scoreboard.game_over()

    if player.ycor() > 280 or player.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for treasure in power.powers:
        if treasure.distance(player) < 20:
            game_is_on = True
            player.go_to_start()
            scoreboard.increase_level()

screen.exitonclick()
