from turtle import Turtle

class MakeTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.make_turtle()

    def make_turtle(self):
        """Make Turtle"""
        self.teleport(0,-300)
        self.color("black")
        self.shape("turtle")
        self.seth(90)

    def move_forward(self):
        """Move turtle forward"""
        self.penup()
        self.forward(10)

    def check_collision(self, cars):
        """Check if the turtle collides with any car"""
        for car in cars:
            if self.distance(car) < 25:  # Collision threshold
                return True
        return False

    def check_if_crossed(self):
        if self.ycor()>200:
            return True
        return False
    
    def update_turtle(self):
        self.reset()
        self.make_turtle()
