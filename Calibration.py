"""Calibration Script for BallShooter"""

##PWM Modules
import RPi.GPIO as GPIO
from time import sleep
from numpy import interp

PWMPIN = 12
PWMPERIOD = 1000

#In % units
OFF = 0
LOWLIMIT = 0
HIGHLIMIT = 100
DEF_LOW = 40
DEF_HIGH = 100

#In duty cycle units
CALILOW = 30         
CALIHIGH = 100     

class Calibration:
        
        def __init__(self):
                
                GPIO.setwarnings(False)			#disable warnings
                GPIO.setmode(GPIO.BOARD)		#set pin numbering system
                GPIO.setup(PWMPIN,GPIO.OUT)
                
                self.pwm = GPIO.PWM(PWMPIN,PWMPERIOD)
                pass

        def turnOn(self):
                #Start the motor at OFF speed
                self.pwm.start(OFF)
                return True
    
    
        def turnOff(self):
                #Stop the motor to off
                self.pwm.ChangeDutyCycle(OFF)
                self.pwm.stop()
                GPIO.cleanup()        
        
                return True
        
        def setSpeed(self, newSpeed):
                if(newSpeed > HIGHLIMIT):
                        newSpeed = HIGHLIMIT
                if(newSpeed < LOWLIMIT):
                        newSpeed = LOWLIMIT
                
                actualOutput = interp(newSpeed, [LOWLIMIT, HIGHLIMIT],[CALILOW, CALIHIGH])
                    
                
                #Set duty cycle at actualOutput
                self.pwm.ChangeDutyCycle(actualOutput)
                
                return True

if __name__ == "__main__":
        
        try:
                
                cali = Calibration()
                cali.turnOn()
                sleep(2)
                cali.setSpeed(30)
                while (1):
                        newSpeed = int(raw_input("Please enter a new speed: "))
                        cali.setSpeed(newSpeed)
                        sleep(4)
            
        except KeyboardInterrupt:
                cali.turnOff()
                print('Done')