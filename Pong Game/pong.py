from turtle import Turtle
import random

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        #speed of ball
        self.game_speed=.09
        #change in x direction
        self.pong_dx=10
        #change in y direction
        self.pong_dy=10
        self.make_ball()
        
        
    def make_ball(self):
        """Make ball"""
        self.shape("circle")
        self.color("white")
        self.penup()
        
    def refresh_ball(self):
        """Reset ball after a player scores"""
        self.reset()
        #reset ball speed
        self.game_speed=.09
        self.make_ball()

    def move(self):
        """Move Ball"""
        new_xcor=self.xcor()+self.pong_dx
        new_ycor=self.ycor()+self.pong_dy
        self.goto(new_xcor,new_ycor)
        
    def bounce(self):
        """Change direction if lower and upper boundary is hit"""
        self.pong_dy*=-1
    
    def paddle_bounce(self):
        """"Change direction if ball is hit by paddle"""
        #increase ball speed
        self.game_speed*=.9
        self.pong_dx*=-1
        
        


