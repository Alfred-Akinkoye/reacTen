import http.client
import urllib.parse
import urllib.request
import time

import threading
import requests
import json

#Keys
TaiyeChannelC1w = "CHH1NY9GO2MMWEXM"
TaiyeChannelC1r = "KSW0O5SZVNZP6LC9"
TaiyeChannelC2w = "3I8BF8VYE42TX9KC"
TaiyeChannelC2r = "BBAQRG5FQB0VGJS5"


def write_status():
    status = 'test'

    while True:
        params = urllib.parse.urlencode({'field1':[status,10] ,'field2': 10,'field3':"shootBall", 'key':TaiyeChannelC1w})
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
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

    URL='https://api.thingspeak.com/channels/1160829/fields/1.json?api_key='
    KEY= TaiyeChannelC1r
    HEADER='&results='
    NUMSIGNALS = '5'
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
    params = urllib.parse.urlencode({'field1': 'startGame','field2': '20','field3': '40','field4': '5', 'key':TaiyeChannelC1w })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        #print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")


    #Message for finishGame
    params = urllib.parse.urlencode({'field1': 'finishGame', 'key':TaiyeChannelC1w })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
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

            #send_message_sample()
            write_status()
            send_message_sample()
            get_message()

        except KeyboardInterrupt:
                print('Done')

