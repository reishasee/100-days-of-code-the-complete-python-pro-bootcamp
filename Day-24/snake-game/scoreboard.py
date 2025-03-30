from turtle import Turtle
ALIGNMENT = "center"
FONT_SCORE = ("Courier New", 20, "normal")
FONT_GAME_OVER = ("Courier New", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, ALIGNMENT, FONT_SCORE)

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
