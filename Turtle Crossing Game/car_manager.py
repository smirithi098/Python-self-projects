from turtle import Turtle
import random

COLORS = ["orange", "red", "yellow", "purple", "blue", "green"]
MOVE_DISTANCE = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.current_speed = 0.1

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(MOVE_DISTANCE)

    def change_speed(self):
        self.current_speed *= 0.5
