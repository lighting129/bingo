from tkinter import *
import random
import numpy


#layout
win = Tk()
win.title(' database')

heading = Label(win , text='DATABASE')
heading.grid(row=1,column=3)

name = Label(win , text = 'COMPANY NAME:-')
name.grid(row=2,column=1)

N = Entry(win)
N.grid(row=2,column=2)
n = N.get()

date = Label(win, text = 'DATE:-')
date.grid(row=2,column=4)

D = Entry(win)
D.grid(row=2,column=5)
d  = D.get()

account_no = Label(win , text = 'ACCOUNT NUMBER:- ')
account_no.grid(row=3,column=2)

A = Entry(win)
A.grid(row=3,column=3)
a = A.get()

def update():
    acc = []
    acc.insert(0,A.get())
    show = Label(win , text=acc)
    show.grid(row = 5,column=3)


up = Button(win , text= 'update', command=update)
up.grid(row=4,column=4)


win.mainloop()