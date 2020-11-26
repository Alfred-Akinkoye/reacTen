#Alfred Akinkoye
#PYTHON 3.0
##Game Logic
import time
from CreateTables import *    #for database logic
from NavTable import *      #to navigate the table
from Read_Write_TS import *     #for reading and writing to table
from GUI import *       #GUI

#create db connection at start, to avoid repition in CreateTables
dbconn = create_connection(r"C:\sqlite\db\pythonsqlite.db")
global match_id
match_id = 1
global balls
balls = 5
global current_speed
current_speed = 20
global preset_speed
preset_speed = 0
global max_speed
max_speed = 100
global min_speed
min_speed = 0
global shot_no
shot_no = 1
global users
users = ["temp","temp"]
global turn
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

def Test():
    temp = pullFromUser(dbconn)
    for x in temp:
        if x[0]=="Alfred" and x[1]=="Test":
            print("works")
            break
    print (temp[0][0]+" "+temp[0][1])

def Game():
    global match_id
    global balls
    global current_speed
    global preset_speed
    global max_speed
    global min_speed
    global shot_no
    global users
    global turn
    #The game starts by creating all the approraite tables, and checking pre existing ones
    create_history_table(dbconn)
    create_userdata_table(dbconn)

    #UI part
    #Login()
    global user_name
    user_name = "Alfred"
    global pass_word
    pass_word = "Test"
    input = pullFromUser(dbconn)
    for x in input:
        if x[0]==user_name and x[1]==pass_word:
            print("works")
            break

    create_match_table(dbconn,match_id)
    writeStart_EndP1("startGame",min_speed,max_speed,balls)
    writeStart_EndP2("startGame",min_speed,max_speed,balls)
    while((int(readShooterStatus()) == 0) and (int(readTargetStatus()) == 0) and balls>0):
        #player 1's turn
        shootBall(current_speed)
        #delay
        time.sleep(3)
        feedback_p1 = readTargetInfo()
        insertMatchTable(dbconn,shot_no,int(feedback_p1[0]),current_speed,int(feedback_p1[1]),users[turn%2],match_id)
        current_speed = feedback_p1[0]
        #player 2's turn
        shootBallSim(current_speed)
        #delay
        time.sleep(3)
        feedback_p2 = readTargetInfoSim()
        insertMatchTable(dbconn,shot_no,int(feedback_p2[0]),current_speed,int(feedback_p2[1]),users[turn%2],match_id)
        current_speed = feedback_p2[0]
        balls-=1


if __name__ == "__main__":
    #Test()
    Game()
