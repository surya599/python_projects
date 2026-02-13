import random

playerchoice = int(input("what do you choose ? type 0 for Rock 1 for paper and 0 for Scissors "))
if playerchoice < 0 or playerchoice > 3:
    print("invalid input")
else :    
    computerchoice = random.randint(0,1)

    zero = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """

one = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

two = """

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

    """

if playerchoice == 0 and computerchoice == 0 :
        print(zero)
        print("vs")
        print(zero)        
        print("tied")  
elif playerchoice == 1 and computerchoice == 1 :
        print(one)
        print("vs")
        print(one)
        print("tied")
elif playerchoice == 2 and computerchoice == 2 :
        print(two)
        print("vs")
        print(two)  
        print("tied")
elif playerchoice == 0 and computerchoice == 1 :
        print(zero)
        print("vs")
        print(one)
        print("you lost")
elif playerchoice == 0 and computerchoice == 2 :
        print(zero)
        print("vs")
        print(two)
        print("you won")
elif playerchoice == 1 and computerchoice == 0 :
        print(one)
        print("vs")
        print(zero)
        print("you won")
elif playerchoice == 1 and computerchoice == 2 :
        print(one)
        print("vs")
        print(two)
        print("you lost")
elif playerchoice == 2 and computerchoice == 0 :
        print(two)
        print("vs")
        print(zero)
        print("you lost")
elif playerchoice == 2 and computerchoice == 1 :
        print(two)
        print("vs")
        print(one)
        print("you won")