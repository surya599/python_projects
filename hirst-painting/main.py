import turtle
import random
turtle.colormode(255)
#import colorgram

#colors = colorgram.extract('hirst_image.jpg', 30)

#rgb_colors = []

#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)



color_list = [(183, 167, 136), (130, 89, 66), (75, 91, 118), (153, 164, 180), (177, 152, 162), (51, 34, 28), (204, 201, 156), (152, 173, 160), (36, 39, 54), (121, 80, 93), (167, 154, 50), (80, 111, 83), (63, 27, 35), (124, 33, 24), (108, 34, 48), (51, 58, 89), (187, 189, 201), (159, 107, 120), (107, 123, 158), (165, 108, 100), (36, 47, 43), (203, 184, 191), (100, 146, 105), (181, 199, 189), (209, 183, 179), (67, 76, 33)]

myturtle = turtle.Turtle()
myturtle.speed("fastest")
screen = turtle.Screen()
myturtle.setheading(225)
myturtle.penup()
myturtle.hideturtle()
myturtle.forward(250)
myturtle.setheading(0)
numberofdots = 100
for dot_count in range (1,numberofdots+1):
    myturtle.dot(20,random.choice(color_list))
    myturtle.penup()
    myturtle.forward(50)
    if dot_count % 10 == 0:
        myturtle.setheading(90)
        myturtle.forward(50)
        myturtle.setheading(180)
        myturtle.forward(500)
        myturtle.setheading(0)

screen.exitonclick()



