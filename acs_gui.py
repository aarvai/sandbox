#  -*- coding: utf-8 -*-
"""
Created on Sat May 12 13:08:54 2018

@author: aarvai
"""

import numpy as np
from tkinter import Tk
from tkinter import Entry, DoubleVar, END, N, E, S, W
from tkinter import ttk

# Select tkinter style
# s = ttk.Style()
# print("Tkinter theme options are:")
# print(s.theme_names())
# print("Current Tkinter theme:")
# print(s.theme_use())
# s.theme_use('clam')


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

        # print("Tkinter theme options are:")
        # print(ttk.Style().theme_names())
        # print("Current Tkinter theme:")
        # print(ttk.Style().theme_use())
        # ttk.Style().theme_use('vista')
        print(ttk.Style().lookup("TButton", "font"))

        #ttk.Style().configure("TLabel", padding=10)
        #ttk.Style().configure("TEntry", padding=10)
        #print(ttk.Style().element_options('TButton'))

        # Title
        self.title = ttk.Label(text="ACS Conversion Tool")
        self.title.grid(row=0, column=0, columnspan=10)

        # Define top-level frames
        self.ephFrame = ttk.Frame(master, relief='ridge')
        self.ephFrame.grid(row=1, column=0, padx=10, pady=10, ipadx=10, ipady=10, sticky=E+W)

        # Ephemeris Section------------------------------------------------------------
        # Ephemeris Title
        self.ephemLabel = ttk.Label(self.ephFrame, text="Ephemeris")
        self.ephemLabel.grid(row=0, column=0, columnspan=6, padx=280, pady=10)

        # Ephemeris Position Frame
        self.ephPosFrame = ttk.Frame(self.ephFrame, relief='groove')
        self.ephPosFrame.grid(row=1, column=0, ipadx=10, ipady=10)
        self.ephFrame.columnconfigure(0, weight=4)

        # Button to Convert Positions to Sun Vector
        self.ephPosToVecButton = ttk.Button(self.ephFrame, text="▶", width=2, command=self.ephPosToVec)
        self.ephPosToVecButton.grid(row=1, column=1)
        self.ephFrame.columnconfigure(1, weight=1)

        # Ephemeris Sun Vector Frame
        self.ephSunVecFrame = ttk.Frame(self.ephFrame,relief='groove')
        self.ephSunVecFrame.grid(row=1, column=2, ipadx=10, ipady=10)
        self.ephFrame.columnconfigure(2, weight=2)

        # Convert sun vector to normalized sun vector
        self.ephVecToNormVecButton = ttk.Button(self.ephFrame, text="▶", width=2, command=self.ephVecToNormVec)
        self.ephVecToNormVecButton.grid(row=1, column=3)
        self.ephFrame.columnconfigure(3, weight=1)

        # Ephemeris Sun Vector Frame
        self.ephSunVecNormFrame = ttk.Frame(self.ephFrame,relief='groove')
        self.ephSunVecNormFrame.grid(row=1, column=4, ipady=10)
        self.ephFrame.columnconfigure(4, weight=3)

        # Clear ephem
        self.ephClearButton = ttk.Button(self.ephFrame, text="Clear", width=5, command=self.ephClear)
        self.ephClearButton.grid(row=1, column=5, padx=10)
        self.ephFrame.columnconfigure(0, weight=4)

        # Ephemeris Position Frame - Details
        self.ephPosLabel = ttk.Label(self.ephPosFrame, text="Positions (ECI, km)")
        self.ephPosLabel.grid(row=0, column=0, columnspan=3, pady=5)

        self.ephPosXLabel = ttk.Label(self.ephPosFrame, text="x")
        self.ephPosXLabel.grid(row=2, column=0, padx=5)

        self.ephPosYLabel = ttk.Label(self.ephPosFrame, text="y")
        self.ephPosYLabel.grid(row=3, column=0, padx=5)

        self.ephPosZLabel = ttk.Label(self.ephPosFrame, text="z")
        self.ephPosZLabel.grid(row=4, column=0, padx=5)

        self.ephSunLabel = ttk.Label(self.ephPosFrame, text="Sun")
        self.ephSunLabel.grid(row=1, column=1)

        self.ephSunPosXEntry = ttk.Entry(self.ephPosFrame, width=10, textvariable=ephSunPosX)
        self.ephSunPosXEntry.grid(row=2, column=1)
        self.ephSunPosXEntry.focus_set()

        self.ephSunPosYEntry = ttk.Entry(self.ephPosFrame, width=10, textvariable=ephSunPosY)
        self.ephSunPosYEntry.grid(row=3, column=1)

        self.ephSunPosZEntry = ttk.Entry(self.ephPosFrame, width=10, textvariable=ephSunPosZ)
        self.ephSunPosZEntry.grid(row=4, column=1)

        self.ephJwstLabel = ttk.Label(self.ephPosFrame, text="JWST")
        self.ephJwstLabel.grid(row=1, column=2)

        self.ephJwstPosXEntry = ttk.Entry(self.ephPosFrame, width=10, textvariable=ephJwstPosX)
        self.ephJwstPosXEntry.grid(row=2, column=2)

        self.ephJwstPosYEntry = ttk.Entry(self.ephPosFrame, width=10, textvariable=ephJwstPosY)
        self.ephJwstPosYEntry.grid(row=3, column=2)

        self.ephJwstPosZEntry = ttk.Entry(self.ephPosFrame, width=10, textvariable=ephJwstPosZ)
        self.ephJwstPosZEntry.grid(row=4, column=2)

        # Ephemeris Sun Vector Frame - Details
        self.ephSunVecLabel = ttk.Label(self.ephSunVecFrame, text="Sun Vector")
        self.ephSunVecLabel.grid(row=0, column=0, columnspan=2, pady=5)

        self.ephSunVecUnitLabel = ttk.Label(self.ephSunVecFrame, text="(ECI, km)")
        self.ephSunVecUnitLabel.grid(row=1, column=0, columnspan=2)

        self.ephSunVecXLabel = ttk.Label(self.ephSunVecFrame, text="x")
        self.ephSunVecXLabel.grid(row=2, column=0, padx=5)

        self.ephSunVecYLabel = ttk.Label(self.ephSunVecFrame, text="y")
        self.ephSunVecYLabel.grid(row=3, column=0, padx=5)

        self.ephSunVecZLabel = ttk.Label(self.ephSunVecFrame, text="z")
        self.ephSunVecZLabel.grid(row=4, column=0, padx=5)

        self.ephSunVecXEntry = ttk.Entry(self.ephSunVecFrame, width=10, textvariable=ephSunVecX)
        self.ephSunVecXEntry.grid(row=2, column=1)

        self.ephSunVecYEntry = ttk.Entry(self.ephSunVecFrame, width=10, textvariable=ephSunVecY)
        self.ephSunVecYEntry.grid(row=3, column=1)

        self.ephSunVecZEntry = ttk.Entry(self.ephSunVecFrame, width=10, textvariable=ephSunVecZ)
        self.ephSunVecZEntry.grid(row=4, column=1)

        # Ephemeris Normalized Sun Vector Frame - Details
        self.ephSunVecNormLabel = ttk.Label(self.ephSunVecNormFrame, text="Sun Vector Normalized")
        self.ephSunVecNormLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.ephSunVecNormUnitLabel = ttk.Label(self.ephSunVecNormFrame, text="(ECI, unitless)")
        self.ephSunVecNormUnitLabel.grid(row=1, column=0, columnspan=2)

        self.ephSunVecNormXLabel = ttk.Label(self.ephSunVecNormFrame, text="x")
        self.ephSunVecNormXLabel.grid(row=2, column=0)

        self.ephSunVecNormYLabel = ttk.Label(self.ephSunVecNormFrame, text="y")
        self.ephSunVecNormYLabel.grid(row=3, column=0)

        self.ephSunVecNormZLabel = ttk.Label(self.ephSunVecNormFrame, text="z")
        self.ephSunVecNormZLabel.grid(row=4, column=0)

        self.ephSunVecNormXEntry = ttk.Entry(self.ephSunVecNormFrame, width=10, textvariable=ephSunVecNormX)
        self.ephSunVecNormXEntry.grid(row=2, column=1)

        self.ephSunVecNormYEntry = ttk.Entry(self.ephSunVecNormFrame, width=10, textvariable=ephSunVecNormY)
        self.ephSunVecNormYEntry.grid(row=3, column=1)

        self.ephSunVecNormZEntry = ttk.Entry(self.ephSunVecNormFrame, width=10, textvariable=ephSunVecNormZ)
        self.ephSunVecNormZEntry.grid(row=4, column=1)

