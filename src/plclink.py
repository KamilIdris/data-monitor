# -*- coding: utf-8 -*-
"""
Interface to Profinet via Snap7

Updated 20th April 2018 by Kamil
"""

import dblayout
import snap7
import settings
from time import strftime, localtime

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
        for x in ['dblayout.'+self.dblist]:
            dbnum = eval(x+'["dbnum"]')
            rawbytes = self.client.db_get(dbnum)
            row = snap7.util.DB(dbnum, rawbytes, eval(x+'["layout"]'),
                                eval(x+'.size'), eval(x+'["numrows"]'),
                                layout_offset = eval(x+'["layoutoffset"]'),
                                db_offset = eval(x+'["dboffset"]'))
            row['Time'] = strftime("%b %d %Y %H:%M:%S", localtime())
            data.append(row)
            
        self.client.disconnect()
        
        return data