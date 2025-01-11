from turtle import Turtle

class Net(Turtle):
    def __init__(self):
        """Create Net"""
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,313)
        self.setheading(270)
        for v in range(16):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        
    