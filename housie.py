import random
from tkinter import *
import numpy as np
from playsound import playsound
from gtts import gTTS

win = Tk()
win.title('housei teller machine')
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
board = np.arange(1,91).reshape(9,10)

#functions

def random_generator():
    x=random.choice(num)
    number = Label(win,text=x)
    number.grid(row=4,column=1)
    num.remove(x)
    for i in range(9):
        for j in range(10):
            if board[i,j]==x:
                board[i,j]=0
    show_board = Label(win,text=board)
    show_board.grid(row=4,column=3)
    tts = gTTS(text=str(x), lang='en')
    tts.save("good.mp3")
    playsound('D:\Documents\poython\good.mp3')

def clear():
    clear = Label(win,text='___')
    clear.grid(row=4,column=1)





#labels
greet = Label(win,text = 'welcome to no.  generator')
greet.grid(row=1,column=3)

#button
generator = Button(win,text='generator',command=random_generator)
generator.grid(row=2,column=2)



clear_screen  = Button(win,text='CLEAR',command=clear)
clear_screen.grid(row=3,column=4)

win.mainloop()

