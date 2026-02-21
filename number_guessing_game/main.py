import random
userchoice = -1
def play():
    user = int(input("enter the number : "))
    if(user == computerchoice):
        return True,"win"
    elif(user > computerchoice):
        print("too high")
        return False,"not win"
    elif(user < computerchoice) :
        print("too low")
        return False,"not win"
    
logo = '''                    ___.                                                      .__                                               
  ____  __ __  _____\_ |__   ___________     ____  __ __   ____   ______ _____|__| ____    ____      _________    _____   ____  
 /    \|  |  \/     \| __ \_/ __ \_  __ \   / ___\|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\    / ___\__  \  /     \_/ __ \ 
|   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/  / /_/  >  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >  / /_/  > __ \|  Y Y  \  ___/ 
|___|  /____/|__|_|  /___  /\___  >__|     \___  /|____/  \___  >____  >____  >__|___|  /\___  /   \___  (____  /__|_|  /\___  >
     \/            \/    \/     \/        /_____/             \/     \/     \/        \//_____/   /_____/     \/      \/     \/ '''

print(logo)

print("I am thinking of a number between 1 , 100")

userchoice = input("choose 'easy' or 'hard' level ")

computerchoice = random.randrange(1,101)
isgameover = False

if userchoice == 'easy':
    totalchoices = 10
    for i in range (10):
        print(f"you have {totalchoices} choices")
        isgameover,result = play()
        if(isgameover):
            break
        else:
            totalchoices = totalchoices - 1
elif userchoice == 'hard' :
    totalchoices = 5
    for i in range(1,6) :
        print(f"you have {totalchoices} choices")
        isgameover,result = play()
        if isgameover:
            break
        else:
            totalchoices = totalchoices - 1

if result == "win":
    print("yes that's correct")
else :
    print(f"no you didn't guessed the number the correct number is {computerchoice}")
    


