import RPi.GPIO as GPIO
import time

def test_servo():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(32,GPIO.OUT)
    servo = GPIO.PWM(32,50)
    servo.start(0)
    time.sleep(2)
    duty = 2
    while duty<=12:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)
        time.sleep(0.5)
        duty = duty+6
        
    servo.stop(2)
    GPIO.cleanup()
    print("Goodbye")
        
if __name__ == '__main__':
    test_servo()
