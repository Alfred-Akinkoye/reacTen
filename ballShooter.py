"""Ball Shooter that controls the DC motor that shoots the ball"""


##PWM Modules
import RPi.GPIO as GPIO
from time import sleep
from numpy import interp

PWMPIN = 32
PWMPERIOD = 1000

#In % units
OFF = 0
LOWLIMIT = 0
HIGHLIMIT = 100
DEF_LOW = 10
DEF_HIGH = 80

#In duty cycle units
CALILOW = 70         
CALIHIGH = 100     


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
        
        actualOutput = interp(newSpeed, [self.lowLimit, self.highLimit],[CALILOW, CALIHIGH])
        
        #Set duty cycle at desired speed
        self.pwm.ChangeDutyCycle(newSpeed)
        self.currSpeed = newSpeed
        sleep(3)
        
        return True
    
    def setLimits(self, newLowLimit, newHighLimit):
        #Check that limits are within acceptable range
        if(newHighLimit > HIGHLIMIT):
            newHighLimit = HIGHLIMIT
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
        self.pwm.ChangeDutyCycle(OFF)
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
    

    
    
    
    
