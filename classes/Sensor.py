#!/usr/bin/env python

"""
Copyright (c) 2015 RasDom by Aeondave
See the file 'LICENSE' for copying permission
"""

from Component import Component

class Sensor(Component): 
    def __init__(self): 
        Component.__init__(self)
        self.note = ""
    
    def get_note(self):
        return self.note

    def set_note(self, note):
        self.note = note