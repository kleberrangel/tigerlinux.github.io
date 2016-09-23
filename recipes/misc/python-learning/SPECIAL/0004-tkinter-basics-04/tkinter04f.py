#!/usr/bin/env python
#
# By Reynaldo R. Martinez P.
# Sept 23, 2016
# TigerLinux AT Gmail DOT Com
# Buttons and Message BOXES arrangment - basic
# 
#

import sys

if sys.version_info.major == 2:
    # from Tkinter import Button, mainloop
    # import Tkinter as tkinter
    from Tkinter import *
else:
    # from tkinter import Button, mainloop
    # import tkinter
    from tkinter import *

# In this example, we'll define a class application, and
# use it with 3 buttons, two of them printing messages to
# the console, and the central one exiting the program


# This is our application class:
class MyMainApp:
    # Constructor:
    def __init__(self, windowobj):
        # The button call's uses the "windowobj" instance of class "Tk()".
        # This time we'll use the "anchor" option in order to force the buttons to "anchor" themselves to a
        # specific "cardinal point", mean: n,s,e,w, nw, ne, se, sw, and center:
        Button(windowobj, text='Top-Left - NW',command=(lambda:sys.stdout.write('Top-Left button pressed\n'))).pack(anchor=NW, side=TOP)
        Button(windowobj, text='CLICK HERE TO EXIT - CENTER',command=(lambda:sys.exit("Program ended normally !!"))).pack(anchor=CENTER, side=TOP)
        Button(windowobj, text='Bottom-Right - SE',command=(lambda:sys.stdout.write('Bottom-Right button pressed\n'))).pack(anchor=SE, side=TOP)

# We init a "Tk" instance:
mainwindow = Tk()
# Add options for the font:
mainwindow.option_add('*font', ('verdana', 12, 'bold'))
# ... and the window title...
mainwindow.title("Main Window")


# Then, we create an instance object with the "mainwindow" class instance of "Tk()" class
# and pass to the MyMainApp class the mainwindow instance which will be used by the buttons
# inside the MyMainApp instance (mydisplay here):

mydisplay = MyMainApp(mainwindow)

# Finally, our message loop:

mainwindow.mainloop()

# END
