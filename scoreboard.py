from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 240)
        self.level = 0
        self.update()

    def update(self):
        self.write(arg=f"level:{self.level}", font=FONT, align="center")

    def increase(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=FONT, align="center")
