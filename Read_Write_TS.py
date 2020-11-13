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
def writeStart_End(function,low_limit,high_limit,no_balls):
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
#Writing Shoot Ball
def shootBall(speed):
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C

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
#Read shooter status
def readShooterStatus():
    url = 'https://api.thingspeak.com/channels/1160941/feeds.json?api_key=OX910MD5LNMRZO17&results=1'
    #print (url)
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    print(current["field1"])
# Read Target Status
def readBallForce():
    url = 'https://api.thingspeak.com/channels/1226455/feeds.json?api_key=ZXWNO235JBIYOK0T&results=1'
    #print (url)
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    print(current["field1"])
