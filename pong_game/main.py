import turtle
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time
from game_over import GameOver

screen = turtle.Screen()

middleline = turtle.Turtle()
turtle.shape("square")
turtle.color("white")
turtle.shapesize(stretch_len=0.4,stretch_wid=800)
screen.tracer(0)
screen.setup(width=800,height=600)
screen.title("pong")
screen.bgcolor("black")
screen.listen()


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()


screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()

    if ball.xcor() > 330 and r_paddle.ycor() - 50 < ball.ycor() < r_paddle.ycor() + 50:
     ball.bounce_x()


    if ball.xcor() < -330 and l_paddle.ycor() - 50 < ball.ycor() < l_paddle.ycor() + 50:
        ball.bounce_x()
        
    if ball.xcor() > 380:
        scoreboard.l_point()

        ball.reset_pos()
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_pos()
    if scoreboard.lscore >= 5 or scoreboard.rscore >=5:
       scoreboard.clear()
       GameOver()
       is_game_on = False
screen.exitonclick()