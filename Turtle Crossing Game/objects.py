from turtle import Turtle
import random
import time

#create turtle obj


colors=["red","yellow","black","brown1","indianRed1","blue","ForestGreen","Gold","Orange"]
highway_lane=[-150,-110,-70,-30,10,50,90,130,170]

class Objects(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        #create cars list
        self.random_cars=[]
        #car speed
        self.cars_speed=10
        self.next_spawn_time=time.time() + random.uniform(0.5, 2.0) 
        self.screen.tracer(0)

    def make_a_car(self):
        """Create Car"""
        #create car obj
        car = Turtle()
        car.shape("square")
        car.teleport(370,random.choice(highway_lane))
        car.shape("square")
        car.color(random.choice(colors))
        car.shapesize(stretch_wid=1,stretch_len=2) 
        return car

    def move_car(self):
        """Move Cars"""
        for car in self.random_cars[:]:  # Use a copy of the list to avoid issues while removing
            car.penup()
            car.backward(self.cars_speed)  # Move left at a constant speed
            if car.xcor() < -320:  # Remove car if it goes off-screen
                self.random_cars.remove(car)
                car.hideturtle()

    def spawn_car(self):
        """Spawn Car after a random delay"""
        random_chance=random.randint(1,4)
        # Check if it's time to spawn a new car
        if random_chance==1:
            self.random_cars.append(self.make_a_car())
            

    def update(self):
        """Main update loop to spawn and move cars"""
        self.spawn_car()  # Spawn a new car if needed
        self.move_car()   # Move all cars
        self.screen.update()  # Update the screen

    def level_up(self):
        """Increase car speed"""
        self.cars_speed+=5
        self.move_car()