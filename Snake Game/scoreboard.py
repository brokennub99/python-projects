from turtle import Turtle




class Scoreboard(Turtle):
    def __init__(self):
        self.read_score()
        self.score=0
        self.make_score()
        

    def make_score(self):
        """Display score"""
        self.pen=Turtle()
        self.pen.penup()
        self.pen.color("lightseagreen")
        self.pen.hideturtle()
        self.pen.setpos(0,280)
        self.pen.write(f"Score:{self.score}     High Score:{self.high_score}",align="Center",font=("Times New Roman",30,"bold"))

    def update_score(self):
        """Updates Score"""
        self.score+=1
        self.pen.clear()
        self.pen.write(f"Score:{self.score}     High Score:{self.high_score}",align="Center",font=("Times New Roman",30,"bold"))

    def game_over(self):
        """Display Game over"""
        pen=Turtle()
        pen.penup()
        pen.color("coral")
        pen.hideturtle()
        pen.goto(0,0)
        pen.write("Game Over!",align="Center",font=("Times New Roman",30,"bold"))

    def reset(self):
        if self.score>self.high_score:
            self.write_score()
        self.score=0
        self.read_score()
        self.pen.clear()
        self.pen.write(f"Score:{self.score}     High Score:{self.high_score}",align="Center",font=("Times New Roman",30,"bold"))

    def read_score(self):
        """Read high score from data.txt"""
        with open("data.txt","r") as file:
            high_score=file.read()
        self.high_score=int(high_score)

    def write_score(self):
        """Write high score to data.txt"""
        with open("data.txt","w") as file:
            file.write(str(self.score))





