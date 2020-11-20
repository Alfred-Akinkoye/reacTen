"""servo Motor"""

import RPi.GPIO as GPIO
import time

class servoMotor:
    
    def __init__(self):
        pass

    def ejectBall(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(32,GPIO.OUT)
        servo = GPIO.PWM(32,50)
        servo.start(0)
        time.sleep(1)
        duty = 2
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



            
