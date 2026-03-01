import turtle

myturtle = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    myturtle.forward(10)
def turn_left():
    newheading = myturtle.heading() + 10
    myturtle.setheading(newheading)
    
def move_backwards():
    myturtle.backward(10)
def turn_right():
    newheading = myturtle.heading() - 10
    myturtle.setheading(newheading)

def clear_drawing():
    myturtle.clear()
    myturtle.penup()
    myturtle.home()
    myturtle.pendown()

screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")  
screen.onkey(turn_right,"d")
screen.onkey(clear_drawing,"c")


screen.exitonclick()
