"""Calibration Script for BallShooter"""

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
DEF_LOW = 40
DEF_HIGH = 100

#In duty cycle units
CALILOW = 75         
CALIHIGH = 100     

class Calibration:
        
        def __init__(self):
                GPIO.setwarnings(False)         #disable warnings
                GPIO.setmode(GPIO.BOARD)        #set pin numbering system
                GPIO.setup(PWMPIN,GPIO.OUT)
                
                self.pwm = GPIO.PWM(PWMPIN,PWMPERIOD)
                pass

        def turnOn(self):
    
                #Start the motor at lowest speed
                self.pwm.start(OFF)
                return True
    
    
        def turnOff(self):
                #Stop the motor to off
                self.pwm.ChangeDutyCycle(OFF)
                sleep(2)
                self.pwm.stop()
                GPIO.cleanup()        
        
                return True
        
        def setSpeed(self, newSpeed):
                #print(type(newSpeed))
                #newSpeed = float(newSpeed)
                
                if(newSpeed > HIGHLIMIT):
                    newSpeed = HIGHLIMIT
                if(newSpeed < LOWLIMIT):
                    newSpeed = LOWLIMIT
                
                actualOutput = interp(newSpeed, [0, 100],[70, 100])
                    
                
                #Set duty cycle at desired speed
                #print(type(actualOutput))
                print("The actual output to motor is: " + str(actualOutput))
                self.pwm.ChangeDutyCycle(actualOutput)
                #Calculate calibrated new speed
                
                return True

if __name__ == "__main__":
        
        try:
                
                cali = Calibration()
                cali.turnOn()
                print('turned on')
                sleep(2)
                cali.setSpeed(3)
                while (1):
                        newSpeed = int(raw_input("Please enter a new speed (%): "))
                        cali.setSpeed(newSpeed)
                        #print(newSpeed)
                        sleep(4)
            
        except KeyboardInterrupt:
                cali.turnOff()
                print('Done')