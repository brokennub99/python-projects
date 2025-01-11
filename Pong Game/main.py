import turtle as t
from objects import Objects
from scoreboard import Scoreboard
from pong import Pong
from net import Net
import time


screen=t.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
#make net
net=Net()
#make pong ball
ball=Pong()
#make scoreboard obj
score=Scoreboard()
#paddle objects
r_paddle=Objects((355,0))
l_paddle=Objects((-360,0))
#check for users key input
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
#loop to keep game going
game_on=True
while game_on:
    time.sleep(ball.game_speed)
    ball.move()
    screen.update()
    #Detect collision with up & low boundary
    if ball.ycor()> 300 or ball.ycor()<-300:
        ball.bounce()
    #Detect collision with of ball with r paddle
    if ball.distance(r_paddle)<40  and ball.xcor()>340:
        ball.paddle_bounce()
    #Detect collision with of ball with l paddle
    if ball.distance(l_paddle)<45  and ball.xcor()<-345:
        ball.paddle_bounce()
    #Check if left player scores
    if ball.xcor()> 350:
        score.score_l+=1
        ball.pong_dx*=-1
        score.update_score()
        ball.refresh_ball()
    #Check if right player scores
    if ball.xcor()< -355:
        score.score_r+=1
        ball.pong_dx*=-1
        score.update_score()
        ball.refresh_ball()
    #Check if winner decided
    if score.score_l==3 or score.score_r==3:
        score.winner()
        game_on=False
screen.exitonclick()