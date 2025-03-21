from turtle import Turtle
ALIGNMENT = "center"
FONT_SCORE = ("Courier New", 20, "normal")
FONT_GAME_OVER = ("Courier New", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT_SCORE)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, ALIGNMENT, FONT_GAME_OVER)
