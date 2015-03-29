'''
Created on 28/mar/2015

@author: Davide
'''

import Socket
import threading
from lib import settings

class Server(): 
    def __init__(self, ComponentList):
        self.ComponentList = ComponentList
        self.current_component = None
        self.current_function = None
        self.server = Socket.ThreadedTCPServer((settings.HOSTNAME,settings.PORT), Socket.ThreadedTCPRequestHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start() 
        self.server.set_componentlist(self.ComponentList)
        self.server.set_current_component(self.current_component)
    
    def set_current_component(self, current_component):
        self.current_component = current_component
        
    def get_current_component(self):
        return self.current_component
    
    def set_current_function(self, current_function):
        self.current_function = current_function
        
    def get_current_function(self):
        return self.current_function
    
    def set_componentlist(self, ComponentList):
        self.ComponentList = ComponentList
        
    def get_componentlist(self):
        return self.ComponentList