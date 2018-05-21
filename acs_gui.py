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

        att1RA = DoubleVar()
        att1Dec = DoubleVar()
        att1PA = DoubleVar()
        att1Quat1 = DoubleVar()
        att1Quat2 = DoubleVar()
        att1Quat3 = DoubleVar()
        att1Quat4 = DoubleVar()
        att1SunRoll = DoubleVar()
        att1SunPitch = DoubleVar()
        att1SunYaw = DoubleVar()

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

        self.att1Frame = ttk.Frame(master, relief='ridge')
        self.att1Frame.grid(row=2, column=0, padx=10, pady=10, ipadx=10, ipady=10, sticky=E+W)

        # Ephemeris Section---------------------------------------------------------------------------------------------

        # Ephemeris Top Level Layout---------------------------------------

        # Ephemeris Title
        self.ephemLabel = ttk.Label(self.ephFrame, text="Ephemeris")
        self.ephemLabel.grid(row=0, column=0, columnspan=3, padx=280, pady=10)

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

        # Ephemeris Position Frame - Details ------------------------------
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

        # Ephemeris Sun Vector Frame - Details-----------------------------
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

        # Ephemeris Normalized Sun Vector Frame - Details------------------

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

        # Attitude 1 Section--------------------------------------------------------------------------------------------

        # Attitude 1 Top Level Layout--------------------------------------

        # Attitude 1 Title
        self.att1Label = ttk.Label(self.att1Frame, text="Attitude 1")
        self.att1Label.grid(row=0, column=0, columnspan=3, padx=280, pady=10)

        # Attitude 1 Celestial Frame
        self.att1CelestFrame = ttk.Frame(self.att1Frame, relief='groove')
        self.att1CelestFrame.grid(row=1, column=0, ipadx=10, ipady=10)
        self.att1Frame.columnconfigure(2, weight=2)

        # Attitude 1 Button 1 Frame
        self.att1But1Frame = ttk.Frame(self.att1Frame)
        self.att1But1Frame.grid(row=1, column=1, ipadx=10, ipady=10)
        self.att1Frame.columnconfigure(1, weight=4)

        # Attitude 1 Quaternion Frame
        self.att1QuatFrame = ttk.Frame(self.att1Frame, relief='groove')
        self.att1QuatFrame.grid(row=1, column=2, ipadx=10, ipady=10)
        self.att1Frame.columnconfigure(0, weight=4)

        # Attitude 1 Button 2 Frame
        self.att1But2Frame = ttk.Frame(self.att1Frame)
        self.att1But2Frame.grid(row=1, column=3, ipadx=10, ipady=10)
        self.att1Frame.columnconfigure(3, weight=4)

        # Attitude 1 Celestial Frame
        self.att1SunAngFrame = ttk.Frame(self.att1Frame, relief='groove')
        self.att1SunAngFrame.grid(row=1, column=4, ipadx=10, ipady=10)
        self.att1Frame.columnconfigure(4, weight=2)

        # Clear att1
        self.att1ClearButton = ttk.Button(self.att1Frame, text="Clear", width=5, command=self.att1Clear)
        self.att1ClearButton.grid(row=1, column=5, padx=10)
        self.att1Frame.columnconfigure(5, weight=4)

        # Attitude 1 Celestial Frame - Details----------------------------
        self.att1CelestLabel = ttk.Label(self.att1CelestFrame, text="Celestial")
        self.att1CelestLabel.grid(row=0, column=0, columnspan=2, pady=5)

        self.att1RALabel = ttk.Label(self.att1CelestFrame, text="RA")
        self.att1RALabel.grid(row=1, column=0, padx=5)

        self.att1DecLabel = ttk.Label(self.att1CelestFrame, text="Dec")
        self.att1DecLabel.grid(row=2, column=0, padx=5)

        self.att1PALabel = ttk.Label(self.att1CelestFrame, text="PA")
        self.att1PALabel.grid(row=3, column=0, padx=5)

        self.att1RAEntry = ttk.Entry(self.att1CelestFrame, width=10, textvariable=att1RA)
        self.att1RAEntry.grid(row=1, column=1)

        self.att1DecEntry = ttk.Entry(self.att1CelestFrame, width=10, textvariable=att1Dec)
        self.att1DecEntry.grid(row=2, column=1)

        self.att1PAEntry = ttk.Entry(self.att1CelestFrame, width=10, textvariable=att1PA)
        self.att1PAEntry.grid(row=3, column=1)

        # Attitude 1 Button 1 Frame - Details-----------------------------

        # Button to Convert Celestial to Quaternion
        self.att1CelestToQuatButton = ttk.Button(self.att1But1Frame, text="▶", width=2, command=self.att1CelestToQuat)
        self.att1CelestToQuatButton.grid(row=1, column=1)

        # Button to Convert Quaternion to Celestial
        self.att1QuatToCelestButton = ttk.Button(self.att1But1Frame, text="◀", width=2, command=self.att1QuatToCelest)
        self.att1QuatToCelestButton.grid(row=2, column=1)

        # Attitude 1 Quaternion Frame - Details----------------------------
        self.att1QuatLabel = ttk.Label(self.att1QuatFrame, text="Quaternion")
        self.att1QuatLabel.grid(row=0, column=0, columnspan=2, pady=5)

        self.att1Quat1Label = ttk.Label(self.att1QuatFrame, text="q1")
        self.att1Quat1Label.grid(row=1, column=0, padx=5)

        self.att1Quat2Label = ttk.Label(self.att1QuatFrame, text="q2")
        self.att1Quat2Label.grid(row=2, column=0, padx=5)

        self.att1Quat3Label = ttk.Label(self.att1QuatFrame, text="q3")
        self.att1Quat3Label.grid(row=3, column=0, padx=5)

        self.att1Quat4Label = ttk.Label(self.att1QuatFrame, text="q4")
        self.att1Quat4Label.grid(row=4, column=0, padx=5)

        self.att1QuatXEntry = ttk.Entry(self.att1QuatFrame, width=10, textvariable=att1Quat1)
        self.att1QuatXEntry.grid(row=1, column=1)

        self.att1QuatYEntry = ttk.Entry(self.att1QuatFrame, width=10, textvariable=att1Quat2)
        self.att1QuatYEntry.grid(row=2, column=1)

        self.att1QuatZEntry = ttk.Entry(self.att1QuatFrame, width=10, textvariable=att1Quat3)
        self.att1QuatZEntry.grid(row=3, column=1)

        self.att1QuatZEntry = ttk.Entry(self.att1QuatFrame, width=10, textvariable=att1Quat4)
        self.att1QuatZEntry.grid(row=4, column=1)

        # Attitude 1 Button 2 Frame - Details-----------------------------

        # Button to Convert Celestial to Sun Angles
        self.att1CelestToSunAngBut = ttk.Button(self.att1But2Frame, text="▶", width=2, command=self.att1QuatToSunAng)
        self.att1CelestToSunAngBut.grid(row=1, column=1)

        # Button to Convert Sun Angles to Celestial
        self.att1CelestToSunAngBut = ttk.Button(self.att1But2Frame, text="◀", width=2, command=self.att1SunAngToQuat)
        self.att1CelestToSunAngBut.grid(row=2, column=1)

        # Attitude 1 Sun Angles Frame - Details---------------------------
        self.att1SunAngLabel = ttk.Label(self.att1SunAngFrame, text="Sun Angles")
        self.att1SunAngLabel.grid(row=0, column=0, columnspan=2, pady=5)

        self.att1SunRollLabel = ttk.Label(self.att1SunAngFrame, text="Sun Roll")
        self.att1SunRollLabel.grid(row=1, column=0, padx=5)

        self.att1SunPitchLabel = ttk.Label(self.att1SunAngFrame, text="Sun Pitch")
        self.att1SunPitchLabel.grid(row=2, column=0, padx=5)

        self.att1SunYawLabel = ttk.Label(self.att1SunAngFrame, text="Sun Yaw")
        self.att1SunYawLabel.grid(row=3, column=0, padx=5)

        self.att1SunRollEntry = ttk.Entry(self.att1SunAngFrame, width=10, textvariable=att1SunRoll)
        self.att1SunRollEntry.grid(row=1, column=1)

        self.att1SunPitchEntry = ttk.Entry(self.att1SunAngFrame, width=10, textvariable=att1SunPitch)
        self.att1SunPitchEntry.grid(row=2, column=1)

        self.att1SunYawEntry = ttk.Entry(self.att1SunAngFrame, width=10, textvariable=att1SunYaw)
        self.att1SunYawEntry.grid(row=3, column=1)
        self.att1SunYawEntry.delete(0,END)
        self.att1SunYawEntry.config(state='disable')

    # End Layout----------------------------------------------------------------------------------------------------

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

    def att1CelestToQuat(self):
        print('hi')

    def att1QuatToCelest(self):
        print('hi')

    def att1QuatToSunAng(self):
        print('hi')

    def att1SunAngToQuat(self):
        print('hi')

    def att1Clear(self):
        print('hi')

root = Tk()
root.title('ACS Conversion Tool')

app = AcsGui(root)

root.mainloop()
