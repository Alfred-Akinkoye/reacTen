"""Ball Shooter object that controls all of the associated hardware devices"""

import httplib
import urllib
import time

import threading
import requests
import json

import ballShooter as bl
import servoMotor as servo

MAX_BALLS = 6
DEF_BALLS = 3
NOERROR = 0

PAUSE = 2    #Seconds


##Keys
#keyJulianB1r = "59EV92UFH25MFELC"            #MessageChannel
#keyJulianB1w = "KWCJB4XPZW92YT2R"  
#keyJulianB2r = "OGZPXUJ66L9TX6M7"
#keyJulianB2w = "U8Y5A1WG8Y5NL3WP"
#keyDelightD1w = "R9H809YX4MUSNPG1"        #Status Channel

messageChannel = "59EV92UFH25MFELC"
messageURL = "https://api.thingspeak.com/channels/1159985/feeds.json?api_key="
statusChannel = "R9H809YX4MUSNPG1"                

class ballShooterServer:
    
    """Constructor for the class"""
    def __init__(self, ballsLeft = DEF_BALLS, statusMessage = NOERROR):
        self.ballsLeft = ballsLeft
        self.statusMessage = statusMessage
        
        self.shooter = bl.ballShooter()
        #initialize Proximity Sensor
        self.servo = servo.servoMotor() 
        
        
    ##Public Methods
    def status(self):
        errorValue = NOERROR
        
        shooterStatus = self.shooter.status()
        if(not(shooterStatus)):
            errorValue += 100
            
        servoStatus = self.servo.status()
        if(not(servoStatus)):
            errorValue += 10       
            
        #Check Proximity Sensor status
        
        self.statusMessage += errorValue
        
        return self.statusMessage         #Assuming no errors
    
    def shootBall(self, newSpeed):
        if (self.ballsLeft == 0):
            return False
        
        #check proximity sensor if somebody, then change status and stop action
        self.shooter.setSpeed(newSpeed)
        self.servo.ejectBall()
        time.sleep(PAUSE)
        self.ballsLeft -= 1
        
        return True
    
    def startGame(self, lowLimit, highLimit, numBalls):
        
        if(numBalls < 0):
            return False
        
        if (numBalls >MAX_BALLS):
            numBalls = MAX_BALLS
        
        self.ballsLeft = numBalls
        
        #startGame for ballShooter
        self.shooter.setLimits(lowLimit, highLimit)
        self.shooter.turnOn()
        
        #startGame for Proximity Sensor
        return True
    
    def finishGame(self):
        
        self.shooter.turnOff()
        #finishGame for proximity sensor
        return True
    
      
        
    ##Private Methods
    def __getMessage(self):
        URL= messageURL
        KEY= messageChannel
        HEADER='&results='
        NUMSIGNALS = '1' 
        NEW_URL=URL+KEY+HEADER+NUMSIGNALS    
        
        get_data=requests.get(NEW_URL).json()
        #print('The type of the JSON data is; ', type(get_data))
        last_entry_id = get_data['channel']['last_entry_id']
        channel_id=get_data['channel']['id']
        
        field_1=get_data['feeds']
        
        t=[]
        for x in field_1:
            t.append(x['field1']) 
        
        return last_entry_id, get_data  
    
    def updateStatus(self,threadName, delay):
        try:
            while (1):
                self.sendStatus()
                time.sleep(delay)
        except KeyboardInterrupt:
            print("status updating ended")
    
    
    def decodeMessage(self,threadName, delay):
        curr_id , message =self.__getMessage()
        try:
            while True:
                mess_id, message =self.__getMessage()
                action = message['feeds']
                received = str(action[0]['field1'])
                if curr_id < mess_id:
                    curr_id = mess_id
                    print('New Message Received')
                    print('The message is: ' + received)
                    if received == 'shootBall':
                        currSpeed = int(action[0]['field2'])
                        if (self.shootBall(currSpeed)):
                            print('The ball is getting ready to be shot at: ', currSpeed, ' %')
                        else:
                            print('The shot failed')
                    if received == 'startGame':
                        lowLimit = int(action[0]['field2'])
                        highLimit = int(action[0]['field3'])
                        numBalls = int(action[0]['field4'])
                        if (self.startGame(lowLimit, highLimit, numBalls)):
                            print('The ballShooter is initializing...')   
                        else:
                            print("the inititialization failed")
                    if received == 'finishGame':
                        if (self.finishGame()):
                            print('The ballShooter is getting deactivated')  
                        else:
                            print('The deactivation of the ballShooter failed')
    
                time.sleep(delay)            
    
        except KeyboardInterrupt:
            print('Done status')        
      
if __name__ == "__main__":
        
        try:
            shooter = ballShooterServer()
            thread.start_new_thread(shooter.updateStatus, ("Thread-1", 12, ) )
            thread.start_new_thread(shooter.decodeMessage, ("Thread-2", 2, ) )
            
        except KeyboardInterrupt:
            print('Done')
            
        while 1:
            pass        
