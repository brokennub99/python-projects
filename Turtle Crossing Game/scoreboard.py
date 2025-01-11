from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.teleport(-370,290)
        self.color("black")
        self.make_score()

    def make_score(self):
        self.write(f"Level: {self.level}",align="left", font=("Arial", 15,"bold"))

    def update_level(self):
        self.level+=1
        self.clear()
        self.make_score()
    
    def game_over(self):
        self.hideturtle()
        self.teleport(0,0)
        self.color("black")
        self.write("Game Over!",align="center",font=("Arial",30,"bold"))
        
