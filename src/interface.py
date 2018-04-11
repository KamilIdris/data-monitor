# -*- coding: utf-8 -*-
"""
Main user interface

Updated 29th March 2018 by Kamil
"""

import tkinter as tk
from tkinter import TOP, LEFT, RIGHT, BOTH, RAISED, Y
from tkinter import NORMAL, END, DISABLED
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
import matplotlib.pyplot as plt

import sys
from time import localtime, strftime

from datastore import DataStore
from plclink import PLCLink

from settings import loginterval

class PlotWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.fig = plt.Figure()
        self.axes = self.fig.add_subplot(111)             
        self.plotcanvas = FigureCanvasTkAgg(self.fig)
        
        tbar = SimpleToolbar(self.plotcanvas, self)
        tbar.update()
        self.plotcanvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        
class ControlWidget(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
 
        # Options menu       
        mmenu = tk.Menu(self, tearoff=0)       
        mmenu.add_command(command=parent.logger, label="Begin logging")      
        mmenu.add_command(command=parent.setplot, label="Configure plot")
        
        mbtn = ttk.Menubutton(self, menu=mmenu, text="Menu", direction=RIGHT)        
        mbtn.pack(side=LEFT, padx=10, pady=4)

        # Text and scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y, pady=4)

        txtbox = tk.Text(self, height=2.1, yscrollcommand=scrollbar.set)
        txtbox.pack(fill=BOTH, expand=1, padx=4, pady=4)
        sys.stdout = RedirectTo(txtbox)
        scrollbar.config(command = txtbox.yview)   
        
class SimpleToolbar(NavigationToolbar2TkAgg):
    """
    Subclass and simplify the standard plot navigation toolbar
    """
    def __init__(self, canvas, parent):
        self.toolitems = (
            ('Home', 'Reset original view', 'home', 'home'),
            ('Pan', 'Pan with left mouse, zoom with right', 'move', 'pan'),
            ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
            ('Save', 'Save the figure', 'filesave', 'save_figure'),)
        NavigationToolbar2TkAgg.__init__(self, canvas, parent)
        
class RedirectTo(object):
    """
    Simple pipe redirector that is used to display stdout in the textbox.
    """
    def __init__(self, txtctrl):
        self.output = txtctrl

    def write(self, string):
        """
        Config state is toggled to from disabled to normal as it is normally
        locked from user entry
        """
        self.output.config(state=NORMAL)
        self.output.insert(END, string)
        self.output.see(END)
        self.output.config(state = DISABLED)
             
class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.datastore = DataStore()
        self.plclink = PLCLink()
        
        # Two frames, display frame and control frame
        displayfrm = PlotWidget(self, relief=RAISED, borderwidth=1)
        displayfrm.pack(fill=BOTH, expand=1)

        ctrlfrm = ControlWidget(self)
        ctrlfrm.pack(fill=BOTH, expand=1)
        
    def logger(self):
        try:
            data = self.plclink.getdata()
            self.datastore.insert(data)
        except:
            print("Logging failed on {}".format(strftime("%b %d %Y %H:%M:%S", 
                  localtime())))
        finally:
            # Log again after specified interval
            self.master.after(loginterval, self.logger)
    def setplot(self):
        pass    
        
def main():
    root = tk.Tk()
    root.title("Data Monitor")
    app = App(root)
    app.pack(side="top", fill="both", expand=True)   
    app.mainloop()

if __name__ == '__main__':
    main()