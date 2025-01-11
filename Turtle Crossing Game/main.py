import turtle as t
from objects import Objects
from scoreboard import Scoreboard
from highway import Highway
from newturtle import MakeTurtle
import time

default_speed=.1
screen=t.Screen()
score=Scoreboard()
screen.title("Turtle Crossing Game")
screen.tracer(0)
#make turtle and cars
cars=Objects(screen)
highway=Highway()
timmy=MakeTurtle()
screen.listen()
screen.onkey(timmy.move_forward,"Up")
game_on=True
while game_on:
    time.sleep(default_speed)
    cars.update()
    screen.update()
    #check if turtle is dead hahaha
    if timmy.check_collision(cars.random_cars):
        score.game_over()
        game_on=False
    #check if turtle successfully crossed the road
    if timmy.check_if_crossed():
        cars.level_up()
        score.update_level()
        timmy.update_turtle()
screen.exitonclick()