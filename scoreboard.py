from turtle import Turtle
import os.path

FONT = ("Arial", 24, "normal")
ALIGN = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        if not os.path.exists("./data.txt"):
            with open("./data.txt", mode="w") as file:
                file.write(str(self.highscore))
        else:
            with open("./data.txt") as file:
                self.highscore = int(file.read())

        self.update_text()
        self.hideturtle()



    def update_text(self):
        self.write(f"Score : {self.score} High Score : {self.highscore}", align=ALIGN, font=FONT)
    def update_scoreboard(self):
        self.clear()
        self.update_text()

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("./data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
