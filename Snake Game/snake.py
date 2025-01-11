from turtle import Turtle

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body=[]
        self.default_x=0
        self.default_y=0
        self.snake_segment()
        self.snake_head=self.snake_body[0]

    def snake_segment(self):
        """Make smoll snake"""
        for v in range(3):
            snake=Turtle()
            snake.penup()
            snake.shape("square")
            snake.color("white")
            snake.goto(self.default_x,self.default_y)
            self.default_x-=20
            self.snake_body.append(snake)

    def add_body(self):
        """Adds body segment"""
        snake=Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(self.snake_body[len(self.snake_body)-1].xcor(),self.snake_body[len(self.snake_body)-1].ycor())
        self.snake_body.append(snake)

    def snake_move(self):
        """Moves Snake"""
        for snake in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[snake - 1].xcor()
            new_y =self.snake_body[snake - 1].ycor()
            self.snake_body[snake].setposition(new_x,new_y)
        self.snake_head.forward(20)

    def move_up(self):
        """Move up"""
        if self.snake_head.heading()!=270:
            self.snake_head.setheading(90)

    def move_down(self):
        """Move down"""
        if self.snake_head.heading()!=90:
            self.snake_head.setheading(270)

    def move_right(self):
        """Move right"""
        if self.snake_head.heading()!=180:
            self.snake_head.setheading(0)

    def move_left(self):
        """Move left"""
        if self.snake_head.heading()!=0:
            self.snake_head.setheading(180)

    def self_check(self,snake_body):
        """Check if snake eats itself. Return True if it has, otherwise False"""
        for snake in snake_body[2:len(snake_body)-1]:
            if self.snake_head.distance(snake)<20:
                return True
        return False

    def update_speed(self,current_score):
        """Increase speed every 10 points."""
        return max(0.01, 0.1 - (current_score // 10) * 0.01)

    def reset(self):
        for snake in self.snake_body:
            snake.goto(1000,1000)
        self.snake_body.clear()
        self.snake_segment()
        self.snake_head=self.snake_body[0]