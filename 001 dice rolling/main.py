#all modules 

from tkinter import *
from PIL import ImageTk, Image
from random import randint 

root = Tk()

##backgound color 

root.configure(bg="gray75")
#music player icon 
#root.iconbitmap("F://Project//dice rolling//dice.ico")

#title
root.title("Dice Rolling")

#szie of window
root.minsize(height=420,width=500)
root.maxsize(height=420,width=500)

## all image file

img_1 = ImageTk.PhotoImage(Image.open("./1 in ludo.png"))
img_2 = ImageTk.PhotoImage(Image.open("./2 in ludo.png"))
img_3 = ImageTk.PhotoImage(Image.open("./3 in ludo.png"))
img_4 = ImageTk.PhotoImage(Image.open("./4 in ludo.png"))
img_5 = ImageTk.PhotoImage(Image.open("./5 in ludo.png"))
img_6 = ImageTk.PhotoImage(Image.open("./6 in ludo.png"))

############################################################################
########################## random sampling #############
def dice_rolling():
	dice_value = randint(1, 6)
	x,y = 40,115 

	if dice_value == 1:my_img_1_label = Label(image=img_1).place(x=x,y=y)
	elif dice_value == 2 :my_img_2_label = Label(image=img_2).place(x=x,y=y)
	elif dice_value == 3:my_img_3_label = Label(image=img_3).place(x=x,y=y)
	elif dice_value == 4 :my_img_4_label = Label(image=img_4).place(x=x,y=y)
	elif dice_value == 5:my_img_5_label = Label(image=img_5).place(x=x,y=y)
	elif dice_value == 6 :my_img_6_label = Label(image=img_6).place(x=x,y=y)


############################################################################
# label dice rolling
show_label = Label(root, text= "DICE ROLLING",borderwidth=6,relief="solid",justify=RIGHT, bg='OrangeRed2', fg="white",padx=127.5, pady=10, font=("arial",25)).place(x=0, y=1)
# label roll the dice
show_label_roll_dice = Label(root, text= "Please Roll The Dice",borderwidth=2,relief="solid",justify=RIGHT, bg='sandy brown',padx=102, pady=7, font=("Times New Roman",15)).place(x=1, y=350)
#thankyou label
show_label_roll_dice = Label(root, text= "Thankyou For Using...",borderwidth=2,relief="solid",justify=RIGHT, bg='snow4',padx=161, pady=0, font=("Times New Roman",15)).place(x=1, y=385)
# rollling dice button
dice_rolling_button = Button(root, text='Roll Here',command=dice_rolling, bg='burlywood1',borderwidth=2,relief="solid",padx=20.5,pady=4,font=("arial Black", 10)).place(x=379.5, y=346)\

# For window 
root.mainloop()
