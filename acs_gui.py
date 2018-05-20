# -*- coding: utf-8 -*-
"""
Created on Sat May 12 13:08:54 2018

@author: aarvai
"""

import numpy as np
from tkinter import Tk
from tkinter import Button, Entry, DoubleVar, END
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

        global ephSunPosX, ephSunPosY, ephSunPosZ
        global ephJwstPosX, ephJwstPosY, ephJwstPosZ
        global ephSunVecX, ephSunVecY, ephSunVecZ
        global ephSunVecNormX, ephSunVecNormY, ephSunVecNormZ

        ephSunPosX = DoubleVar()
        ephSunPosY = DoubleVar()
        ephSunPosZ = DoubleVar()
        ephJwstPosX = DoubleVar()
        ephJwstPosY = DoubleVar()
        ephJwstPosZ = DoubleVar()
        ephSunVecX = DoubleVar()
        ephSunVecY = DoubleVar()
        ephSunVecZ = DoubleVar()
        ephSunVecNormX = DoubleVar()
        ephSunVecNormY = DoubleVar()
        ephSunVecNormZ = DoubleVar()

        #print("Tkinter theme options are:")
        #print(ttk.Style().theme_names())
        #print("Current Tkinter theme:")
        #print(ttk.Style().theme_use())
        ttk.Style().theme_use('vista')

        #Title
        self.title = ttk.Label(text="ACS Conversion Tool")
        self.title.grid(row=0, column=0, columnspan=10)

        #Ephemeris Section
        self.ephemLabel = ttk.Label(text="Ephemeris")
        self.ephemLabel.grid(row=1, column=0, columnspan=10)

        #Sun and JWST Positions
        self.ephPosLabel = ttk.Label(text="Positions (ECI, km)")
        self.ephPosLabel.grid(row=2, column=0, columnspan=3)

        self.ephPosXLabel = ttk.Label(text="x")
        self.ephPosXLabel.grid(row=4, column=0)

        self.ephPosYLabel = ttk.Label(text="y")
        self.ephPosYLabel.grid(row=5, column=0)

        self.ephPosZLabel = ttk.Label(text="z")
        self.ephPosZLabel.grid(row=6, column=0)

        self.ephSunLabel = ttk.Label(text="Sun")
        self.ephSunLabel.grid(row=3, column=1)

        self.ephSunPosXEntry = ttk.Entry(master, width=20, textvariable=ephSunPosX)
        self.ephSunPosXEntry.grid(row=4, column=1)
        self.ephSunPosXEntry.focus_set()

        self.ephSunPosYEntry = ttk.Entry(master, width=20, textvariable=ephSunPosY)
        self.ephSunPosYEntry.grid(row=5, column=1)

        self.ephSunPosZEntry = ttk.Entry(master, width=20, textvariable=ephSunPosZ)
        self.ephSunPosZEntry.grid(row=6, column=1)

        self.ephJwstLabel = ttk.Label(text="JWST")
        self.ephJwstLabel.grid(row=3, column=2)

        self.ephJwstPosXEntry = ttk.Entry(master, width=20, textvariable=ephJwstPosX)
        self.ephJwstPosXEntry.grid(row=4, column=2)

        self.ephJwstPosYEntry = ttk.Entry(master, width=20, textvariable=ephJwstPosY)
        self.ephJwstPosYEntry.grid(row=5, column=2)

        self.ephJwstPosZEntry = ttk.Entry(master, width=20, textvariable=ephJwstPosZ)
        self.ephJwstPosZEntry.grid(row=6, column=2)

        #Convert Positions to Sun Vector
        self.ephPosToVecButton = ttk.Button(master, text="▶", command=self.ephPosToVec)
        self.ephPosToVecButton.grid(row=4, column=3)

        #Sun Vector
        self.ephSunVecLabel = ttk.Label(text="Sun Vector")
        self.ephSunVecLabel.grid(row=2, column=4, columnspan=2)

        self.ephSunVecUnitLabel = ttk.Label(text="(ECI, km)")
        self.ephSunVecUnitLabel.grid(row=3, column=4, columnspan=2)

        self.ephSunVecXEntry = ttk.Entry(master, width=20, textvariable=ephSunVecX)
        self.ephSunVecXEntry.grid(row=4, column=5)

        self.ephSunVecYEntry = ttk.Entry(master, width=20, textvariable=ephSunVecY)
        self.ephSunVecYEntry.grid(row=5, column=5)

        self.ephSunVecZEntry = ttk.Entry(master, width=20, textvariable=ephSunVecZ)
        self.ephSunVecZEntry.grid(row=6, column=5)

        #Convert sun vector to normalized sun vector
        self.ephVecToNormVecButton = ttk.Button(master, text="▶", command=self.ephVecToNormVec)
        self.ephVecToNormVecButton.grid(row=4, column=6)

        #Normalized Sun Vector
        self.ephSunVecNormLabel = ttk.Label(text="Sun Vector Normalized")
        self.ephSunVecNormLabel.grid(row=2, column=7, columnspan=2)

        self.ephSunVecNormUnitLabel = ttk.Label(text="(ECI)")
        self.ephSunVecNormUnitLabel.grid(row=3, column=7, columnspan=2)

        self.ephSunVecNormXEntry = ttk.Entry(master, width=20, textvariable=ephSunVecNormX)
        self.ephSunVecNormXEntry.grid(row=4, column=8)

        self.ephSunVecNormYEntry = ttk.Entry(master, width=20, textvariable=ephSunVecNormY)
        self.ephSunVecNormYEntry.grid(row=5, column=8)

        self.ephSunVecNormZEntry = ttk.Entry(master, width=20, textvariable=ephSunVecNormZ)
        self.ephSunVecNormZEntry.grid(row=6, column=8)

        #Clear ephem
        self.ephClearButton = ttk.Button(master, text="Clear", command=self.ephClear)
        self.ephClearButton.grid(row=4, column=9)


