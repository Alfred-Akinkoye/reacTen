import httplib
import urllib
import time

import threading
import requests
import json

keyJulianB1r = "59EV92UFH25MFELC"
keyJulianB1w = "KWCJB4XPZW92YT2R"  
keyJulianB2r = "OGZPXUJ66L9TX6M7"
keyJulianB2w = "U8Y5A1WG8Y5NL3WP"



def send_status():
    status = 'test'
    
    while True:
        params = urllib.urlencode({'field1': [status, 10],'field2': 10, 'key':keyJulianB1r }) 
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

def get_message():
    
    URL='https://api.thingspeak.com/channels/1159985/fields/1.json?api_key='
    KEY= keyJulianB1r
    HEADER='&results='
    NUMSIGNALS = '4' 
    NEW_URL=URL+KEY+HEADER+NUMSIGNALS    
    
    get_data=requests.get(NEW_URL).json()
    print('The type of the JSON data is; ', type(get_data))
    channel_id=get_data['channel']['id']
    
    field_1=get_data['feeds']
    
    t=[]
    for x in field_1:
        #print(x['field1'])
        #print(x['field1'][0])
        #print(type(x['field1']))
        #print(type(str(x['field1'])))
        #print(str(x['field1']))
        t.append(x['field1'])    
        #print(int('10'))
        #print(type(int('10')))
        #print(bool("True"))
        #if bool('True'):
            #print("Success")

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
        
        
        
        
    



    
    
if __name__ == "__main__":
        
        try:
            #frequency = 5  #Seconds
            #while True:
                    #send_status()        
                    #time.sleep(frequency)
            
            #get_message()
            
            send_message_sample()
            send_message_sample()
            send_message_sample()
     
        except KeyboardInterrupt:
                print('Done')