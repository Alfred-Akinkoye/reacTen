from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image

temp = Tk()
def table():
    from GameEngine import dbconn
    from GameEngine import match_id
    cursor = dbconn.cursor();
    temp.title('GAME DATA '+str(match_id))
    text = "SELECT * FROM Match_"+str(match_id)
    cursor.execute(text)
    myresult = cursor.fetchall()
    prequel = [("ShotNo","TargetForce", "ShooterSpeed", "Hit/Miss", "User")]
    final = prequel+myresult
    myresult = final
    total_rows=len(myresult)
    total_columns = len(myresult[0])
    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(temp, width=20,fg='blue',font=('Arial',16,'bold'))
            e.grid(row=i,column = j)
            e.insert(END,myresult[i][j])
    temp.mainloop()
