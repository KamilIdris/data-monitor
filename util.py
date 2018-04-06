# -*- coding: utf-8 -*-
"""
Utility functions for use in the program

Updated 5th March 2018 by Kamil
"""

from dbfread import DBF
import dataset

def create_varlist():
    """
    Utility to parse uk_Measurement.DBF to get the list of variables 
    """
    try:
        sourcetable = DBF('uk_Measurement.DBF')
        
        db = dataset.connect('varlist.sqlite')
        desttable = db['tbl']
        
        for record in sourcetable:
            desttable.insert(record)
    
    except:
        print("Unable to create variable list")
