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
        deg = DoubleVar()
        rad = DoubleVar()

        #print("Tkinter theme options are:")
        #print(ttk.Style().theme_names())
        #print("Current Tkinter theme:")
        #print(ttk.Style().theme_use())
        ttk.Style().theme_use('vista')

        self.l1 = ttk.Label(text="Degrees")
        self.l1.grid(row=0, column=0)

        self.degrees = ttk.Entry(master, width=20, textvariable=deg)
        self.degrees.grid(row=1, column=0)
        self.degrees.focus_set()

        self.buttonltor = ttk.Button(master, text="▶", command=self.l_to_r)
        self.buttonltor.grid(row=0, column=1)

        self.l2 = ttk.Label(text="Radians")
        self.l2.grid(row=0, column=2)

        self.radians = ttk.Entry(master, width=20, textvariable=rad)
        self.radians.grid(row=1, column=2)

        self.button1 = ttk.Button(master, text="Print Value", command=self.print_value)
        self.button1.grid(row=0, column=3, rowspan=2)

        self.button2 = ttk.Button(master, text="Gray it out", command=self.gray_it_out)
        self.button2.grid(row=0, column=4, rowspan=2)

        self.button3 = ttk.Button(master, text="QUIT", command=master.quit)
        self.button3.grid(row=0, column=5, rowspan=2)

    def print_value(self):
        print(rad.get())

    def gray_it_out(self):
        self.degrees.config(state=DISABLED)

    def l_to_r(self):
        self.radians.delete(0,END)
        self.radians.insert(0,deg.get()*3.14159/180)
        self.radians.config(state='readonly')
        self.degrees.config(state='readonly')

root = Tk()

app = AcsGui(root)

root.mainloop()
