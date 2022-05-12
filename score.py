import os
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        filesize = os.path.getsize("data.txt")
        if filesize != 0 :
            with open("data.txt") as data:
                self.highest_score = int(data.read())
                self.color("white")
                self.penup()
                self.goto(0, 270)
                self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
                self.hideturtle()
        else:
            self.highest_score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def write_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highest_score}")
