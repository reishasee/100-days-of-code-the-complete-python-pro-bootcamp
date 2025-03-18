from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()

angle = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(7)

for _ in range(200):
    red = random.random()
    green = random.random()
    blue = random.random()
    tim.pencolor((red, green, blue))
    tim.fd(50)
    tim.seth(random.choice(angle))

screen.exitonclick()
