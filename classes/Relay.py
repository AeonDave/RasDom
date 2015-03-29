#!/usr/bin/env python

"""
Copyright (c) 2015 RasDom by Aeondave
See the file 'LICENSE' for copying permission
"""

import time
import RPi.GPIO as GPIO
from lib import settings
from Switch import Switch
from Component import Component

class Relay(Switch): 
    def __init__(self): 
        Switch.__init__(self)
        self.sleeptime = settings.SLEEPTIME
        try:
            Component.gpio_initialization(self)
            Switch.gpio_setup(self)
            self.set_status('on')
        except:
            print 'Fatal error. Run as Root'
            self.set_status('fatal error')
        
    def get_sleeptime(self):
        return self.sleeptime
    
    def get_gpiomode(self):
        return self.gpiomode
    
    def get_pins(self):
        return self.pins

    def get_pins_name(self):
        return self.pins_names

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def set_gpiomode(self, gpiomode):
        self.get_gpiomode = gpiomode
        
    def set_pins(self, pins):
        self.pins = pins
        
    def set_pins_name(self, names):
        self.pins_names = names
    
    def set_sleeptime(self, sleeptime):
        self.sleeptime = sleeptime
    
    def on(self,pins):
        print str(pins)+ ' on'
        GPIO.output(pins, GPIO.HIGH)
    
    def off(self, pins):
        print str(pins)+ ' off'
        GPIO.output(pins, GPIO.LOW)
    
    def activation(self, pins):
        self.on(pins)
        time.sleep(self.get_sleeptime());
        self.off(pins)
        
    def test(self):
        for i in self.get_pins():
            self.on(i)
            time.sleep(self.get_sleeptime());
        for i in self.get_pins():
            self.off(i)
            time.sleep(self.get_sleeptime());  
            
    def get_functions(self):
        functions = ['activate']
        return functions
        
    def launch_function(self, function, pin):
        if function == "0":
            print "Activating"
            self.activation(pin)
