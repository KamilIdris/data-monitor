# -*- coding: utf-8 -*-
"""
SQLite interface for data storage

Updated 11th April 2018 by Kamil
"""

import dataset
from time import localtime, strftime
 
class DataStore(object):
    """
    The DataStore is used to handle all connections with the SQLite database 
    """
    def __init__(self):
        self.updatedbname()
    
    def updatedbname(self):
        """
        DB name is based on current date, this ensures file
        """
        identifier = strftime('%Y%m%d', localtime())
        self.dbname = 'sqlite:///db/' + identifier + '.db'
        
    def insert(self, data):
        """
        Inserts additional data into the data store
        """
        self.updatedbname()
        
        with dataset.connect(self.dbname) as tx:
            tx['tbl'].insert(data)
            
    def read(self):
        pass