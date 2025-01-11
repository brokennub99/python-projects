import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCORE_BOMB=[10,20,30,40,50,60,70,80,90,100]
screen=t.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
#make objects
snake=Snake()
food=Food()
score=Scoreboard()
#listen to key pressed
screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_right,"Right")
screen.onkey(snake.move_left,"Left")

game_on=True
while game_on:
    #check if needed to increase speed after every 10 increase in score
    game_speed=snake.update_speed(score.score)
    time.sleep(game_speed)
    snake.snake_move()
    screen.update()
    #check collision with wall
    if snake.snake_head.xcor()>360 or snake.snake_head.xcor()<-365 or snake.snake_head.ycor()>315 or snake.snake_head.ycor()<-315 :
        snake.reset()
        score.reset()
    #check if snake head collides with body
    if snake.self_check(snake.snake_body):
        snake.reset()
        score.reset()
    #check if snake eats food
    if snake.snake_head.distance(food)<20:
        snake.add_body()
        food.make_food()
        score.update_score()


screen.exitonclick()