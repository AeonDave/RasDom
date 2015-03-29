#!/usr/bin/env python

"""
Copyright (c) 2015 RasDom by Aeondave
See the file 'LICENSE' for copying permission
"""

import RPi.GPIO as GPIO
from Component import Component

class Switch(Component): 
    def __init__(self): 
        Component.__init__(self)
        self.note = ""
    
    def get_note(self):
        return self.note

    def set_note(self, note):
        self.note = note
        
    def gpio_setup(self):
        print 'setup'
        GPIO.setup(self.get_pins(), GPIO.OUT)
        GPIO.output(self.get_pins(), GPIO.LOW)