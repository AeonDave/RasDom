#!/usr/bin/env python

"""
Copyright (c) 2015 RasDom by Aeondave
See the file 'LICENSE' for copying permission
"""

import SocketServer, time
from lib import settings

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        print "Client connected with ", self.client_address
        x = ['W','e','l','c','o','m','e', ' ','t','o',' ','R','a','s','D','o','m',' ','i','n','t','e','r','f','a','c','e\r\n']
        for i in x:
            self.request.send(i)
            time.sleep(0.1)
        try:
            self.request.send("Insert Password\r\n")
            
            if self.request.recv(1024).strip() == settings.PASSWORD:
                time.sleep(1)
                self.request.send("Correct password\r\n")
    
                try:
                    self.request.send("Listening for commands\r\n")
                    self.data = self.request.recv(1024).strip()
                    
                    while self.data != 'exit':
                        self.data = self.request.recv(1024).strip()
                        
                finally:
                    self.request.close()
                    print "Client exited"
            
            else:
                time.sleep(1)
                self.request.send("Incorrect password\r\n")
                self.request.send("Bye\r\n")
        except:
            print "Connection interrupted"
            self.request.close()
            
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass