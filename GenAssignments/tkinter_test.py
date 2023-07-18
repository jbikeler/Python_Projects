from tkinter import *

win = Tk()
win.mainloop()

b1 = Button(win, text="One")
b2 = Button(win, text="Two")

b1.pack(side=LEFT, padx=10)
b2.pack(side=RIGHT, padx=10)

def but1():
    print("Button one was pushed")

b1.configure(command=but1)