from turtle import Turtle,Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.screen=Screen()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=.7, stretch_wid=.7)
        self.color("white")
        self.speed("fastest")
        self.make_food()

    def make_food(self):
        """Make food at random location"""
        self.goto(random.randint(-350,350),random.randint(-300,300))

    def bonus_food(self):
        global b_food
        b_food=Turtle()
        b_food.penup()
        b_food.shape("circle")
        b_food.shapesize(stretch_len=1, stretch_wid=1)
        b_food.color("white")
        b_food.speed("fastest")
        """Make the object appear and hide after a set time."""
        b_food.goto(random.randint(-350,350),random.randint(-300,300))  # Position the object at the center
        # Schedule the object to disappear after 2 seconds
        self.screen.ontimer(b_food.clear, 1000)