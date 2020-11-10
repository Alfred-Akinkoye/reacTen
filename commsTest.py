import httplib
import urllib
import time

key = "KWCJB4XPZW92YT2R"  # Put your API Key here

def send_status():
    status = 'test'
    
    while True:
        params = urllib.urlencode({'field1': [status, 10],'field2': 10, 'key':key }) 
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


    
if __name__ == "__main__":
        
        try:
            frequency = 5  #Seconds
            while True:
                    send_status()        
                    time.sleep(frequency)
        except KeyboardInterrupt:
                print('Done')