# pseudocode

# look for any exsisting python program on youtube
# re-create that project then send a demo that it is working

# make sure first that you have installed the textblob module

# import tkinter and the textblob
import tkinter
from tkinter import *
from textblob import TextBlob

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    corrected_text = str(a.correct())
    spell.config(text="Corrected text is:\n" + corrected_text)

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
enter_button = Button(window, text="Check", width=10, font=("Glacial Indifference", 20, "bold"), fg="black", bg="pink", command=check_spelling)
enter_button.place(x=150, y= 220)

# command
spell= Label (window, justify="center", font=("Impact", 20,), fg="pink", bg="black")
spell.place(x=145, y= 300)

window.mainloop()