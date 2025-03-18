from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()

for angle in range(0, 361, 4):
    red = random.random()
    green = random.random()
    blue = random.random()

    screen.tracer(7)
    tim.pencolor(red, green, blue)
    tim.circle(100)
    tim.seth(angle)
    # screen.update()

screen.exitonclick()
