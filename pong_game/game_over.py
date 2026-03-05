from turtle import Turtle

class  GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()     
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Courier",80,"normal")) 