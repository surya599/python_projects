import turtle
import random
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from gameover import Game_over
screen = turtle.Screen()
screen.setup(600,600)
screen.tracer(0)
screen.title("My Snake Game")
screen.bgcolor("black")
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


     
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        snake.extend()
        x = food.xcor()
        y = food.ycor()
        snake.extend()
        food.refresh()
        scoreboard.score = scoreboard.score + 1
        scoreboard.refresh_score()
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() <-290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        Game_over()
        game_is_on = False

    for segment in snake.segments[1:]:

        if snake.segments[0].distance(segment) < 10:
            Game_over()
            game_is_on = False
    
screen.exitonclick()