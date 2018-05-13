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

        global deg, rad
        deg = StringVar()
        rad = StringVar()

        #print("Tkinter theme options are:")
        #print(ttk.Style().theme_names())
        #print("Current Tkinter theme:")
        #print(ttk.Style().theme_use())
        ttk.Style().theme_use('vista')

        frame = ttk.Frame(master)
        frame.pack()

        self.l1 = ttk.Label(text="Degrees")
        self.l1.pack(side=LEFT)

        self.degrees = ttk.Entry(frame, width=20, textvariable=deg)
        self.degrees.pack(side=LEFT)
        self.degrees.focus_set()

        self.l2 = ttk.Label(text="Radians")
        self.l2.pack(side=LEFT)

        self.buttonltor = ttk.Button(frame, text="-->", command=self.l_to_r)
        self.buttonltor.pack(side=LEFT)

        self.radians = ttk.Entry(frame, width=20, textvariable=rad)
        self.radians.pack(side=LEFT)

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
        self.degrees.config(state=DISABLED)

    def l_to_r(self):
        self.radians.delete(0)
        self.radians.insert(0, deg+'rad')
        self.radians.config(state='readonly')

root = Tk()

app = AcsGui(root)

root.mainloop()
