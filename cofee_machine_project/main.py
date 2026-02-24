from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
CoffeeMaker = CoffeeMaker()
CoffeeMaker.report()
moneyMachine.report()

mymenu = Menu()
print("Menu and costs:")
for item in mymenu.menu:
    print(f"{item.name} : ${item.cost}")

is_on = True

while is_on:
    options = mymenu.get_items()
    choice = input(f"What Would You like {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        CoffeeMaker.report()
        moneyMachine.report()
    else :
        drink = mymenu.find_drink(choice)
        if(CoffeeMaker.is_resource_sufficient(drink)):
            if moneyMachine.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)