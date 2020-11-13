import http.client
import urllib
import time
import requests
import threading
import json

import random

#API keys
channelD1write = "R9H809YX4MUSNPG1"
channelD1read = "OX910MD5LNMRZO17"
channelD2write = "ZDILVXVB0LFJA9AK"
channelD2read = "ZXWNO235JBIYOK0T"
hitwrite ="U8Y5A1WG8Y5NL3WP"

def send_status():
    status = 0
    params = urllib.parse.urlencode({'field2': status, 'key':channelD1write })
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
    hit = True
    params = urllib.parse.urlencode({'field2': hit, 'key':hitwrite })
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
        
def send_miss():
    hit = False
    params = urllib.parse.urlencode({'field2': hit, 'key':hitwrite })
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
        
def get_start_and_end():
     url = 'https://api.thingspeak.com/channels/1159985/feeds.json?api_key=59EV92UFH25MFELC&results=2'
    #print (url)
     get_data = requests.get(url).json()
     subject = get_data["feeds"]
     current = subject[0]
     print(current["field1"])
    
def get_shootball():
    URl='https://api.thingspeak.com/channels/1160941/fields/1.json?api_key='

    
    get_data = requests.get(NEW_URL)
    response_data = get_data.json()
    channel_id=get_data['channel']['id']
    
    field_1=get_data['field1']
    print(field_1)

def simulated_force():
    ballForce = random.randint(0,50)
    print(ballForce)
    
def hit_or_miss():
    
    if random.randint(0,1000) <= 250:
        send_miss()
        return False
    else:
        send_hit()
        simulated_force()
        return True
def main(): 
    get_start_and_end()
    send_status()
    hit_or_miss()

if __name__ == "__main__":
    main()
    
    
    ##59EV92UFH25MFELC
##https://api.thingspeak.com/channels/1180930/fields/1.json?api_key=OGZPXUJ66L9TX6M7&results=2
 #url = 'https://api.thingspeak.com/channels/1159985/feeds.json?api_key=59EV92UFH25MFELC&results=2'
    #print (url)
    #get_data = requests.get(url).json()
    #subject = get_data["feeds"]
    #current = subject[0]
    #print(current["field1"])
    #U8Y5A1WG8Y5NL3WP
