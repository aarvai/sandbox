# -*- coding: utf-8 -*-
"""
Created on Sat May 12 13:08:54 2018

@author: aarvai
"""

from tkinter import *

class App:

    def __init__(self, master):
	    v = StringVar()
		
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="Print Value", fg="red", command=self.print_value)
        self.button.pack(side=LEFT)

        self.enter_value = Entry(frame, width=50, textvariable=v)
        self.enter_value.pack(side=LEFT)
		
	def print_value(self):
        print("hi there")
        print(v)
		
root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below
