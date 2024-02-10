# pseudocode

# look for any exsisting python program on youtube
# re-create that project then send a demo that it is working

# make sure first that you have installed the textblob module

# import tkinter and the textblob
import tkinter
from tkinter import *
from textblob import TextBlob

# create the main window for your program
window = Tk()
window.title("Spelling Checker")
window.minsize(width=500, height=400)
window.config(background="pink")

# heading
heading = Label(window, text="Spelling Checker")
heading.place (x=0, y=0)
# entry
# button
# command

window.mainloop()