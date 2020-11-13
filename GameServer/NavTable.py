import sqlite3
from sqlite3 import Error

###Append to each table###
def insertUserTable(conn, username, password):
    cursor = conn.cursor();
    cursor.execute('''insert into USERS values (?, ?)''',(username,password));
    conn.commit();

def insertHistoryTable(conn, username, gameno, result, gamemode, score):
    cursor = conn.cursor();
    cursor.execute('''insert into HISTORY values (?, ?, ?, ?, ?)''',(username,gameno,result,gamemode,score));
    conn.commit();

def insertMatchTable(conn, shotno,targetForce,shooterspeed,hitormiss,user,id):
    temp = '''insert into Match_''' + str(id) + ''' values (?, ?, ?, ?, ?)'''
    cursor = conn.cursor();
    cursor.execute(temp,(shotno,targetForce,shooterspeed,hitormiss,user));
    conn.commit();
