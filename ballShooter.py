##PWM Modules
import RPi.GPIO as GPIO
from time import sleep


PWMPIN = 12
PWMPERIOD = 1000

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
        
        ledpin = PWMPIN				# PWM pin connected to LED
        GPIO.setwarnings(False)			#disable warnings
        GPIO.setmode(GPIO.BOARD)		#set pin numbering system
        GPIO.setup(ledpin,GPIO.OUT)
        
        self.pwm = GPIO.PWM(ledpin,PWMPERIOD)		#create PWM instance with frequency                
        

    
    ##Public Methods
    def setSpeed(self, newSpeed):
        #Set duty cycle at desired speed
        self.pwm.ChangeDutyCycle(newSpeed)
        #Calculate calibrated new speed
        self.currSpeed = newSpeed
        
        return True
    
    def setLimits(self, newLowLimit, newHighLimit):
        
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
        self.pwm.start(LOWLIMIT)
        
        self.idle = True
        return True
    

    
    
    
    
