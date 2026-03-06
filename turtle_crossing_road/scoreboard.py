from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,230)
        self.update_scoreboard()
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}",font=FONT,align="left")
    def gameover(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")