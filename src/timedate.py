# -*- coding: utf-8 -*-
"""
Date time picker

Updated 19th April 2018 by Kamil
"""

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class Timebox(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        """
        Row of comboboxes for inputting time
        """
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        tk.Label(self, text="Hours").grid(row=0, column=0)
        self.hr = tk.StringVar()
        hrbox = ttk.Combobox(self, textvariable=self.hr, justify=tk.CENTER,
                              width=6, state='readonly', 
                              values=["{:02d}".format(x) for x in range(25)])
        hrbox.grid(row=1, column=0, padx=2)

        tk.Label(self, text="Minutes").grid(row=0, column=1)
        self.min = tk.StringVar()
        minbox = ttk.Combobox(self, textvariable=self.min, justify=tk.CENTER,
                               width=6, state='readonly', 
                               values=["{:02d}".format(x) for x in range(61)])
        minbox.grid(row=1, column=1, padx=2)

        tk.Label(self, text="Seconds").grid(row=0, column=2)
        self.sec = tk.StringVar()
        secbox = ttk.Combobox(self, textvariable=self.sec, justify=tk.CENTER,
                               width=6, state='readonly', 
                               values=["{:02d}".format(x) for x in range(61)])
        secbox.grid(row=1, column=2, padx=2)
        
    def get(self):
        return (self.hr.get().zfill(2) + ":" + self.min.get().zfill(2) 
                + ":" + self.sec.get().zfill(2))

class TimedateSelector(tk.Frame):
    """
    Merge Timebox and Calendar widgets to form complete Time & Date selector
    """
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
               
        self.time = Timebox(parent).pack(side=tk.TOP, padx=4, pady=4)
        self.date = DateEntry(parent).pack(side=tk.TOP, pady=4)
        
    def get(self):
        return self.date.selection_get() + self.time.get()
        
def main():
    root = tk.Tk()
    
    TimedateSelector(root)
    
    root.mainloop()
    

if __name__=='__main__':
    main()
    

