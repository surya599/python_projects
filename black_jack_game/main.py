import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

def deal_cards():
    cards = [11, 2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    score = sum(cards)
    return score
def compare(user_score,computer_score):
    if user_score > 21:
        return "you loose"
    elif computer_score > 21:
        return "you win"
    elif user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "you lost because opponent has black jack"
    elif user_score == 0:
        return "you win because you have black jack"
    elif user_score > computer_score:
        return "you win"
    elif user_score < computer_score:
        return "you loose"
    

usercards = []
computercards = []
is_game_over = False
computer_score = -1

for i in range(2):
    usercards.append(deal_cards())

    
for i in range(2):
     computercards.append(deal_cards())
print(f"your cards {usercards}")
print(f"computer first cards {computercards[0]}")
while not is_game_over:
    user_score = calculate_score(usercards)
    computer_score = calculate_score(computercards)
    print(f"your score {user_score}")

    if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("type 'y' to to get another card or 'n' to pass ")
        if user_should_deal == 'y':
            usercards.append(deal_cards())
        else :
            is_game_over = True 

while computer_score != 0 and computer_score < 17:
    computercards.append(deal_cards())
    computer_score =  calculate_score(computercards)

print(f"your cards {usercards} and your score {user_score}")
print(f"computer cards {computercards} and computer score {computer_score}")

print(compare(user_score,computer_score))