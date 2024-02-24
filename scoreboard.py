from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGN = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_text()
        self.hideturtle()

    def update_text(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)
    def update_score(self):
        self.score += 1
        self.clear()
        self.update_text()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)
