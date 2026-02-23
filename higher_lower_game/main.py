import random
from data import datalist
from art import logo
from art import vs

print(logo)
isgameover = False
winner = "none"
score = 0
choice1 = random.choice(datalist)
choice2 = random.choice(datalist)
while choice1 == choice2:
    choice2 = random.choice(datalist)

while isgameover != True:
    print(f"compare A : {choice1["name"]}, {choice1["description"]}\n")
    print(vs)
    print(f"Against B: {choice2["name"]}, {choice2["description"]}\n")

    if(choice1["followers"] > choice2["followers"]):
        winner = choice1
    else:
        winner = choice2

    userchoice = input("Who has more followers A or B : ").lower()

    if userchoice =='a' and winner == choice1:
        score = score + 1
        print(f"You are correct your score is {score}")
        choice2 = random.choice(datalist)
        while choice1 == choice2:
            choice2 = random.choice(datalist)
    elif userchoice ==  'b' and winner == choice2:
        score = score + 1
        print(f"you are correct your score is {score}")
        choice1 = choice2
        choice2 = random.choice(datalist)
        while choice1 == choice2:
            choice2 = random.choice(datalist)
    else:
        print(f"No you are wrong your total score is {score}")
        isgameover = True
