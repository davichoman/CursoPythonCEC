# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:34:16 2019

@author: CEC
"""


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
def clicked():
 
    lbl.configure(text="Button was clicked !!")
 
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=1, row=0)
 
window.mainloop()