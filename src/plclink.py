# -*- coding: utf-8 -*-
"""
Interface to Profinet via Snap7

Updated 4th April 2018 by Kamil
"""

import snap7

import settings
import dblayout

def getDBList():
    return [x for x in dir(dblayout) if not x.startswith('__')]
 
class PLCLink(object):
    """
    Interface with PLC
    """
    def __init__(self):
        self.client = snap7.client.Client()
        self.dblist = getDBList()
                  
    def getdata(self):
        self.client.connect(settings.ip, 0, 2)

        data = []
        for x in self.dblist:
            raw = self.client.db_get(eval(x+'.dbnum'))
            # processed = snap7.util.DB(key, raw, )
            data.append(raw)
            
        self.client.disconnect()
        
        return data