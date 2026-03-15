from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"
YELLOW = "#f7f5dd"

window = Tk()
window.config(padx=100,pady=100)
window.title("Password Manager")
window.config(bg=YELLOW)
photo = PhotoImage(file ="logo.png")

def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError,json.JSONDecodeError):
        messagebox.showinfo(title="Error",message="No Data found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message= f"email : {email}\n password: {password}")

def add_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="You can't leave the fields empty")
    else:
        is_ok = messagebox.askokcancel(title= website,message= f"these are your credentials email : {email}\n password : {password}")
        
        if is_ok:
            try:
                with open("data.json",mode='r') as data_file:
                    data = json.load(data_file)
            except (FileNotFoundError,json.JSONDecodeError):
                with open("data.json",mode='w') as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open("data.json",mode='w') as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                website_input.delete(0,END)
                password_input.delete(0,END)

def generate_password():
    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')','*', '+', ',', '-', '.', '/', ':', ';', '<','=', '>', '?', '@', '[', ']', '^', '_','`', '{', '|', '}', '~']
    password = ""
    nlc = random.randint(1,5)
    nuc = random.randint(1,5)
    nn = random.randint(2,4)
    nsc = random.randint(2,4)
    for i in range (nlc):
        character = random.choice(lower_case)
        password = password + character
    for i in range (nuc):
        character = random.choice(upper_case)
        password = password + character
    for i in range (nsc):
        character = random.choice(special_characters)
        password = password + character
    for i in range (nn):
        character = random.choice(numbers)
        password = password + character
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    password_input.delete(0,END)
    password_input.insert(0,password)
    pyperclip.copy(password)


    

canvas = Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image = photo)

canvas.grid(column=1,row = 0)
website_label = Label(text="Website",bg=YELLOW,font=(FONT_NAME,15,"normal"))
website_label.grid(column=0,row=1)

website_input = Entry(width=35)
website_input.grid(column=1,row=1)
website_input.focus()

search_button = Button(text="search",bg=YELLOW,font=(FONT_NAME,15,"normal"),width=17,command = find_password)
search_button.grid(column=2,row=1)

email_label = Label(text="Email/Username",bg=YELLOW,font=(FONT_NAME,15,"normal"))
email_label.grid(column=0,row=2)

email_input = Entry(width=75)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(END,"suryabhuvaneshwarreddy@gmail.com")

password_label = Label(text="Password",bg=YELLOW,font=(FONT_NAME,15,"normal"))
password_label.grid(column=0,row=3)

password_input = Entry(width=37)
password_input.grid(column=1,row=3)

generate_button = Button(text="Generate password",bg=YELLOW,font=(FONT_NAME,15,"normal"),command = generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="add",bg=YELLOW,font=(FONT_NAME,15,"normal"),width=36,command=add_data)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()