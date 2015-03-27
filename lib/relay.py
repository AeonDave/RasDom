#!/usr/bin/env python

"""
Copyright (c) 2015 RasDom by Aeondave
See the file 'LICENSE' for copying permission
"""

import RPi.GPIO as GPIO
import time
from lib.settings import SLEEPTIME

def setup(pin, gpiomode):
    GPIO.setmode(gpiomode)
    try:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        test(pin)
    except:
        print "error"
    
def test(pin):
    try:
        for i in pin:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(SLEEPTIME);
        for i in pin:
            GPIO.output(i, GPIO.LOW)
            time.sleep(SLEEPTIME);  
        return True
    except:
        print "error"
        
def unset():
    GPIO.cleanup()
    print "[+] GPIO ports resetted."
    
def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    
def off(pin):
    GPIO.output(pin, GPIO.LOW)
    
def activation(pin):
    on(pin)
    time.sleep(SLEEPTIME);
    off(pin)
    print "[+]"