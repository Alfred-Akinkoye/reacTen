##PWM Modules
import RPi.GPIO as GPIO
from time import sleep


PWMPIN = 12
PWMPERIOD = 1000

OFF = 0
LOWLIMIT = 0
HIGHLIMIT = 100
DEF_LOW = 40
DEF_HIGH = 100


class ballShooter:
    """Constructor for the class"""
    def __init__(self, idle = False, lowLimit = DEF_LOW, highLimit = DEF_HIGH, currSpeed = OFF):
        self.idle= idle
        self.lowLimit = lowLimit
        self.highLimit = highLimit
        self.currSpeed = currSpeed
        
        ledpin = PWMPIN				# PWM pin connected to LED
        GPIO.setwarnings(False)			#disable warnings
        GPIO.setmode(GPIO.BOARD)		#set pin numbering system
        GPIO.setup(ledpin,GPIO.OUT)
        
        self.pwm = GPIO.PWM(ledpin,PWMPERIOD)		#create PWM instance with frequency                
        

    
    ##Public Methods
    def setSpeed(self, newSpeed):
        if(newSpeed > HIGHLIMIT):
            newSpeed = HIGHLIMIT
        if(newSpeed < LOWLIMIT):
            newSpeed = LOWLIMIT
        
        #Set duty cycle at desired speed
        self.pwm.ChangeDutyCycle(newSpeed)
        #Calculate calibrated new speed
        self.currSpeed = newSpeed
        
        return True
    
    def setLimits(self, newLowLimit, newHighLimit):
        #Check that limits are within acceptable range
        if(newHighLimit > HIGHLIMIT):
            newHIghLimit = HIGHLIMIT
        if(newLowLimit < LOWLIMIT):
            newLowLimit = LOWLIMIT
        
        #Check that limits are compatible
        if newLowLimit >newHighLimit:
            return False         #The limits remain unchanged
        
        self.lowLimit = newLowLimit
        self.highLimit = newHighLimit  
        
        return True
    
    def status(self):
        return True
    
    def turnOff(self):
        if (self.idle == False):
            return False        
        #Stop the motor to off
        self.pwm.stop()
        GPIO.cleanup()        

        self.idle = False
        return True

    
    def turnOn(self):
        if (self.idle == True) :
            return False        
        #Start the motor at lowest speed
        self.pwm.start(DEF_LOW)
        
        self.idle = True
        return True
    

    
    
    
    
