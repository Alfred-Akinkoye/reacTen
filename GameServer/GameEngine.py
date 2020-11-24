#Alfred Akinkoye
#PYTHON 3.0
##Game Logic
from CreateTables import *    #for database logic
from NavTable import *      #to navigate the table
from Read_Write_TS import *     #for reading and writing to table
from GUI import *       #GUI

#create db connection at start, to avoid repition in CreateTables
dbconn = create_connection(r"C:\sqlite\db\pythonsqlite.db")
match_id = 1
current_speed = 20
preset_speed = 0
max_speed = 100
min_speed = 0
shot_no = 1
users = ["temp","temp"]
turn = 0

#insertHistoryTable(dbconn, "username", 2, "Won", 0, 3)
#insertUserTable(dbconn,"Alfred","Test")
#insertMatchTable(dbconn, 2,20,50,0,"user",match_id)

#pullFromUser(dbconn)
#pullFromMatch(dbconn,match_id)
#pullFromHistory(dbconn)

#ThingSpeak Setup
#readShooterStatus()
#readBallForce()
#writeStart_EndP2("startGame",2,3,4)
#finishGame
#shootBall
#readSimuStatus()
#readTargetInfo()

def main():
    #The game starts by creating all the approraite tables, and checking pre existing ones
    create_history_table(dbconn)
    create_userdata_table(dbconn)

    #UI part

    create_match_table(dbconn,match_id)
    while(readShooterStatus() == readTargetStatus() == 1):
        shootBall(current_speed)
        feedback = readTargetInfo()
        insertMatchTable(dbconn,shot_no,feedback[0],current_speed,feedback[1],users[turn%2],match_id)


if __name__ == "__main__":
        main()
