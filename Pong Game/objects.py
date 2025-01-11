from turtle import Turtle

class Objects(Turtle):
    def __init__(self,position):
        """Create Paddles"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Go up"""
        new_y=self.ycor()+40
        self.goto(self.xcor(),new_y)

    def go_down(self):
        """Go Down"""
        new_y=self.ycor()-40
        self.goto(self.xcor(),new_y)