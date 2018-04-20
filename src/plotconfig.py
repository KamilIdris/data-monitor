# -*- coding: utf-8 -*-
"""
Plot configuration child window

Updated 20th April 2018 by Kamil
"""

import tkinter as tk
from tkinter import ttk
from tkinter import TOP, LEFT, RIGHT, BOTTOM, BOTH, VERTICAL
from timedate import TimedateSelector

class PeriodSelector(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        # Tabbed interface to cater to different plot periods
        self.notebook = ttk.Notebook(self)
        tab1 = tk.Frame(self.notebook)
        tab2 = tk.Frame(self.notebook)
        tab3 = tk.Frame(self.notebook)
        
        self.timetab(tab1)
        self.notebook.add(tab1, text='Time period')
        
        self.ringtab(tab2)
        self.notebook.add(tab2, text='Ring number')
        
        self.livetab(tab3)
        self.notebook.add(tab3, text='Live plot')
        
        self.notebook.pack(fill=BOTH, pady=5, expand=1)
        
    def timetab(self, parent):
        
        leftside = tk.Frame(parent)
        leftside.pack(side=LEFT)
        tk.Label(leftside, text="Start time").pack(side=TOP)
        tk.Label(leftside, text="End time").pack(side=TOP)
        
        rightside = tk.Frame(parent)
        rightside.pack(side=LEFT)
        self.starttime = TimedateSelector(rightside)
        self.starttime.pack(side=TOP)
        self.endtime = TimedateSelector(rightside)
        self.endtime.pack(side=TOP)
            
    def ringtab(self, parent):
        leftside = tk.Frame(parent)
        leftside.pack(side=LEFT)
        tk.Label(leftside, text="Start ring number").pack(side=TOP)
        tk.Label(leftside, text="End ring number").pack(side=TOP)
        
        rightside = tk.Frame(parent)
        rightside.pack(side=LEFT)
        self.startring = tk.IntVar()
        tk.Entry(rightside, textvariable=self.startring).pack(side=TOP)
        self.endring = tk.IntVar()
        tk.Entry(rightside, textvariable=self.endring).pack(side=TOP)
        
        #TODO: Validate values 
    
    def livetab(self, parent):
        txt = tk.Label(parent, text="Make a live plot as data arrives")
        txt.pack(fill=BOTH, expand=True)
        
class VariableSelector(tk.Frame):
    def __init__(self, parent, varlist, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Implement canvas area with scrollbar
        self.canvas = tk.Canvas(self, borderwidth=0)
        self.canvas.pack(side=LEFT, expand=True)
        scrollbar = tk.Scrollbar(self, orient=VERTICAL, 
                                 command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Make scrollable area in the canvas
        self.scrollarea = tk.Frame(self.canvas)
        self.canvas.create_window((4,4), window=self.scrollarea, anchor=tk.NW)
        self.scrollarea.bind('<Configure>', self.onFrameConfigure)
        
        # Fill scroll area with variable names
        self._populate(varlist)
        
    def onFrameConfigure(self, event):       
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def _populate(self, varlist):
        self.cbvar, cbtn = [], []
        tk.Label(self.scrollarea, text="Plot variables").grid(row=0,
                column=0, columnspan=2)
        
        numrows = int(len(varlist)/2)

        for i in range(numrows):
            # Left column
            self.cbvar.append(tk.IntVar())
            cbtn.append(tk.Checkbutton(self.scrollarea, 
                                       variable=self.cbvar[2*i],
                                       text=varlist[2*i]))
            cbtn[2*i].grid(row=i+1, column=0, pady=2, sticky=tk.W)
            # Right column
            self.cbvar.append(tk.IntVar())
            cbtn.append(tk.Checkbutton(self.scrollarea, 
                                       variable=self.cbvar[2*i+1], 
                                       text=varlist[2*i+1]))
            cbtn[2*i+1].grid(row=i+1, column=1, pady=2, sticky=tk.W)
        
        # If varlist has an odd numbered length, there is still one more
        last = len(self.cbvar)
        if len(varlist) & 0x1:
            self.cbvar.append(tk.IntVar())
            cbtn.append(tk.Checkbutton(self.scrollarea, 
                                       variable=self.cbvar[last],
                                       text=varlist[last]))
            cbtn[last].grid(row=numrows+1, column=0, pady=2, sticky=tk.W)
      
class Confirmation(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        # Parent is rightside (frame), its master is PlotConfigurator
        okaybtn = tk.Button(self, text='Plot', 
                            command=parent.master.makeplot)
        okaybtn.pack(side=BOTTOM, padx=4, pady=4)
        
        cancelbtn = tk.Button(self, text='Cancel', 
                              command=parent.master.destroy)
        cancelbtn.pack(side=BOTTOM)

class PlotConfigurator(tk.Toplevel):
    def __init__(self, parent, varlist, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.parent = parent
        self.plotconfig = {}
        
        self.varconfig = VariableSelector(self, varlist) 
        self.varconfig.pack(side=LEFT, expand=True)
        
        rightside = tk.Frame(self)
        rightside.pack(side=LEFT)       
        self.action = Confirmation(rightside)
        self.action.pack(side=BOTTOM)
        self.periodconfig = PeriodSelector(rightside)
        self.periodconfig.pack(side=BOTTOM, expand=True, fill=tk.X)
               
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

def main():
    root = tk.Tk()

    window = PlotConfigurator(root, ['Var1', 'Var2', 'Var3'])

    window.mainloop()        
        
if __name__=='__main__':
    main()
                    
        
        
     
        
        
      
        
    