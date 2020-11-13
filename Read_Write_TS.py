#Alfred Akinkoye
#PYTHON 3.0
#import and export to and from TS
import http.client
import urllib
from urllib.request import *
import json
import requests
#import urllib2

write_key = "FJX6WIJU2SA4BYJ0"
B1 = 'KWCJB4XPZW92YT2R'
D1 = '0RIUH454O61S1D7F'
C1 = 'CHH1NY9GO2MMWEXM'
channelID = "1155258"

#Writing start game to TS
def writeStart_EndP1(function,low_limit,high_limit,no_balls):
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C

        params = urllib.parse.urlencode({'field1': function, 'field2': low_limit,'field3': high_limit,'field4': no_balls, 'key':B1 })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection('api.thingspeak.com:80')
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

def writeStart_EndP2(function,low_limit,high_limit,no_balls):
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C

        params = urllib.parse.urlencode({'field1': function, 'field2': low_limit,'field3': high_limit,'field4': no_balls, 'key':C1 })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection('api.thingspeak.com:80')
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break


#Writing Shoot Ball to Ball shooter
def shootBall(speed):
    while True:
        params = urllib.parse.urlencode({'field1': "shootBall", 'field2': speed, 'key':B1 })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection('api.thingspeak.com:80')
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

#Writing shootball to simulator
def shootBall(speed):
    while True:
        params = urllib.parse.urlencode({'field1': "shootBall", 'field2': speed, 'key':C1 })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection('api.thingspeak.com:80')
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

#Read shooter status
def readShooterStatus():
    url = 'https://api.thingspeak.com/channels/1160941/feeds.json?api_key=OX910MD5LNMRZO17&results=1'
    #print (url)
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    print(current["field1"])

#read Target Status
def readTargetStatus():
    url = 'https://api.thingspeak.com/channels/1160941/feeds.json?api_key=OX910MD5LNMRZO17&results=1'
    #print (url)
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    print(current["field1"])

# Read Target Status
def readTargetInfo():
    url = 'https://api.thingspeak.com/channels/1180930/feeds.json?api_key=OGZPXUJ66L9TX6M7&results=1'
    #print (url)
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    print(current["field1"])
    print(current["field2"])

#Staus Simulation
def readSimuStatus():
    url = 'https://api.thingspeak.com/channels/1181306/feeds.json?api_key=BBAQRG5FQB0VGJS5&results=1'
    #print (url)
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    print(current["field1"])
