from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0,260)
        self.refresh_score()
        self.hideturtle()

    def refresh_score(self):
        self.clear()
        self.write(f"Score : {self.score}",align="center",font=("Arial",24,"normal"))