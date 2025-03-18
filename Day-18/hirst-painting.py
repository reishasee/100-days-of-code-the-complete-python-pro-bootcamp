import colorgram
from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()
screen.colormode(255)
tim.speed("fastest")

x_coor = -200
y_coor = -150
dot_dist = 30

tim.ht()
tim.pu()
tim.goto(x_coor, y_coor)

num_of_colors = 17
colors_obj = colorgram.extract("hirst-painting-dot-artwork.jpeg", num_of_colors)
color_list = []

for color in colors_obj:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    color_tuple = (r,g,b)
    color_list.append(color_tuple)

for y in range(10):
    tim.setx(x_coor)
    tim.sety(y_coor)
    for i in range(10):
        random_color = random.choice(color_list)
        tim.dot(15, random_color)
        tim.fd(dot_dist)

    y_coor += dot_dist

screen.exitonclick()
