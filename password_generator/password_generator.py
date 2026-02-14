import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','^','%','&','*','(',')','+']

print("Welcome to password generator")
letters_count = int(input('how many letters world you like in your password: '))
numbers_count = int(input('how many numbers world you like in your password: '))
symbols_count = int(input('how many symbols world you like in your password: '))

password = []

for i in range (0,letters_count):
    password.append(random.choice(letters))

for i in range (0,numbers_count):
    password.append(random.choice(numbers))

for i in range (0,symbols_count):
    password.append(random.choice(symbols))

random.shuffle(password)

password_string = ""
for i in password:
    password_string = password_string + i

print("your password is "+password_string) 