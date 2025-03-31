from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
us_map = Turtle()
us_state = Turtle()

screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=500)
us_map.shape(image)

us_state.hideturtle()
us_state.pu()

data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()

score = 0

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{score} / 50", prompt="Enter a state:").title()

    if answer_state == "Exit":
        state_dict = {"state": state_list}
        df = pd.DataFrame(state_dict)
        df.to_csv("states_to_learn.csv")

        game_is_on = False

    elif answer_state in state_list:

        state_data = data[data.state == answer_state]
        us_state.goto(state_data.x.item(), state_data.y.item())
        us_state.write(state_data.state.item(), align="center")

        score += 1
        state_list.remove(answer_state)

    if len(state_list) == 0:
        game_is_on = False
