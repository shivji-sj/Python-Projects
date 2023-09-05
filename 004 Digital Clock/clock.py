# Creating a digital clock in python

import time
from tkinter import *

root = Tk()
root.minsize(width=391,height=150)
root.maxsize(width=391,height=250)

root.configure(bg="black")


def start():
	text = time.strftime("%H:%M:%S")
	label = Label(root, text = text,font=("ds_digital", 50, "bold"), bg="black", fg="#15ff00", bd=50, highlightbackground="yellow", highlightthickness=10,)
	label.grid(row=0, column=1)
	label.after(200, start)

start()
root.mainloop()