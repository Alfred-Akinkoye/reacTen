import httplib
import urllib
#import urllib.request
import time

import threading
import requests
import json

#Keys
TaiyeChannelC1w = "CHH1NY9GO2MMWEXM"
TaiyeChannelC1r = "KSW0O5SZVNZP6LC9"
TaiyeChannelC2w = "3I8BF8VYE42TX9KC"
TaiyeChannelC2r = "BBAQRG5FQB0VGJS5"
keyDelightD1w = "R9H809YX4MUSNPG1"    #Status Channel
#Alfred
write_key = "FJX6WIJU2SA4BYJ0"

def send_status(error):

     while True:
        params = urllib.urlencode({'field1':error,'field2':0, 'key' :TaiyeChannelC2w})
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(response.status, response.reason)
            data = response.read()
            conn.close()
            print("Message sent")
        except:
            print ("connection failed")
        break

def get_message():

    URL='https://api.thingspeak.com/channels/1160829/feeds.json?api_key='
    KEY= TaiyeChannelC1r
    HEADER='&results='
    NUMSIGNALS = '4'
    NEW_URL=URL+KEY+HEADER+NUMSIGNALS
    #print (url)
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    print(current["field1"])

    get_data=requests.get(NEW_URL).json()
    #print('The type of the JSON data is; ', type(get_data))
    last_entry_id = get_data['channel']['last_entry_id']
    channel_id=get_data['channel']['id']

    field_1= get_data['feeds']


    t= []

    for x in field_1:
        t.append(x['field1'])
        print(field_1)
    for x in field_2:
        t.append(x['field2'])
        print(field_2)
    for x in field_3:
        t.append(x['field3'])

    for x in field_4:
        t.append(x['field4'])

    return  last_entry_id,get_data

def test_receive():
    url = 'https://api.thingspeak.com/channels/1160829/feeds.json?api_key=KSW0O5SZVNZP6LC9&results=1'
    get_data = requests.get(url).json()
    subject = get_data["feeds"]
    current = subject[0]
    print(current["field1"])
    print(current["field2"])
    print(current["field3"])
    print(current["field4"])

def send_message_sample(sample):
    RUNNING = 'running'
    SHOOTER = 'ballShooter'
    PROX = 'proximitySensor'
    SERVO = 'servoMotor'

    status = SHOOTER


    #Error Message from ballshooter
    #params = urllib.urlencode({'field1':status, 'key':TaiyeChannelC1w })
    #headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    #conn = httplib.HTTPConnection("api.thingspeak.com:80")
    #try:
        #conn.request("POST", "/update", params, headers)
        #response = conn.getresponse()
        #print(response.status, response.reason)
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
    #params = urllib.parse.urlencode({'field1': 'startGame','field2': '20','field3': '40','field4': '5', 'key':TaiyeChannelC2w })
    #headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    #conn = http.client.HTTPConnection("api.thingspeak.com:80")
    #try:
        #conn.request("POST", "/update", params, headers)
        #response = conn.getresponse()
        #print(response.status, response.reason)
        #data = response.read()
        #conn.close()
    #except:
        #print ("connection failed")


    #Message for finishGame
    params = urllib.urlencode({'field1': 'finishGame', 'key':TaiyeChannelC2w })
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
            mess_id, message =test_receive()
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

def demo_status_single(error):
    send_status(error)

def demo_status_sequence():
    try:
        while True:
            error = 100
            send_status(error)
            time.sleep(5)
            error = 010
            send_status(error)
            time.sleep(5)
            error = 001
            send_status(error)
            time.sleep(5)
            error = 002
            send_status(error)
            time.sleep(5)

    except KeyboardInterrupt:
            print('Done status')


if __name__ == "__main__":

        try:
            #demo_status_sequence()
            #demo_receive_message()
            #send_message_sample(12)
            #send_status(006)
            test_receive()

        except KeyboardInterrupt:
            print('Done')
