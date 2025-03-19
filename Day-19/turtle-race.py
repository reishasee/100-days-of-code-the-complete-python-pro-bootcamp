from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Welcome to Turtle Race!", prompt="Which turtle will win the race? Make a bet and enter a color (red/orange/yellow/green/blue/purple): ")

y=-100
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-235, y=y)
    turtle_list.append(new_turtle)
    y+=40

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You win! The winner is the {winner} turtle.")
            else:
                print(f"You lose! The winner is the {winner} turtle.")
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)

screen.exitonclick()
