# -*- coding: utf-8 -*-
"""
Created on Sat May 12 13:08:54 2018

@author: aarvai
"""

from tkinter import *
from tkinter import Button, Entry
from tkinter import ttk

#Select tkinter style
#s = ttk.Style()
#print("Tkinter theme options are:")
#print(s.theme_names())
#print("Current Tkinter theme:")
#print(s.theme_use())
#s.theme_use('clam')


class AcsGui:

    enter_value: Entry

    def __init__(self, master):

        global v
        v = StringVar()

        print("Tkinter theme options are:")
        print(ttk.Style().theme_names())
        print("Current Tkinter theme:")
        print(ttk.Style().theme_use())
        ttk.Style().theme_use('vista')

        frame = ttk.Frame(master)
        frame.pack()

        self.enter_value = ttk.Entry(frame, width=50, textvariable=v)
        self.enter_value.pack(side=LEFT)
        self.enter_value.focus_set()

        self.button1 = ttk.Button(frame, text="Print Value", command=self.print_value)
        self.button1.pack(side=LEFT)

        self.button2 = ttk.Button(frame, text="Gray it out", command=self.gray_it_out)
        self.button2.pack(side=LEFT)

        self.button3 = ttk.Button(frame, text="QUIT", command=frame.quit)
        self.button3.pack(side=LEFT)

    def print_value(self):
        print("hi there")
        #print(self.enter_value.get())
        print(v.get())

    def gray_it_out(self):
        self.enter_value.config(state=DISABLED)


root = Tk()

app = AcsGui(root)

root.mainloop()
