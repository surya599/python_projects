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
    time.sleep(0.1)
    for seg_num in range(len(segments)-1,0,-1):
        newx = segments[seg_num -1].xcor() 
        newy = segments[seg_num -1].ycor() 
        segments[seg_num].goto(newx,newy)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()