import turtle
import pandas
from displaytext import Display
screen = turtle.Screen()
screen.title("India States Game")
screen.setup(width=600,height=700)
image = "india_map_3.gif"
screen.addshape(image)
turtle.shape(image)
gussed_states = []
correct = 0
data = pandas.read_csv("indian_states.csv")
all_states = data.state.to_list()
while len(gussed_states) < 29:
    answer_state = screen.textinput(title=f"{correct}/28",prompt="What is the another state's name").title()
    if answer_state is None:
        break

    if answer_state in all_states :
        correct = correct + 1
        statedata = data[data.state == answer_state]
        Display(answer_state,statedata.x.item(),statedata.y.item())


screen.exitonclick()