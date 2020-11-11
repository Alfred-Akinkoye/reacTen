##Game Logic
from time import sleep
import urllib2
from CreateTables import *    #for database logic
from NavTable import *      #for reading and writing to table

#create db connection at start, to avoid repition in CreateTables
dbconn = create_connection(r"C:\sqlite\db\pythonsqlite.db")
#create rows at start, to avoid repition in NavTable
dbconn.row_factory = sqlite3.Row;
#creates any required Table
match_id = 0
#ThingSpeak Setup
write_key = "FJX6WIJU2SA4BYJ0"
channelID = "1155258"

#For status
temp = "start"
baseURL = 'http://api.thingspeak.com/update?api_key=FJX6WIJU2SA4BYJ0&field1='
print (temp)
f = urllib2.urlopen(baseURL + temp)
f.read()
f.close()
sleep(2)
print "Program has ended"
