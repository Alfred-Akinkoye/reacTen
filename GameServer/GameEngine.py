#Alfred Akinkoye
#PYTHON 3.0
##Game Logic
import time
from CreateTables import *    #for database logic
from NavTable import *      #to navigate the table
from Read_Write_TS import *     #for reading and writing to table
from Login import *

#create db connection at start, to avoid repition in CreateTables
dbconn = create_connection(r"C:\sqlite\db\pythonsqlite.db")
match_id = 1
balls = 5
current_speed = 20
preset_speed = 0
max_speed = 100
min_speed = 0
shot_no = 1
users = ["temp","Simulation"]
turn = 0

def Test():
    Login()
    #username = "Alfred"
    users[0]=getusername()
    print(users)
    print(getusername())
    print(getpassword())
    #from MainMenuPage import MainMenu
    #MainMenu()
def ValidateLogin():
    userinfo = pullFromUser(dbconn)
    validate = False
    for x in userinfo:
        if x[0]==getusername() and x[1]==getpassword():
            validate = True;
            break
    return validate


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

    '''UI part'''
    Login()
    '''call the main menu page'''
    from MainMenuPage import MainMenu
    MainMenu()
    from GameMode import getMode
    '''For multiplayer'''
    if(1==getMode()):
        create_match_table(dbconn,match_id)
        writeStart_EndP1("startGame",min_speed,max_speed,balls)
        writeStart_EndP2("startGame",min_speed,max_speed,balls)
        time.sleep(1)
        while((int(readShooterStatus()) == 0) and (int(readTargetStatus()) == 0) and (balls>0) and (int(readSimuStatus())==0) and (int(readTargetInfoSim())==0)):
            #player 1's turn
            shootBall(current_speed)
            #delay      Gonna change to julians code here
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
        match_id += 1
    '''For single player'''
    if (0==getMode()) :
        create_match_table(dbconn,match_id)
        writeStart_EndP1("startGame",min_speed,max_speed,balls)
        writeStart_EndP2("startGame",min_speed,max_speed,balls)
        print("get's here")
        while((int(readShooterStatus()) == 0) and (int(readTargetStatus()) == 0) and (balls>0) and (int(readSimuStatus())==0) and (int(readTargetInfoSim())==0)):
            #player 1's turn
            shootBall(current_speed)
            #delay      Gonna change to julians code here
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
        match_id += 1

    '''Call closing page'''
    '''if statement for play again, look at stats, or main menu'''


if __name__ == "__main__":
    #Test()
    Game()
