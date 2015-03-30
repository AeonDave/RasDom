#!/usr/bin/env python

"""
Copyright (c) 2015 RasDom by Aeondave
See the file 'LICENSE' for copying permission
"""

from classes import Relay
from classes import Server
import sys


def main():
    
    ComponentList = []
    
    rel1 = Relay.Relay() 
    rel1.test()
    rel1.set_note("Relay Cantina")

    ComponentList.append(rel1)
    
    Server.Server(ComponentList)
    
    print 'server ok'
    while 1:
        try:
            print 'Listening for commands'
            x = raw_input()
            print x
        except:
            print 'RasDom console terminated'
			rel1.gpio_unset()
            sys.exit()
            
if  __name__ =='__main__':
    main()
