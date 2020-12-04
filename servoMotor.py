"""servo Motor"""

import RPi.GPIO as GPIO
import time

PIN = 33   #GPIO 12 in Pi4

class servoMotor:
    
    def __init__(self):
        pass   
    
    def status(self):
        return True    
        
    def ejectBall(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PIN,GPIO.OUT)
        servo = GPIO.PWM(PIN,50)
        servo.start(0)
        time.sleep(0.5)
        duty = 3
        while duty<=12:
            servo.ChangeDutyCycle(duty)
            time.sleep(0.5)
            servo.ChangeDutyCycle(0)
            time.sleep(0.5)
            duty = duty+6     
        servo.stop(2)
        GPIO.cleanup()        
        
if __name__ == '__main__':
    servo = servoMotor()
    servo.ejectBall()