# -*- coding: utf-8 -*-
"""
Plot configuration child window

Updated 17th April 2018 by Kamil
"""

import tkinter as tk
from tkinter import ttk
from tkinter import TOP, LEFT, RIGHT, BOTTOM, BOTH, VERTICAL

class PeriodSelector(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        # Tabbed interface to cater to different plot periods
        self.notebook = ttk.Notebook(self).pack(fill=BOTH, pady=5, expand=1)
        
        tab1 = tk.Frame(self.notebook)
        tab2 = tk.Frame(self.notebook)
        tab3 = tk.Frame(self.notebook)
        
        self.timetab(tab1)
        self.notebook.add(tab1, text='Time period')
        
        self.ringtab(tab2)
        self.notebook.add(tab2, text='Ring number')
        
        self.liveTab(tab3)
        self.notebook.add(tab3, text='Live plot')
        
    def timetab(self, parent):
        top = tk.Frame(parent).pack(side=TOP, expand=1)
        middle = tk.Frame(parent).pack(side=TOP, expand=1)
        bottom = tk.Frame(parent).pack(side=TOP, expand=1)     
        pass
    
    def ringtab(self, parent):
        pass
    
    def livetab(self, parent):
        pass
        
class VariableSelector(tk.Frame):
    def __init__(self, parent, varlist, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Implement canvas area with scrollbar
        canvas = tk.Canvas(self, borderwidth=0).pack(side=LEFT, expand=1)
        scrollbar = tk.Scrollbar(self, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Make scrollable area in the canvas
        scrollarea = tk.Frame(canvas)
        canvas.create_window((4,4), window=scrollarea, anchor=tk.NW)
        self.scrollarea.bind('<Configure>', self.onFrameConfigure)
        
        # Fill scroll area with variable names
        self.populate(varlist)
        
    def populate(self, varlist):
        self.cbvar, cbtn = [], []
        tk.Label(self.varframe, text="Plot variables").grid(row=0,
                     column=0, columnspan=2)
        
        numrows = int(len(varlist)/2)

        for i in range(numrows):
            # Left column
            self.cbvar.append(tk.IntVar())
            cbtn.append(tk.Checkbutton(self.scrollarea, 
                                       variable=self.cbvar[2*i],
                                       text=self.varlist[2*i]))
            cbtn[2*i].grid(row=i+1, column=0, pady=2, sticky=tk.W)
            # Right column
            self.cbvar.append(tk.IntVar())
            cbtn.append(tk.Checkbutton(self.scrollarea, 
                                       variable=self.cbvar[2*i+1], 
                                       text=self.varlist[2*i+1]))
            cbtn[2*i+1].grid(row=i+1, column=1, pady=2, sticky=tk.W)
        
        # If varlist has an odd numbered length, there is still one more
        last = len(self.cbvar)
        if len(self.varlist) & 0x1:
            self.cbvar.append(tk.IntVar())
            cbtn.append(tk.Checkbutton(self.scrollarea, 
                                       variable=self.cbvar[last],
                                       text=self.varlist[last]))
            cbtn[last].grid(row=numrows+1, column=0, pady=2, sticky=tk.W)
      
class Confirmation(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        # Note double parent in commands so as to refer to PlotConfigurator
        okaybtn = tk.Button(self, text='Plot', 
                            command=parent.parent.makeplot)
        okaybtn.pack(side=BOTTOM, padx=4, pady=4)
        
        cancelbtn = tk.Button(self, text='Cancel', 
                              command=parent.parent.destroy)
        cancelbtn.pack(side=BOTTOM)

class PlotConfigurator(tk.Toplevel):
    def __init__(self, parent, varlist, *args, **kwargs):
        tk.Toplevel(self, parent, varlist, *args, **kwargs)
        self.parent = parent
        self.plotconfig = {}
        
        leftside = tk.Frame(self).pack(side=LEFT, expand = 1)
        rightside = tk.Frame(self).pack(side=LEFT)
        bottomright = tk.Frame(rightside).pack(side=BOTTOM)
        topright = tk.Frame(rightside).pack(side=BOTTOM, fill=tk.X)

        self.varconfig = VariableSelector(leftside, varlist)        
        self.periodconfig = PeriodSelector(topright)
        self.action = Confirmation(bottomright)
                       
    def makeplot(self):
        # Save plot config and do plot here
        nb = self.periodconfig.notebook
        periodtype = nb.tab(nb.select())
        
        if periodtype == 1:
            pass
        elif periodtype == 2:
            pass
        elif periodtype ==3:
            pass
            
            
            

        
        
        
     
        
        
      
        
    