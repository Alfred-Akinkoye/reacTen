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

def send_status():
    status = "online"
    params = urllib.parse.urlencode({'field1': status, 'key':channelD1write })
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

send_status()
def send_hit():
    hit = True
    params = urllib.urlencode({'field2': hit, 'key':channelD1write })
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
    params = urllib.urlencode({'field2': hit, 'key':channelD1write })
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
        
def get_start():
    URl='https://api.thingspeak.com/channels/1160941/fields/1.json?api_key='
    KEY=channelD1read
    HEADER='&results=2'
    NEW_URL=URl+KEY+HEADER
    
    get_data = requests.get(NEW_URL,)
    response_data = get_data.json()
    channel_id=get_data['channel']['id']
    
    field_1=get_data['field1']
    print(field_1)
    
def get_end():
    URl='https://api.thingspeak.com/channels/1160941/fields/1.json?api_key='
    KEY=channelD1read
    HEADER='&results=2'
    NEW_URL=URl+KEY+HEADER
    
    get_data = requests.get(NEW_URL,)
    response_data = get_data.json()
    channel_id=get_data['channel']['id']
    
    field_1=get_data['field1']
    print(field_1)
        
def get_shootball():
    URl='https://api.thingspeak.com/channels/1160941/fields/1.json?api_key='
    KEY=channelD1read
    HEADER='&results=2'
    NEW_URL=URl+KEY+HEADER
    
    get_data = requests.get(NEW_URL,)
    response_data = get_data.json()
    channel_id=get_data['channel']['id']
    
    field_1=get_data['field1']
    print(field_1)

def simulated_force():
    ballForce = random.randint(0,50)
    
def hit_or_miss():
    if random.randint(0,1000) <= 250:
        send_miss()
        return False
    else:
        noOfHits += 1
        send_hit()
        simulated_force()
        return True

