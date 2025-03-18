from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

import random

for n in range(3, 11):
    angle = -360/n
    red = random.random()
    green = random.random()
    blue = random.random()
    tim.pencolor((red, green, blue))
    for _ in range(n):
        tim.fd(100)
        tim.seth(angle)
        angle -= 360/n

screen.exitonclick()
