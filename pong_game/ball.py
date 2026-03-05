from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.xmov = 10
        self.ymov = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor()+self.xmov
        new_y = self.ycor()+self.ymov
        self.penup()
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.ymov = self.ymov * -1
    
        self.move_speed *= 0.9
    def bounce_x(self):
        self.xmov = self.xmov * -1

        self.move_speed *= 0.9
    def reset_pos(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        