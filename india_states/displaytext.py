from turtle import Turtle

class Display(Turtle):
    def __init__(self,answer,x,y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x,y)
        self.write(f"{answer}",font= ("Arial",10,"normal"),align="center")