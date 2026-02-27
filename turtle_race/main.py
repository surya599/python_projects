import turtle
import random

screen = turtle.Screen()
screen.setup(width= 500,height=400)
user_bet =  screen.textinput(title="make your bet",prompt= "which turtle will win the race : enter color:")
colors = ["red","green","orange","yellow","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
winner = "none"

allturtles = []
for turtle_index in range(6):
    tim = turtle.Turtle()
    allturtles.append(tim)
    tim.shape("turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y = y_positions[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:
    for tim in allturtles:
        if tim.xcor() > 230:
            winner = tim.pencolor()
            is_race_on = False
        randdistances = random.randint(0,10)
        tim.forward(randdistances)

if user_bet == winner:
    print(f"you guessed correct the winner is {winner}")
else :
    print(f"you are wrong the winner is {winner}")
screen.exitonclick()
