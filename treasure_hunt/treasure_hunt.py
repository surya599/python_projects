print ('''
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888  
                                                             
                                                             
       ''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice = input('you are at a cross road where do you want to go  Left or right : ').lower()

if choice == "left" :
    choice2 = input('you have come to a lake . there is an island in the middle of the lake type "wait" to wait for a boat or type "swim " to swim : ').lower()
    if choice2 == 'wait' :
        choice3 = input('you arrive at the island unharmed. There is house with 3 doors. One "red", one "yellow" and one "blue : " ').lower()
        if choice3 == 'red' :
            print("it's a room full of fire .game over ")
        elif choice3 == 'yellow':
            print('you have found a treasure you win!')
        elif choice3 == 'blue' :
            print('you enter a room of beasts . game over')
        else :
            print('the room does not exist')
    else :
        print("Attacked by trout. Game Over.")

else :
    print("you fell into a hole game over")
