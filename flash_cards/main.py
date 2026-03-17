from tkinter import *
import pandas
import random
current_card = {} 
WHITE = "#FFFFFF"
GREEN = "#B1DDC6"

try:
    data = pandas.read_csv("words_to_learn.csv") 
    
except FileNotFoundError:
    original_data = pandas.read_csv("spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def flip_card():
    global current_card
    canvas.itemconfig(card_title,text = "English",fill = "white")
    canvas.itemconfig(create_word,text = current_card["English"],fill = "white")

    canvas.itemconfig(card_background,image = card_back_image)


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text = "Spanish",fill = "black")
    canvas.itemconfig(create_word,text = current_card["Spanish"],fill = "black")
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer = window.after(3000,func=flip_card)

def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv",index=False)
    next_card()



window = Tk()
window.title("flash card")
window.config(pady=50,padx=50,bg=GREEN)
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526,bg=GREEN,highlightthickness=0)
card_front_img = PhotoImage(file ="card_front.png")
card_back_image = PhotoImage(file = "card_back.png")
card_background = canvas.create_image(400,263,image = card_front_img)
card_title = canvas.create_text(400,150,text="Title", font=("Ariel",40, "italic"))
create_word = canvas.create_text(400,263,text="Word", font=("Ariel",40, "bold"))
canvas.grid(column=0,row=0,columnspan=2)    

cross_img = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_img,highlightthickness=0,command = next_card)
unknown_button.grid(column=0,row=1)
right_img = PhotoImage(file="right.png")
known_button = Button(image=right_img,highlightthickness=0, command= is_known)
known_button.grid(column=1,row=1)

next_card()

window.mainloop()
