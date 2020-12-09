#Alfred Akinkoye
#PYTHON 3.0
##Game Logic
import time
from CreateTables import *    #for database logic
from NavTable import *      #to navigate the table
from Read_Write_TS import *     #for reading and writing to table
from Login import *
import random

#create db connection at start, to avoid repition in CreateTables
dbconn = create_connection(r"C:\sqlite\db\pythonsqlite.db")
match_id = 1
balls = 5
current_speed = 20
preset_speed = 0
speed = []
shot_no = 1
users = ["temp","Simulation"]
turn = 0


def ValidateLogin():
    userinfo = pullFromUser(dbconn)
    validate = False
    for x in userinfo:
        if x[0]==getusername() and x[1]==getpassword():
            validate = True;
            break
    return validate

def Game(temp):
    global match_id
    global loginno
    global balls
    global current_speed
    global preset_speed
    global speed
    global shot_no
    global users
    global turn
    #The game starts by creating all the approraite tables, and checking pre existing ones
    create_history_table(dbconn)
    create_userdata_table(dbconn)

    '''UI part'''
    if not temp:
        Login()
    else:
        pass
    users[0] = getusername()
    '''call the main menu page'''
    from MainMenuPage import MainMenu
    MainMenu()
    from MainMenuPage import ifexit
    if not ifexit:
        exit()
    else:
        pass
    from GameMode import getMode
    from BallShooterLimit import getLimit
    speed = getLimit()
    current_speed = random.randint(speed[0],speed[1])
    '''For multiplayer'''
    if(1==getMode()):
        create_match_table(dbconn,match_id)
        writeStart_EndP1("startGame",min_speed,max_speed,balls)
        writeStart_EndP2("startGame",min_speed,max_speed,balls)
        time.sleep(5)
        while((int(readShooterStatus()) == 0) and (int(readTargetStatus()) == 0) and (balls>0) and (int(readSimuStatus())==0) and (int(readTargetSimStatus())==0)):
            #player 1's turn
            shootBall(current_speed)
            #delay      Gonna change to julians code here
            time.sleep(5)
            feedback_p1 = readTargetInfo()
            insertMatchTable(dbconn,shot_no,int(feedback_p1[0]),current_speed,int(feedback_p1[1]),users[turn%2],match_id)
            current_speed = feedback_p1[0]
            time.sleep(2)
            #player 2's turn
            shootBallSim(current_speed)
            #delay
            time.sleep(5)
            feedback_p2 = readTargetInfoSim()
            insertMatchTable(dbconn,shot_no,int(feedback_p2[0]),current_speed,int(feedback_p2[1]),users[turn%2],match_id)
            current_speed = feedback_p2[0]
            time.sleep(2)
            balls-=1
            turn+=1
        match_id += 1
    '''For single player'''
    if (0==getMode()) :
        create_match_table(dbconn,match_id)
        writeStart_EndP1("startGame",speed[0],speed[1],balls)
        writeStart_EndP2("startGame",speed[0],speed[1],balls)
        time.sleep(5)
        while((int(readShooterStatus()) == 0) and (int(readTargetStatus()) == 0) and (balls>0) and (int(readSimuStatus())==0) and (int(readTargetSimStatus())==0)):
            #player 1's turn
            shootBall(current_speed)
            #delay      Gonna change to julians code here
            time.sleep(5)
            feedback_p1 = readTargetInfo()
            insertMatchTable(dbconn,shot_no,int(feedback_p1[0]),current_speed,int(feedback_p1[1]),users[turn],match_id)
            current_speed = feedback_p1[0]
            time.sleep(2)
            #player 2's turn
            shootBallSim(current_speed)
            turn+=1
            #delay
            time.sleep(5)
            feedback_p2 = readTargetInfoSim()
            insertMatchTable(dbconn,shot_no,int(feedback_p2[0]),current_speed,int(feedback_p2[1]),users[turn%2],match_id)
            current_speed = feedback_p2[0]
            time.sleep(2)
            print("Ball"+ str(balls) +"Done")
            balls-=1
            turn-=1
        writeStart_EndP1("finishGame",0,0,0)
        writeStart_EndP2("finishGame",0,0,0)

        temp = pullFromMatch(dbconn,match_id)
        temp2 = 0
        i = 0
        while i<(balls*2):
            if(temp[i][3]==1):
                temp2+=1
            i+=2
        i = 1
        temp3 = 0
        while i<(balls*2):
            if(temp[i][3]==1):
                temp3+=1
            i+=2
        margin = ""
        if(temp2>temp3):
            margin = "won"
        else:
            margin = "lost"
        insertHistoryTable(dbconn,users[0],match_id,margin,"Single Player",temp2)
        match_id += 1
        from gameOver import GameOver
        GameOver()
    '''Call closing page'''
    '''if statement for play again, look at stats, or main menu'''


if __name__ == "__main__":
    temp = False
    Game(temp)
