from turtle import Turtle
import random

FOOD_COLOR = "yellow"
FOOD_SIZE_L = 0.5
FOOD_SIZE_W = 0.5
BOUNDARY_X = -280
BOUNDARY_Y = 250

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=FOOD_SIZE_W, stretch_len=FOOD_SIZE_L)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        random_x = random.randint(BOUNDARY_X, BOUNDARY_Y)
        random_y = random.randint(BOUNDARY_X, BOUNDARY_Y)
        self.goto(x=random_x, y=random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(BOUNDARY_X, BOUNDARY_Y)
        random_y = random.randint(BOUNDARY_X, BOUNDARY_Y)
        self.goto(x=random_x, y=random_y)
