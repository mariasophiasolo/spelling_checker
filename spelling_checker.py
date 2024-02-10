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
window.minsize(width=500, height=500)
window.config(background="black")
window.resizable(False,False)

# heading
heading = Label(window, text="Spelling Checker", font=("Impact", 30,), fg="pink", bg="black")
heading.place (x=100, y= 90)

# entry
enter_text = Entry (window, justify="center", width=20, font=("Glacial Indifference", 25), fg="pink", bg="black", border=2)
enter_text.place(x=65, y= 150)
enter_text.focus()

# button
# command

window.mainloop()