"Sample simulation code"

import http.client
import urllib.parse
import urllib.request
import json
import simpy,random, statistics

#Status
RUNNING = 'running'
SHOOTER = 'ballShooter'
PROX = 'proximitySensor'
SERVO = 'servoMotor'

#Keys
TaiyeChannelC1w = "CHH1NY9GO2MMWEXM"
TaiyeChannelC1r = "KSW0O5SZVNZP6LC9"
TaiyeChannelC2w = "3I8BF8VYE42TX9KC"
TaiyeChannelC2r = "BBAQRG5FQB0VGJS5"

currentSpeed = random.randint(0,100)
lowLimit = random.randint(0,100)
highLimit = random.randint(0,100)
#STATUS
"Simulation class for ballShooter"
class Simulation(object):
    "Private Method"
    def init(self, ballsLeft = 5, status = "idle"):
        self.ballsLeft = ballsLeft
        self.status = status

"Public Methods"
def ballShooter():
    return True
    
def setSpeed():
    return currentSpeed
def setLimits(lowLimit,highLimit):
        try:
            if (highLimit > lowLimit):
                print(lowLimit)
                print(highLimit)
        except:
            if(highLimit < lowLimit):
                print("Comparison Exception")
def status():
    return ''
def turnOff():
    return ''
def turnOn():
    return ''

 ##Private  Methods
def __sendStatus():
    
    status = status()
    params = urllib.urlencode({'field1': status, 'field2': 10, 'field3': "shootBall",'key':TaiyeChannelC1w })
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
        #break

    def __readMessageShootBall():
        URL='https://api.thingspeak.com/channels/1160829/feeds.json?api_key='
        KEY= TaiyeChannelC1r
        HEADER='&results='
        NUMSIGNALS = '4'
        NEW_URL=URL+KEY+HEADER+NUMSIGNALS

        get_data=requests.get(NEW_URL).json()
        channel_id=get_data['channel']['id']

        field_1=get_data['feeds']


    def __readMessageGame():
        URL='https://api.thingspeak.com/channels/1160829/feeds.json?api_key='
        KEY= TaiyeChannelC1r
        HEADER='&results='
        NUMSIGNALS = '4'
        NEW_URL=URL+KEY+HEADER+NUMSIGNALS

        get_data=requests.get(NEW_URL).json()
        channel_id=get_data['channel']['id']

        field_1=get_data['feeds']
        

    
    