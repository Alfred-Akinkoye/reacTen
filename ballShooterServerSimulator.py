"""Ball Shooter Simulator object that controls all of the associated hardware devices"""

import httplib
import urllib
import time

import threading
import requests
import json

import numpy.random as rn

MAX_BALLS = 6
DEF_BALLS = 3
NOERROR = 0

PAUSE = 2    #Seconds


##Keys
#keyC1r = "KSW0O5SZVNZP6LC9"            #MessageChannel
#keyC2w = "R9H809YX4MUSNPG1"        #Status Channel

messageChannel = "KSW0O5SZVNZP6LC9"
statusChannel = "R9H809YX4MUSNPG1"                

class ballShooterServer:
    
    """Constructor for the class"""
    def __init__(self, ballsLeft = DEF_BALLS, statusMessage = NOERROR):
        self.ballsLeft = ballsLeft
        self.statusMessage = statusMessage
        
        
    ##Public Methods
    def status(self):
        self.statusMessage =  __statusSimulation()
        
        return self.statusMessage         #Assuming no errors
    
    def shootBall(self, newSpeed):
        if (self.ballsLeft == 0):
            return False
        
        #check proximity sensor if somebody, then change status and stop action
        time.sleep(PAUSE)
        self.ballsLeft -= 1
        
        return True
    
    def startGame(self, lowLimit, highLimit, numBalls):
        
        if(numBalls < 0):
            return False
        
        if (numBalls >MAX_BALLS):
            numBalls = MAX_BALLS
        
        self.ballsLeft = numBalls
        return True
    
    def finishGame(self):
        return True
    
    
    def sendStatus(self):
        
        statusMessage = self.status()
        
        params = urllib.urlencode({'field1': statusMessage, 'key':statusChannel}) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
    
    def decodeMessage(self):
        curr_id = -1
        try:
            while True:
                mess_id, message =self.__getMessage()
                action = message['feeds']
                received = str(action[0]['field1'])
                if curr_id < mess_id:
                    curr_id = mess_id
                    print('New Message Received')
                    print('The message is: ' + received)
                    print('field2 = ' +str(action[0]['field2']))
                    print('field3 = ' +str(action[0]['field3']))
                    print('field4 = ' +str(action[0]['field4']))
                    #if message == 'shootBall':
                        #currSpeed = action[0]['field2']
                        #print('The ball is getting ready to be shot at: ', currSpeed, ' %')
                    #if message == 'startGame':
                        #print('The ballShooter is initializing...')        
                    #if message == 'finishGame':
                        #print('The ballShooter is getting deactivated')                    
    
                time.sleep(5)            
    
        except KeyboardInterrupt:
                print('Done status')        
        
    ##Private Methods
    def __getMessage(self):
        URL='https://api.thingspeak.com/channels/1159985/feeds.json?api_key='
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
    
    def __statusSimulation():
        errorMessa = 0
        
        shooter = [0, 100]
        prob = [0.98, 0.02]    
        errorMessa += int(rn.choice(shooter, 1, p = prob))
        
        servo = [0, 10]
        prob = [0.98, 0.02]    
        errorMessa += int(rn.choice(servo, 1, p = prob))      
        
        proxsensor = [0, 1, 2]
        prob = [0.93, 0.02, 0.05]    
        errorMessa += int(rn.choice(servo, 1, p = prob))              
        
        return errorMessa
    

      
#if __name__ == "__main__":
        
        #try:
            #shooterServer = ballShooterServer()
            #shooterServer.decodeMessage()
            #shooterServer.sendStatus()
            
        #except KeyboardInterrupt:
            #print('Done')
