from turtle import Turtle

class Game_over(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.write("Game Over",align=("center"),font=("Arial",24,"normal"))