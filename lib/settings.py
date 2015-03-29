#!/usr/bin/env python

"""
Copyright (c) 2015 RasDom by Aeondave
See the file 'LICENSE' for copying permission
"""

import os ,sys
#import RPi.GPIO as GPIO

VERSION = "0.1 alfa"
AUTHOR = "AeonDave"
DESCRIPTION = "RasDom or Raspberry Domotica"
SITE = ""
ISSUES_PAGE = ""
GIT_REPOSITORY = ""

#GPIO Relay
#GPIOMODE = GPIO.BCM
SLEEPTIME = 0.5
PINS = [17,18]
PINS_NAMES = ['Cancello','Portone']

#socket
PORT=4242
HOSTNAME=''
PASSWORD='123'

#general
PLATFORM = os.name
ROOTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
LIBDIR = os.path.abspath(os.path.dirname(__file__))
PYVERSION = sys.version.split()[0]
