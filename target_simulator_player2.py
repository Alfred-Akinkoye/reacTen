import http.client
import urllib
import time
import requests
import _thread
import json

import random

#API keys
channelD1write = "R9H809YX4MUSNPG1"
channelD1read = "OX910MD5LNMRZO17"
channelD2write = "ZDILVXVB0LFJA9AK"
channelD2read = "ZXWNO235JBIYOK0T"
hitwrite ="U8Y5A1WG8Y5NL3WP"
statuswrite = "3I8BF8VYE42TX9KC"

def send_status():
    status = 0
    params = urllib.parse.urlencode({'field2': status, 'key':statuswrite })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print (status)
        print (response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")

def send_hit():
    hit = 1
    ballForce = random.randint(0,50)
    params = urllib.parse.urlencode({'field': ballForce, 'field2': hit, 'key':channelD2write })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print (hit)
        print(ballForce)
        print (response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")
        
def send_miss():
    hit = 0
    params = urllib.parse.urlencode({'field2': hit, 'key':channelD2write })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print (hit)
        print (response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")
        
    
def get_message():
    url = 'https://api.thingspeak.com/channels/1160829/feeds.json?api_key=KSW0O5SZVNZP6LC9&results=1'
    #print (url)
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    last_entry_id = get_data['channel']['last_entry_id']
    channel_id=get_data['channel']['id']
    current = subject[0]
    t=[]
    for x in subject:
        t.append(x['field1'])
    return last_entry_id, get_data
    
def hit_or_miss():
    
    if random.randint(0,1000) <= 250:
        send_miss()
        return False
    else:
        send_hit()
        #simulated_force()
        return True
def updateStatus(threadName,delay):
    try:
        while (1):
            send_status()
            time.sleep(delay)
    except KeyboardInterrupt:
        print("status updating ended")
        
def target_action(threadName,delay):
    curr_id , message =get_message()
    try:
        while True:
            mess_id, message =get_message()
            action = message['feeds']
            received = str(action[0]['field1'])
            if curr_id < mess_id:
                curr_id = mess_id
                print('New Message Received')
                print('The message is: ' + received)
                if received == 'shootBall':
                    hit_or_miss()
                if received == 'startGame':
                        print('The Target is initializing...')   
                if received == 'finishGame':
                        print('The Target is getting deactivated')    
                time.sleep(delay)            
    
    except KeyboardInterrupt:
            print('Done status')        
    
if __name__ == "__main__":
    #create 2 threads
    try:
        _thread.start_new_thread(updateStatus, ("Thread-1", 12, ) )
        _thread.start_new_thread(target_action, ("Thread-2", 4, ) )
    except KeyboardInterrupt:
        print('Done')
            
    while 1:
        pass        