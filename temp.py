# -*- coding: utf-8 -*-
"""
Created on Sat May 12 13:08:54 2018

@author: aarvai
"""

from tkinter import *
from tkinter import Button, Entry


class App:

    enter_value: Entry

    def __init__(self, master):
        global v
        v = StringVar()

        frame = Frame(master)
        frame.pack()

        self.enter_value = Entry(frame, width=50, textvariable=v)
        self.enter_value.pack(side=LEFT)
        self.enter_value.focus_set()

        self.button1 = Button(frame, text="Print Value", fg="red", command=self.print_value)
        self.button1.pack(side=LEFT)

        self.button2 = Button(frame, text="Gray it out", fg="red", command=self.gray_it_out)
        self.button2.pack(side=LEFT)

        self.button3 = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button3.pack(side=LEFT)

    def print_value(self):
        print("hi there")
        #print(self.enter_value.get())
        print(v.get())

    def gray_it_out(self):
        self.enter_value.config(state=DISABLED)


root = Tk()

app = App(root)

root.mainloop()
