print("welcome to tip calculator")
a = float(input("what was the tota bill to be paid : "))
b = float(input("how much tip would you like to give: "))
c = int(input("how many people are going to pay the bill: "))

d = a * (b /100)
totalvalue = a + d
eachperson = totalvalue/c

print(f"each person should pay {round(eachperson,2)}")
