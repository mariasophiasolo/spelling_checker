# pseudocode

# look for any exsisting python program on youtube
# re-create that project then send a demo that it is working

# make sure first that you have installed the textblob module

# import tkinter and the textblob
import tkinter as tk
from tkinter import *
from textblob import TextBlob

# create the main window for your program
window = Tk()
window.title("Spelling Checker")
window.minsize(width=500, height=500)
window.config(background="black")
window.resizable(False,False)

image = tk.PhotoImage (file="spelling.jpg")
image_label = tk.Label (picture = image, borderwidth=0)
image_label.place (x=0, y=0)
# heading
heading = Label(window, text="Spelling Checker", font=("Impact", 30,), fg="pink", bg="black")
heading.place (x=100, y= 90)

# entry
# button
# command

window.mainloop()