#         self.l2 = ttk.Label(text="Radians")
#         self.l2.grid(row=0, column=2)

#         self.radians = ttk.Entry(master, width=10, textvariable=rad)
#         self.radians.grid(row=1, column=2)

#         self.button1 = ttk.Button(master, text="Print Value", command=self.print_value)
#         self.button1.grid(row=0, column=3, rowspan=2)

#         self.button2 = ttk.Button(master, text="Gray it out", command=self.gray_it_out)
#         self.button2.grid(row=0, column=4, rowspan=2)

#         self.button3 = ttk.Button(master, text="QUIT", command=master.quit)
#         self.button3.grid(row=0, column=5, rowspan=2)

    def ephPosToVec(self):

        # clear sunVec
        self.ephSunVecXEntry.delete(0,END)
        self.ephSunVecYEntry.delete(0,END)
        self.ephSunVecZEntry.delete(0,END)

        # sun vector = sun position - JWST position
        self.ephSunVecXEntry.insert(0,ephSunPosX.get()-ephJwstPosX.get())
        self.ephSunVecYEntry.insert(0,ephSunPosY.get()-ephJwstPosY.get())
        self.ephSunVecZEntry.insert(0,ephSunPosZ.get()-ephJwstPosZ.get())

        # disable sun position
        self.ephSunPosXEntry.config(state='readonly')
        self.ephSunPosYEntry.config(state='readonly')
        self.ephSunPosZEntry.config(state='readonly')

        #  disable JWST position
        self.ephJwstPosXEntry.config(state='readonly')
        self.ephJwstPosYEntry.config(state='readonly')
        self.ephJwstPosZEntry.config(state='readonly')

        #  disable sun vector
        self.ephSunVecXEntry.config(state='readonly')
        self.ephSunVecYEntry.config(state='readonly')
        self.ephSunVecZEntry.config(state='readonly')

    def ephVecToNormVec(self):

        # clear sunVec
        self.ephSunVecNormXEntry.delete(0,END)
        self.ephSunVecNormYEntry.delete(0,END)
        self.ephSunVecNormZEntry.delete(0,END)

        # normalize sun vector
        ephSunVec = np.array([ephSunVecX.get(), ephSunVecY.get(), ephSunVecZ.get()])
        ephSunVecNorm = ephSunVec / np.linalg.norm(ephSunVec)
        self.ephSunVecNormXEntry.insert(0,ephSunVecNorm[0])
        self.ephSunVecNormYEntry.insert(0,ephSunVecNorm[1])
        self.ephSunVecNormZEntry.insert(0,ephSunVecNorm[2])

        #  disable sun vector
        self.ephSunVecXEntry.config(state='readonly')
        self.ephSunVecYEntry.config(state='readonly')
        self.ephSunVecZEntry.config(state='readonly')

        #  disable normalized sun vector
        self.ephSunVecNormXEntry.config(state='readonly')
        self.ephSunVecNormYEntry.config(state='readonly')
        self.ephSunVecNormZEntry.config(state='readonly')

    def ephClear(self):

        # re-enable all ephemeris values
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

        # clear all ephemeris values
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

        # Set the focus to the first ephemeris value
        self.ephSunPosXEntry.focus_set()

#     def print_value(self):
#         print(rad.get())

#     def gray_it_out(self):
#         self.degrees.config(state=DISABLED)

#     def l_to_r(self):
#         self.radians.delete(0,END)
#         self.radians.insert(0,deg.get()*3.14159/180)
#         self.radians.config(state='readonly')
#         self.degrees.config(state='readonly')

root = Tk()
root.title('ACS Conversion Tool')

app = AcsGui(root)

root.mainloop()
