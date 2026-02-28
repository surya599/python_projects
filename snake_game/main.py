import turtle
import random
import time
screen = turtle.Screen()
screen.setup(600,600)
screen.tracer(0)
start_positions = [(0,0),(-20,0),(-40,0)]
screen.bgcolor("black")
segments = []
for positions in start_positions:
    new_segment = turtle.Turtle()
    segments.append(new_segment)
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(positions)
    
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    for seg in segments:
        seg.penup()
        seg.forward(20)

screen.exitonclick()