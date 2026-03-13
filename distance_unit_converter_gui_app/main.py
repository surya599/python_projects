from tkinter import *


def miles_km():
    miles = float(miles_input.get())
    km = round(miles*1.609)
    kilometerresultlabel.config(text=f"{km}")
window = Tk()
window.config(padx=20,pady=20)
window.title("Miles to Kilometers Converter")
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
isequaltolabel = Label(text="is equal to")
isequaltolabel.grid(column=0, row=1)
kilometerresultlabel = Label(text="0")
kilometerresultlabel.grid(column=1, row=1)
kilometerlabel = Label(text="Km")
kilometerlabel.grid(column=2, row=1)
buttonlabel = Button(text="Calculate",command=miles_km)
buttonlabel.grid(column=1, row=2)


window.mainloop()