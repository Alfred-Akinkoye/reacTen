#Alfred Akinkoye
#PYTHON 3.0
##Game Logic
from CreateTables import *    #for database logic
from NavTable import *      #for reading and writing to table
from Read_Write_TS import *

#create db connection at start, to avoid repition in CreateTables
#dbconn = create_connection(r"C:\sqlite\db\pythonsqlite.db")
#create rows at start, to avoid repition in NavTable
#dbconn.row_factory = sqlite3.Row;
#creates any required Table
match_id = 0
#ThingSpeak Setup
#readShooterStatus()
#readBallForce()
writeStart_EndP2("startGame",2,3,4)
#finishGame
#shootBall
#readSimuStatus()
#readTargetInfo()
