from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
    
        self.color("white")
        self.goto(0,260)
        self.refresh_score()
        self.hideturtle()



    def refresh_score(self):
        self.clear()

        self.write(f"Score : {self.score} Highscore : {self.highscore}", align="center",font=("Arial",24,"normal"))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt",mode='w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.refresh_score()