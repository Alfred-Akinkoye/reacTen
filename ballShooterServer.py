"""Ball Shooter object that controls all of the associated hardware devices"""

import httplib
import urllib
import time

import threading
import requests
import json

#Status
RUNNING = 'running'
SHOOTER = 'ballShooter'
PROX = 'proximitySensor'
SERVO = 'servoMotor'

#Keys
keyJulianB1r = "59EV92UFH25MFELC"
keyJulianB1w = "KWCJB4XPZW92YT2R"  
keyJulianB2r = "OGZPXUJ66L9TX6M7"
keyJulianB2w = "U8Y5A1WG8Y5NL3WP"


class ballShooterServer:
    
    """Constructor for the class"""
    def __init__(self, ballsLeft = None, status = None):
        self.ballsLeft = ballsLeft
        self.status = status
        
    ##Public Methods
    def status():
        return ''
    
    def shootBall():
        return False
    
    def startGame():
        return False
    
    def finishGame():
        return False
    
    ##Private Methods
    def __sendStatus():
        
        status = status()
        
        params = urllib.urlencode({'field1': status, 'key':keyJulianB1r }) 
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
        break
    
    def __getMessageShootBall():
        URL='https://api.thingspeak.com/channels/1159985/fields/1.json?api_key='
        KEY= keyJulianB1r
        HEADER='&results='
        NUMSIGNALS = '4' 
        NEW_URL=URL+KEY+HEADER+NUMSIGNALS    
        
        get_data=requests.get(NEW_URL).json()
        channel_id=get_data['channel']['id']
        
        field_1=get_data['feeds']
      
    
    def __getMessageGame():
        URL='https://api.thingspeak.com/channels/1159985/fields/1.json?api_key='
        KEY= keyJulianB1r
        HEADER='&results='
        NUMSIGNALS = '4' 
        NEW_URL=URL+KEY+HEADER+NUMSIGNALS    
        
        get_data=requests.get(NEW_URL).json()
        channel_id=get_data['channel']['id']
        
        field_1=get_data['feeds']