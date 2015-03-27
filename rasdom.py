#!/usr/bin/env python

"""
Copyright (c) 2015 RasDom by Aeondave
See the file 'LICENSE' for copying permission
"""

from classes import Relay
from classes import Socket
from lib import settings

import threading, sys

def main():
    r = Relay.Relay() 
    print 'Rele status: ' + str(r.get_status())
    if r.get_status()=='on':
        print 'Starting Server on port 4242'
        server = Socket.ThreadedTCPServer((settings.HOSTNAME,settings.PORT), Socket.ThreadedTCPRequestHandler)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
    while 1:
        try:
            print 'Listening for commands'
            x = raw_input()
            print x
        except:
            print 'RasDom console terminated'
            sys.exit()
            
if  __name__ =='__main__':
    main()