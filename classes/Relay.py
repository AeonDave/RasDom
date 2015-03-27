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
            if self.test():
                print 'Test ok'
                self.set_status('on')
                
            else:
                print 'Test failed'
                self.set_status('test error')
        except:
            print 'Fatal error'
            self.set_status('fatal error. Run as Root')
        
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
    
    def on(self,i):
        print i
        GPIO.output(self.get_pins(), GPIO.HIGH)
    
    def off(self, i):
        print i
        GPIO.output(self.get_pins(), GPIO.LOW)
    
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
        return True 
