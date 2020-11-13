import httplib
import urllib
import time

import threading
import requests
import json

keyJulianB1r = "59EV92UFH25MFELC"      #MessageChannel
keyJulianB1w = "KWCJB4XPZW92YT2R"  
keyJulianB2r = "OGZPXUJ66L9TX6M7"
keyJulianB2w = "U8Y5A1WG8Y5NL3WP"

keyDelightD1w = "R9H809YX4MUSNPG1"    #Status Channel


def send_status(error):
    
    while True:
        params = urllib.urlencode({'field1': error, 'key':keyDelightD1w}) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(response.status, response.reason)
            print('The error message sent was: ', error)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

def get_message():
    
    URL='https://api.thingspeak.com/channels/1159985/fields/1.json?api_key='
    KEY= keyJulianB1r
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


def send_message_sample():
    RUNNING = 'running'
    SHOOTER = 'ballShooter'
    PROX = 'proximitySensor'
    SERVO = 'servoMotor'
    
    status = SHOOTER
    
    
    ##Error Message from ballshooter
    #params = urllib.urlencode({'field1':status, 'key':keyJulianB2w }) 
    #headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    #conn = httplib.HTTPConnection("api.thingspeak.com:80")
    #try:
        #conn.request("POST", "/update", params, headers)
        #response = conn.getresponse()
        ##print(response.status, response.reason)
        #data = response.read()
        #conn.close()
    #except:
        #print ("connection failed")
  


    ##Message for shootBall at 50%
    #params = urllib.urlencode({'field3': 'shootBall','field4': '50', 'key':keyJulianB2w }) 
    #headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    #conn = httplib.HTTPConnection("api.thingspeak.com:80")    
    #try:
        #conn.request("POST", "/update", params, headers)
        #response = conn.getresponse()
        ##print(response.status, response.reason)
        #data = response.read()
        #conn.close()
    #except:
        #print ("connection failed")
        
        
    #Message for startGame
    params = urllib.urlencode({'field1': 'startGame','field2': '20','field3': '40','field4': '5', 'key':keyJulianB1w }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")    
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        #print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")      
        
    
    #Message for finishGame
    params = urllib.urlencode({'field1': 'finishGame', 'key':keyJulianB1w }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")    
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        #print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")          
  

def demo_receive_message():
    curr_id = -1
    try:
        while True:
            mess_id, message =get_message()
            action = message['feeds']
            for data in action:
                if curr_id < mess_id:
                    curr_id = mess_id
                    print('New Message Received')
                    print('The message is; ', str(data))
                    if message == 'shootBall':
                        print('The ball is getting ready to be shot...')
            
            time.sleep(5)            

    except KeyboardInterrupt:
            print('Done status')
            
def demo_status():
    try:
        while True:
            error = 110
            send_status(error)   
            time.sleep(5)
            error = 0
            send_status(error)
            time.sleep(5)
            error = 12
            send_status(error)
            time.sleep(5)            

    except KeyboardInterrupt:
            print('Done status')    

    
if __name__ == "__main__":
        
        try:
            #demo_status()
            demo_receive_message()
        except KeyboardInterrupt:
            print('Done')