#        self.l2 = ttk.Label(text="Radians")
#        self.l2.grid(row=0, column=2)

#        self.radians = ttk.Entry(master, width=20, textvariable=rad)
#        self.radians.grid(row=1, column=2)

#        self.button1 = ttk.Button(master, text="Print Value", command=self.print_value)
#        self.button1.grid(row=0, column=3, rowspan=2)

#        self.button2 = ttk.Button(master, text="Gray it out", command=self.gray_it_out)
#        self.button2.grid(row=0, column=4, rowspan=2)

#        self.button3 = ttk.Button(master, text="QUIT", command=master.quit)
#        self.button3.grid(row=0, column=5, rowspan=2)

    def ephPosToVec(self):

        #clear sunVec
        self.ephSunVecXEntry.delete(0,END)
        self.ephSunVecYEntry.delete(0,END)
        self.ephSunVecZEntry.delete(0,END)

        #sun vector = sun position - JWST position
        self.ephSunVecXEntry.insert(0,ephSunPosX.get()-ephJwstPosX.get())
        self.ephSunVecYEntry.insert(0,ephSunPosY.get()-ephJwstPosY.get())
        self.ephSunVecZEntry.insert(0,ephSunPosZ.get()-ephJwstPosZ.get())

        #disable sun position
        self.ephSunPosXEntry.config(state='readonly')
        self.ephSunPosYEntry.config(state='readonly')
        self.ephSunPosZEntry.config(state='readonly')

        # disable JWST position
        self.ephJwstPosXEntry.config(state='readonly')
        self.ephJwstPosYEntry.config(state='readonly')
        self.ephJwstPosZEntry.config(state='readonly')

        # disable sun vector
        self.ephSunVecXEntry.config(state='readonly')
        self.ephSunVecYEntry.config(state='readonly')
        self.ephSunVecZEntry.config(state='readonly')

    def ephVecToNormVec(self):

        #clear sunVec
        self.ephSunVecNormXEntry.delete(0,END)
        self.ephSunVecNormYEntry.delete(0,END)
        self.ephSunVecNormZEntry.delete(0,END)

        #normalize sun vector
        ephSunVec = np.array([ephSunVecX.get(), ephSunVecY.get(), ephSunVecZ.get()])
        ephSunVecNorm = ephSunVec / np.linalg.norm(ephSunVec)
        self.ephSunVecNormXEntry.insert(0,ephSunVecNorm[0])
        self.ephSunVecNormYEntry.insert(0,ephSunVecNorm[1])
        self.ephSunVecNormZEntry.insert(0,ephSunVecNorm[2])

        # disable sun vector
        self.ephSunVecXEntry.config(state='readonly')
        self.ephSunVecYEntry.config(state='readonly')
        self.ephSunVecZEntry.config(state='readonly')

        # disable normalized sun vector
        self.ephSunVecNormXEntry.config(state='readonly')
        self.ephSunVecNormYEntry.config(state='readonly')
        self.ephSunVecNormZEntry.config(state='readonly')

    def ephClear(self):

        #re-enable all ephemeris values
        self.ephJwstPosXEntry.config(state='Normal')
        self.ephJwstPosYEntry.config(state='Normal')
        self.ephJwstPosZEntry.config(state='Normal')
        self.ephSunPosXEntry.config(state='Normal')
        self.ephSunPosYEntry.config(state='Normal')
        self.ephSunPosZEntry.config(state='Normal')
        self.ephSunVecXEntry.config(state='Normal')
        self.ephSunVecYEntry.config(state='Normal')
        self.ephSunVecZEntry.config(state='Normal')
        self.ephSunVecNormXEntry.config(state='Normal')
        self.ephSunVecNormYEntry.config(state='Normal')
        self.ephSunVecNormZEntry.config(state='Normal')

        #clear all ephemeris values
        self.ephJwstPosXEntry.delete(0,END)
        self.ephJwstPosYEntry.delete(0,END)
        self.ephJwstPosZEntry.delete(0,END)
        self.ephSunPosXEntry.delete(0,END)
        self.ephSunPosYEntry.delete(0,END)
        self.ephSunPosZEntry.delete(0,END)
        self.ephSunVecXEntry.delete(0,END)
        self.ephSunVecYEntry.delete(0,END)
        self.ephSunVecZEntry.delete(0,END)
        self.ephSunVecNormXEntry.delete(0,END)
        self.ephSunVecNormYEntry.delete(0,END)
        self.ephSunVecNormZEntry.delete(0,END)

        #Set the focus to the first ephemeris value
        self.ephSunPosXEntry.focus_set()

#    def print_value(self):
#        print(rad.get())

#    def gray_it_out(self):
#        self.degrees.config(state=DISABLED)

#    def l_to_r(self):
#        self.radians.delete(0,END)
#        self.radians.insert(0,deg.get()*3.14159/180)
#        self.radians.config(state='readonly')
#        self.degrees.config(state='readonly')

root = Tk()

app = AcsGui(root)

root.mainloop()
