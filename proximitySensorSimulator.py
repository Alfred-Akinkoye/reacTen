""" Object class for the proximity Sensor Simulator"""

from numpy import interp
import numpy.random as rn

class proximitySensorSimulator():
    
    def __init__(self, idle = True):
        self.idle = idle    
    
    def status(self):
        return self.isSafe()
    
    def isSafe(self):
        proxsensor = [0, 1, 2]
        prob = [1, 0, 0]    
        errorMessa = int(rn.choice(proxsensor, 1, p = prob))            
        return errorMessa
    
    def turnOff(self):
        if (self.idle == False):
            return False        
        self.idle = False
        return True


    def turnOn(self):
        if (self.idle == True) :
            return False        
        self.idle = True
        return True    