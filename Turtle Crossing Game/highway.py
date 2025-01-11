from turtle import Turtle,Screen

screen=Screen()
class Highway(Turtle):
    def __init__(self):
        super().__init__()
        default_y=-170
        screen.tracer(0)
        self.color("black")
        self.pensize(5)
        self.seth(180)
        self.hideturtle()
        self.teleport(370,default_y)
        for _ in range(10):
            for v in range(19):
                self.forward(20)
                self.penup()
                self.forward(20)
                self.pendown()
            default_y+=40
            self.teleport(370,default_y)
            screen.update()
