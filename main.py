import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
car = CarManager()
player = Player()
screen = Screen()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.listen()
screen.onkey(key="Up", fun=player.move)
screen.tracer(0)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_car()
    car.move()
    for i in car.all_cars:
        if i.distance(player) < 28:
            game_is_on = False
            score.game_over()
    if player.ycor() >= 280:
        player.level()
        car.increase()
        score.increase()

screen.exitonclick()