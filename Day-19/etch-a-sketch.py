from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.fd(10)
def backward():
    tim.bk(10)
def right():
    tim.rt(10)
def left():
    tim.lt(10)
def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=right, key="d")
screen.onkey(fun=left, key="a")
screen.onkey(fun=clear, key="c")
screen.listen()
screen.exitonclick()
