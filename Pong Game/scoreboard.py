from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score_l=0
        self.score_r=0
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score_left()
        self.score_right()
        
    def score_left(self):
        """Keep tally of score left"""
        self.goto(-30,250)
        self.pendown()
        self.write(f"{self.score_l}",align="right",font=("Courier",50,"bold"))
        self.penup()

    def score_right(self):
        """Keep tally of score right"""
        self.goto(30,250)
        self.pendown()
        self.write(f"{self.score_r}",align="left",font=("Courier",50,"bold"))

    def update_score(self):
        """Update score"""
        self.clear()
        self.score_left()
        self.score_right()
    
    def winner(self):
        """Announce winner"""
        self.clear()
        self.goto(0,100)
        self.write(f"Final Score",align="center",font=("Courier",30,"bold")) 
        self.goto(-25,60)
        self.write(f"Left Player:{self.score_l}",align="right",font=("Courier",30,"bold")) 
        self.goto(25,60)
        self.write(f"Right Player:{self.score_r}",align="left",font=("Courier",30,"bold")) 
        self.goto(0,0)
        if self.score_l>self.score_r:
            self.write(f"Winner:Left Player!",align="center",font=("Courier",40,"bold"))
        else:
            self.write(f"Winner:Right Player!",align="center",font=("Courier",40,"bold"))