#!/usr/bin/env python

"""
Copyright (c) 2015 RasDom by Aeondave
See the file 'LICENSE' for copying permission
"""

import SocketServer, time
from lib import settings

ACK = "\x06"
SIZE = 1024

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        
        print "Client connected with ", self.client_address
        x = ['W','e','l','c','o','m','e', ' ','t','o',' ','R','a','s','D','o','m',' ','i','n','t','e','r','f','a','c','e\r\n']
        for i in x:
            self.request.send(i)
            time.sleep(0.1)
        self.request.send("Insert Password\r\n")
        password = self.request.recv(SIZE)
        self.request.send(ACK)
        
        if password == settings.PASSWORD:
            
            while self.request.recv(SIZE) != "e":
                
                self.request.send("\n\n---------------------\r\n")
                self.request.send("Listening for commands\r\n")
                self.request.send("1: Connected devices list\r\n")
                self.request.send("2: Select device\r\n")
                self.request.send("3: Device functions\r\n")
                self.request.send("e: Close connection\r\n")
                self.request.send("---------------------\r\n\n")    
            
                data = self.request.recv(SIZE)
                self.request.send(ACK)
                self.request.send("\n")
    
                if data == "1":
                    self.request.send(str(len(self.server.get_componentlist()))+" Components loaded\r\n")
                    c=0
                    for i in self.server.get_componentlist():
                        self.request.send(str(str(c)+": "+i.get_note()+"\r\n"))
                        c=c+1
                if data == "2":
                    if self.server.get_current_component() is None:
                        current_component = "None"
                    else:
                        current_component = self.server.get_current_component()
                    self.request.send("Selected component: "+current_component+"\r\n")
                    self.request.send("Select component id form connected devices\r\n")
                    component = self.request.recv(SIZE)
                    component = self.request.recv(SIZE)
                    self.request.send(ACK)
                    self.request.send("\n")
                    if component is not None:
                        self.server.set_current_component(str(component))
                if data == "3":
                    if self.server.get_current_component() is not None:

                        components = self.server.get_componentlist()
                        current_component = self.server.get_current_component()
                        component = components[int(current_component)]

                        self.request.send("Device selected: "+current_component+ " "+ component.get_note()+"\n\r")
                        self.request.send("Select id function:\n\r")
                        
                        c = 0
                        for i in component.get_functions():
                            self.request.send(str(c)+": "+i+"\n\r")
                            c = c+1
                        function = self.request.recv(SIZE)
                        function = self.request.recv(SIZE)
                        self.request.send(ACK)
                        self.request.send("\n")
                        
                        if function is not None:
                            self.server.set_current_function(str(function))

                        if len(component.get_pins_name())>1:
                            self.request.send("Select id object to " +str(component.get_functions()[int(function)])+ "\n\r")
                            c = 0
                            for i in component.get_pins_name():
                                self.request.send(str(c)+": "+str(i)+"\n\r")
                                c = c+1
                            pin = self.request.recv(SIZE)
                            pin = self.request.recv(SIZE)
                            self.request.send(ACK)
                            self.request.send("\n")
                            
                        else:
                            pin = 0
                        
                        component.launch_function(str(self.server.get_current_function()), int(pin))
                        self.request.send("Function Launched\n\r")
                        
                        
                    else:
                        self.request.send("No divice selected\n\r")
                            
                if data == "0":
                    break
        else:
            print "Password Wrong"
            self.request.close()
            
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    
    allow_reuse_address = True
    
    def set_componentlist(self, ComponentList):
        self.ComponentList = ComponentList
        
    def get_componentlist(self):
        return self.ComponentList
    
    def set_current_component(self, current_component):
        self.current_component = current_component
        
    def get_current_component(self):
        return self.current_component
    
    def set_current_function(self, current_function):
        self.current_function = str(current_function)
        
    def get_current_function(self):
        return self.current_function