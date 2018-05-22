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

        global att1RA, att1Dec, att1PA
        global att1Quat1, att1Quat2, att1Quat3, att1Quat4
        global att1SunRoll, att1SunPitch, att1SunYaw

        global att2RA, att2Dec, att2PA
        global att2Quat1, att2Quat2, att2Quat3, att2Quat4
        global att2SunRoll, att2SunPitch, att2SunYaw

        global slewMom, slewDur, slewAngRoll, slewAngPitch, slewAngYaw

        # Ephemeris Variables
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

        # Attitude 1 Variables
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

        # Attitude 2 Variables
        att2RA = DoubleVar()
        att2Dec = DoubleVar()
        att2PA = DoubleVar()
        att2Quat1 = DoubleVar()
        att2Quat2 = DoubleVar()
        att2Quat3 = DoubleVar()
        att2Quat4 = DoubleVar()
        att2SunRoll = DoubleVar()
        att2SunPitch = DoubleVar()
        att2SunYaw = DoubleVar()

        # Slew Variables
        slewMom = DoubleVar()
        slewDur = DoubleVar()
        slewAngRoll = DoubleVar()
        slewAngPitch = DoubleVar()
        slewAngYaw = DoubleVar()

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
        self.ephFrame.grid(row=1, column=0, padx=10, pady=2, ipadx=20, ipady=2, sticky=E+W)

        self.att1Frame = ttk.Frame(master, relief='ridge')
        self.att1Frame.grid(row=2, column=0, padx=10, pady=2, ipadx=20, ipady=2, sticky=E+W)

        self.att2Frame = ttk.Frame(master, relief='ridge')
        self.att2Frame.grid(row=3, column=0, padx=10, pady=2, ipadx=20, ipady=2, sticky=E+W)

        self.slewFrame = ttk.Frame(master, relief='ridge')
        self.slewFrame.grid(row=4, column=0, padx=10, pady=2, ipadx=20, ipady=2, sticky=E+W)

        # Ephemeris Section---------------------------------------------------------------------------------------------

        # Ephemeris Top Level Layout---------------------------------------

        # Ephemeris Title
        self.ephemLabel = ttk.Label(self.ephFrame, text="Ephemeris")
        self.ephemLabel.grid(row=0, column=0, columnspan=6, pady=2)

        # Ephemeris Position Frame
        self.ephPosFrame = ttk.Frame(self.ephFrame, relief='groove')
        self.ephPosFrame.grid(row=1, column=0, ipadx=10, ipady=2)
        self.ephFrame.columnconfigure(0, weight=4)

        # Button to Convert Positions to Sun Vector
        self.ephPosToVecButton = ttk.Button(self.ephFrame, text="▶", width=2, command=self.ephPosToVec)
        self.ephPosToVecButton.grid(row=1, column=1)
        self.ephFrame.columnconfigure(1, weight=1)

        # Ephemeris Sun Vector Frame
        self.ephSunVecFrame = ttk.Frame(self.ephFrame,relief='groove')
        self.ephSunVecFrame.grid(row=1, column=2, ipadx=10, ipady=2)
        self.ephFrame.columnconfigure(2, weight=2)

        # Convert sun vector to normalized sun vector
        self.ephVecToNormVecButton = ttk.Button(self.ephFrame, text="▶", width=2, command=self.ephVecToNormVec)
        self.ephVecToNormVecButton.grid(row=1, column=3)
        self.ephFrame.columnconfigure(3, weight=1)

        # Ephemeris Sun Vector Frame
        self.ephSunVecNormFrame = ttk.Frame(self.ephFrame,relief='groove')
        self.ephSunVecNormFrame.grid(row=1, column=4, ipady=2)
        self.ephFrame.columnconfigure(4, weight=3)

        # Clear ephem
        self.ephClearButton = ttk.Button(self.ephFrame, text="Clear", width=5, command=self.ephClear)
        self.ephClearButton.grid(row=1, column=5, padx=10)
        self.ephFrame.columnconfigure(0, weight=4)

        # Ephemeris Position Frame - Details ------------------------------

        self.ephPosLabel = ttk.Label(self.ephPosFrame, text="Positions (ECI, km)")
        self.ephPosLabel.grid(row=0, column=0, columnspan=3, pady=2)

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
        self.ephSunVecLabel.grid(row=0, column=0, columnspan=2, pady=2)

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
        self.ephSunVecNormLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=2)

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
        self.att1Label.grid(row=0, column=0, columnspan=6, padx=0, pady=2)

        # Attitude 1 Celestial Frame
        self.att1CelestFrame = ttk.Frame(self.att1Frame, relief='groove')
        self.att1CelestFrame.grid(row=1, column=0, ipadx=10, ipady=2)
        self.att1Frame.columnconfigure(0, weight=4)

        # Attitude 1 Button 1 Frame
        self.att1But1Frame = ttk.Frame(self.att1Frame)
        self.att1But1Frame.grid(row=1, column=1, ipady=2)
        self.att1Frame.columnconfigure(1, weight=1)

        # Attitude 1 Quaternion Frame
        self.att1QuatFrame = ttk.Frame(self.att1Frame, relief='groove')
        self.att1QuatFrame.grid(row=1, column=2, ipadx=10, ipady=2)
        self.att1Frame.columnconfigure(2, weight=4)

        # Attitude 1 Button 2 Frame
        self.att1But2Frame = ttk.Frame(self.att1Frame)
        self.att1But2Frame.grid(row=1, column=3, ipady=2)
        self.att1Frame.columnconfigure(3, weight=1)

        # Attitude 1 Celestial Frame
        self.att1SunAngFrame = ttk.Frame(self.att1Frame, relief='groove')
        self.att1SunAngFrame.grid(row=1, column=4, ipadx=10, ipady=2)
        self.att1Frame.columnconfigure(4, weight=2)

        # Clear att1
        self.att1ClearButton = ttk.Button(self.att1Frame, text="Clear", width=5, command=self.att1Clear)
        self.att1ClearButton.grid(row=1, column=5, padx=10)
        self.att1Frame.columnconfigure(5, weight=4)

        # Attitude 1 Celestial Frame - Details----------------------------

        self.att1CelestLabel = ttk.Label(self.att1CelestFrame, text="Celestial")
        self.att1CelestLabel.grid(row=0, column=0, columnspan=2, pady=2)

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
        self.att1QuatLabel.grid(row=0, column=0, columnspan=2, pady=2)

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

        # Button to Convert Quaternion to Sun Angles
        self.att1CelestToSunAngBut = ttk.Button(self.att1But2Frame, text="▶", width=2, command=self.att1QuatToSunAng)
        self.att1CelestToSunAngBut.grid(row=1, column=1)

        # Button to Convert Sun Angles to Quaternion
        self.att1CelestToSunAngBut = ttk.Button(self.att1But2Frame, text="◀", width=2, command=self.att1SunAngToQuat)
        self.att1CelestToSunAngBut.grid(row=2, column=1)

        # Attitude 1 Sun Angles Frame - Details---------------------------

        self.att1SunAngLabel = ttk.Label(self.att1SunAngFrame, text="Sun Angles")
        self.att1SunAngLabel.grid(row=0, column=0, columnspan=2, pady=2)

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

        # Attitude 2 Section--------------------------------------------------------------------------------------------

        # Attitude 2 Top Level Layout--------------------------------------

        # Attitude 2 Title
        self.att2Label = ttk.Label(self.att2Frame, text="Attitude 2")
        self.att2Label.grid(row=0, column=0, columnspan=6, padx=0, pady=2)

        # Attitude 2 Celestial Frame
        self.att2CelestFrame = ttk.Frame(self.att2Frame, relief='groove')
        self.att2CelestFrame.grid(row=1, column=0, ipadx=10, ipady=2)
        self.att2Frame.columnconfigure(0, weight=4)

        # Attitude 2 Button 1 Frame
        self.att2But1Frame = ttk.Frame(self.att2Frame)
        self.att2But1Frame.grid(row=1, column=1, ipady=2)
        self.att2Frame.columnconfigure(1, weight=1)

        # Attitude 2 Quaternion Frame
        self.att2QuatFrame = ttk.Frame(self.att2Frame, relief='groove')
        self.att2QuatFrame.grid(row=1, column=2, ipadx=10, ipady=2)
        self.att2Frame.columnconfigure(2, weight=4)

        # Attitude 2 Button 2 Frame
        self.att2But2Frame = ttk.Frame(self.att2Frame)
        self.att2But2Frame.grid(row=1, column=3, ipady=2)
        self.att2Frame.columnconfigure(3, weight=1)

        # Attitude 2 Celestial Frame
        self.att2SunAngFrame = ttk.Frame(self.att2Frame, relief='groove')
        self.att2SunAngFrame.grid(row=1, column=4, ipadx=10, ipady=2)
        self.att2Frame.columnconfigure(4, weight=2)

        # Clear att2
        self.att2ClearButton = ttk.Button(self.att2Frame, text="Clear", width=5, command=self.att2Clear)
        self.att2ClearButton.grid(row=1, column=5, padx=10)
        self.att2Frame.columnconfigure(5, weight=4)

        # Attitude 2 Celestial Frame - Details----------------------------

        self.att2CelestLabel = ttk.Label(self.att2CelestFrame, text="Celestial")
        self.att2CelestLabel.grid(row=0, column=0, columnspan=2, pady=2)

        self.att2RALabel = ttk.Label(self.att2CelestFrame, text="RA")
        self.att2RALabel.grid(row=1, column=0, padx=5)

        self.att2DecLabel = ttk.Label(self.att2CelestFrame, text="Dec")
        self.att2DecLabel.grid(row=2, column=0, padx=5)

        self.att2PALabel = ttk.Label(self.att2CelestFrame, text="PA")
        self.att2PALabel.grid(row=3, column=0, padx=5)

        self.att2RAEntry = ttk.Entry(self.att2CelestFrame, width=10, textvariable=att2RA)
        self.att2RAEntry.grid(row=1, column=1)

        self.att2DecEntry = ttk.Entry(self.att2CelestFrame, width=10, textvariable=att2Dec)
        self.att2DecEntry.grid(row=2, column=1)

        self.att2PAEntry = ttk.Entry(self.att2CelestFrame, width=10, textvariable=att2PA)
        self.att2PAEntry.grid(row=3, column=1)

        # Attitude 2 Button 1 Frame - Details-----------------------------

        # Button to Convert Celestial to Quaternion
        self.att2CelestToQuatButton = ttk.Button(self.att2But1Frame, text="▶", width=2, command=self.att2CelestToQuat)
        self.att2CelestToQuatButton.grid(row=1, column=1)

        # Button to Convert Quaternion to Celestial
        self.att2QuatToCelestButton = ttk.Button(self.att2But1Frame, text="◀", width=2, command=self.att2QuatToCelest)
        self.att2QuatToCelestButton.grid(row=2, column=1)

        # Attitude 2 Quaternion Frame - Details----------------------------

        self.att2QuatLabel = ttk.Label(self.att2QuatFrame, text="Quaternion")
        self.att2QuatLabel.grid(row=0, column=0, columnspan=2, pady=2)

        self.att2Quat1Label = ttk.Label(self.att2QuatFrame, text="q1")
        self.att2Quat1Label.grid(row=1, column=0, padx=5)

        self.att2Quat2Label = ttk.Label(self.att2QuatFrame, text="q2")
        self.att2Quat2Label.grid(row=2, column=0, padx=5)

        self.att2Quat3Label = ttk.Label(self.att2QuatFrame, text="q3")
        self.att2Quat3Label.grid(row=3, column=0, padx=5)

        self.att2Quat4Label = ttk.Label(self.att2QuatFrame, text="q4")
        self.att2Quat4Label.grid(row=4, column=0, padx=5)

        self.att2QuatXEntry = ttk.Entry(self.att2QuatFrame, width=10, textvariable=att2Quat1)
        self.att2QuatXEntry.grid(row=1, column=1)

        self.att2QuatYEntry = ttk.Entry(self.att2QuatFrame, width=10, textvariable=att2Quat2)
        self.att2QuatYEntry.grid(row=2, column=1)

        self.att2QuatZEntry = ttk.Entry(self.att2QuatFrame, width=10, textvariable=att2Quat3)
        self.att2QuatZEntry.grid(row=3, column=1)

        self.att2QuatZEntry = ttk.Entry(self.att2QuatFrame, width=10, textvariable=att2Quat4)
        self.att2QuatZEntry.grid(row=4, column=1)

        # Attitude 2 Button 2 Frame - Details-----------------------------

        # Button to Convert Quaternion to Sun Angles
        self.att2CelestToSunAngBut = ttk.Button(self.att2But2Frame, text="▶", width=2, command=self.att2QuatToSunAng)
        self.att2CelestToSunAngBut.grid(row=1, column=1)

        # Button to Convert Sun Angles to Quaternion
        self.att2CelestToSunAngBut = ttk.Button(self.att2But2Frame, text="◀", width=2, command=self.att2SunAngToQuat)
        self.att2CelestToSunAngBut.grid(row=2, column=1)

        # Attitude 2 Sun Angles Frame - Details---------------------------

        self.att2SunAngLabel = ttk.Label(self.att2SunAngFrame, text="Sun Angles")
        self.att2SunAngLabel.grid(row=0, column=0, columnspan=2, pady=2)

        self.att2SunRollLabel = ttk.Label(self.att2SunAngFrame, text="Sun Roll")
        self.att2SunRollLabel.grid(row=1, column=0, padx=5)

        self.att2SunPitchLabel = ttk.Label(self.att2SunAngFrame, text="Sun Pitch")
        self.att2SunPitchLabel.grid(row=2, column=0, padx=5)

        self.att2SunYawLabel = ttk.Label(self.att2SunAngFrame, text="Sun Yaw")
        self.att2SunYawLabel.grid(row=3, column=0, padx=5)

        self.att2SunRollEntry = ttk.Entry(self.att2SunAngFrame, width=10, textvariable=att2SunRoll)
        self.att2SunRollEntry.grid(row=1, column=1)

        self.att2SunPitchEntry = ttk.Entry(self.att2SunAngFrame, width=10, textvariable=att2SunPitch)
        self.att2SunPitchEntry.grid(row=2, column=1)

        self.att2SunYawEntry = ttk.Entry(self.att2SunAngFrame, width=10, textvariable=att2SunYaw)
        self.att2SunYawEntry.grid(row=3, column=1)
        self.att2SunYawEntry.delete(0,END)
        self.att2SunYawEntry.config(state='disable')

        # Slew Section--------------------------------------------------------------------------------------------------

        # Slew Top Level Layout--------------------------------------------

        # Slew Title
        self.slewLabel = ttk.Label(self.slewFrame, text="Slew")
        self.slewLabel.grid(row=0, column=0, columnspan=5, padx=0, pady=2)

        # Slew Momentum Frame
        self.slewMomFrame = ttk.Frame(self.slewFrame, relief='groove')
        self.slewMomFrame.grid(row=1, column=0, ipadx=10, ipady=2)
        self.slewFrame.columnconfigure(0, weight=4)

        # Calculate Slew
        self.slewButton = ttk.Button(self.slewFrame, text="▶", width=2, command=self.slew)
        self.slewButton.grid(row=1, column=1)
        self.slewFrame.columnconfigure(1, weight=1)

        # Slew Duration Frame
        self.slewDurFrame = ttk.Frame(self.slewFrame, relief='groove')
        self.slewDurFrame.grid(row=1, column=2, ipadx=10, ipady=2)
        self.slewFrame.columnconfigure(2, weight=4)

        # Slew Angles Frame
        self.slewAngFrame = ttk.Frame(self.slewFrame, relief='groove')
        self.slewAngFrame.grid(row=1, column=3, ipadx=10, ipady=2)
        self.slewFrame.columnconfigure(3, weight=2)

        # Clear slew
        self.slewClearButton = ttk.Button(self.slewFrame, text="Clear", width=5, command=self.slewClear)
        self.slewClearButton.grid(row=1, column=4, padx=10)
        self.slewFrame.columnconfigure(4, weight=4)

        # Slew Momentum Frame - Details-----------------------------------

        self.slewMomLabel = ttk.Label(self.slewMomFrame, text="Total System Momentum")
        self.slewMomLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=2)

        self.slewMomUnitLabel = ttk.Label(self.slewMomFrame, text="(N-m-s)")
        self.slewMomUnitLabel.grid(row=1, column=0, padx=5)

        self.slewMomEntry = ttk.Entry(self.slewMomFrame, width=10, textvariable=slewMom)
        self.slewMomEntry.grid(row=1, column=1)

        # Slew Duration Frame - Details-----------------------------------

        self.slewDurLabel = ttk.Label(self.slewDurFrame, text="Duration")
        self.slewDurLabel.grid(row=0, column=0, columnspan=2, pady=2)

        self.slewDurUnitLabel = ttk.Label(self.slewDurFrame, text="(min)")
        self.slewDurUnitLabel.grid(row=1, column=0, padx=5)

        self.slewDurEntry = ttk.Entry(self.slewDurFrame, width=10, textvariable=slewDur)
        self.slewDurEntry.grid(row=1, column=1)
        self.slewDurEntry.delete(0,END)
        self.slewDurEntry.config(state='readonly')

        # Slew Angles Frame - Details-------------------------------------

        self.slewAngLabel = ttk.Label(self.slewAngFrame, text="Sun Angles")
        self.slewAngLabel.grid(row=0, column=0, columnspan=2, pady=2)

        self.slewAngRollLabel = ttk.Label(self.slewAngFrame, text="Roll")
        self.slewAngRollLabel.grid(row=1, column=0, padx=5)

        self.slewAngPitchLabel = ttk.Label(self.slewAngFrame, text="Pitch")
        self.slewAngPitchLabel.grid(row=2, column=0, padx=5)

        self.slewAngYawLabel = ttk.Label(self.slewAngFrame, text="Yaw")
        self.slewAngYawLabel.grid(row=3, column=0, padx=5)

        self.slewAngRollEntry = ttk.Entry(self.slewAngFrame, width=10, textvariable=slewAngRoll)
        self.slewAngRollEntry.grid(row=1, column=1)
        self.slewAngRollEntry.delete(0,END)
        self.slewAngRollEntry.config(state='readonly')

        self.slewAngPitchEntry = ttk.Entry(self.slewAngFrame, width=10, textvariable=slewAngPitch)
        self.slewAngPitchEntry.grid(row=2, column=1)
        self.slewAngPitchEntry.delete(0,END)
        self.slewAngPitchEntry.config(state='readonly')

        self.slewAngYawEntry = ttk.Entry(self.slewAngFrame, width=10, textvariable=slewAngYaw)
        self.slewAngYawEntry.grid(row=3, column=1)
        self.slewAngYawEntry.delete(0,END)
        self.slewAngYawEntry.config(state='readonly')

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

    def att2CelestToQuat(self):
        print('hi')

    def att2QuatToCelest(self):
        print('hi')

    def att2QuatToSunAng(self):
        print('hi')

    def att2SunAngToQuat(self):
        print('hi')

    def att2Clear(self):
        print('hi')

    def slew(self):
        print('hi')

    def slewClear(self):
        print('hi')

root = Tk()
root.title('ACS Conversion Tool')

app = AcsGui(root)

root.mainloop()
