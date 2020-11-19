OFF = 0
LOWLIMIT = 40
HIGHLIMIT = 100


class ballShooter:
    """Constructor for the class"""
    def __init__(self, idle = False, lowLimit = LOWLIMIT, highLimit = HIGHLIMIT, currSpeed = OFF):
        self.idle= idle
        self.lowLimit = lowLimit
        self.highLimit = highLimit
        self.currSpeed = currSpeed
    
    ##Public Methods
    def setSpeed(newSpeed):
        #Set duty cycle at desired speed
        #Calculate calibrated new speed
        self.currSpeed = newSpeed
        
        return True
    
    def setLimits(newLowLimit, newHighLimit):
        
        self.lowLimit = newLowLimit
        self.highLimit = newHighLimit  
        
        return True
    
    def status():
        return True
    
    def turnOff():
        if (self.idle == False):
            return False        
        #Stop the motor to off

        self.idle = False
        return True

    
    def turnOn():
        if (self.idle == True) :
            return False        
        #Start the motor at lowest speed
        
        self.idle = True
        return True
    
    ##Private Methods
    def __initPWM():
        return True
    
    
    
    
