#!/usr/bin/env python

"""
Copyright (c) 2015 RasDom by Aeondave
See the file 'LICENSE' for copying permission
"""

import RPi.GPIO as GPIO
from lib import settings

class Component(object): 
    def __init__(self): 
        self.gpiomode = settings.GPIOMODE 
        self.pins = settings.PINS 
        self.pins_names = settings.PINS_NAMES
        self.status = 'on'

    def gpio_initialization(self):
        print 'init'
        GPIO.setmode(self.gpiomode)
        
    def gpio_unset(self):
        print 'unset'
        GPIO.cleanup()
    