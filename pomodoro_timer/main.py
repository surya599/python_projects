from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_id = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer_id) 
    canvas.itemconfig(timer_text,text = "00:00")
    label.config(text="Timer")
    tickmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global reps
    reps = reps + 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Long Break" ,fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Short Break",fg= GREEN)
    else:
        countdown(work_sec)
        label.config(text="Work Time",fg= PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count /60)
    count_sec = count %60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count > 0:
       global timer_id
       timer_id = window.after(1000,countdown,count-1)
    else:
        timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        tickmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro timer")
window.config(padx=100,pady=50,bg=YELLOW)
photo = PhotoImage(file="tomato.png")
label = Label(text="Pomodoro Timer")
label.config(bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
label.grid(column=1,row=0)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image = photo)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
button1 = Button(text="Start",command=timer)
button1.grid(column=0,row=2)

button2 = Button(text="Reset", command=reset_timer)

button2.grid(column=2,row=2)
tickmark = Label()
tickmark.config(bg=YELLOW,fg=GREEN,font=(FONT_NAME,20,"bold"))
tickmark.grid(column=1,row=3)
window.mainloop()