from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.allcars = []
        self.carspeed = STARTING_MOVE_DISTANCE
    def createcar(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.allcars.append(new_car)
    def move_cars(self):
        for car in self.allcars:
            car.backward(self.carspeed)
    def level_up(self):
        self.carspeed = self.carspeed + MOVE_INCREMENT
        
