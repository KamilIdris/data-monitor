# -*- coding: utf-8 -*-
"""
SQLite interface for data storage

Updated 2nd March 2018 by Kamil
"""

import dataset
   
class DataStore(object):
    """
    The DataStore is used to handle all connections with the SQLite database 
    """
    def __init__(self, dbname='data'):
        self.dbname = dbname
        
    def insert(self, data):
        """
        Inserts additional data into the data store
        """
        with dataset.connect(self.dbname) as tx:
            tx['tbl'].insert(data)