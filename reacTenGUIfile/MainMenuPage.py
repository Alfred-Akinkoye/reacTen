from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sqlite3
from PIL import ImageTk, Image

HEIGHT = 500
WIDTH = 600
hasenteredtable = False
exit_yes = False
def ifexit():
    global exit_yes
    return exit_yes
def restart(root):
    ans = tkinter.messagebox.askyesno('Restarting New Game','Are you sure?')
    if ans:
        root.destroy()
        root = None
        from GameMode import GameMode
        GameMode()

def history():
    global hasenteredtable
    hasenteredtable = True
    hist = tkinter.messagebox.askyesno('View History','Are you sure you would like to view history?')
    if hist:
        from GameEngine import dbconn
        temp = tk.Toplevel()
        temp.title('HISTORY DATA')
        cursor = dbconn.cursor();
        text = "SELECT * FROM HISTORY"
        cursor.execute(text)
        myresult = cursor.fetchall()
        prequel = [("Username","GameNo","Result","GameMode","Score")]
        final = prequel+myresult
        myresult = final
        total_rows=len(myresult)
        total_columns = len(myresult[0])
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(temp, width=20,fg='blue',font=('Arial',16,'bold'))
                e.grid(row=i,column = j)
                e.insert(END,myresult[i][j])

def exiting(root):
    global exit_yes
    exit_yes = True
    exiting = tkinter.messagebox.askyesno('Exit','Are you sure you would like to exit?')
    if exiting:
        if hasenteredtable:
            root.destroy()
            root = None
        else:
            root.destroy()

def MainMenu():
  root = Tk()
  root.title("Main Menu Page GUI")
  canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH)
  canvas.pack()

  #displays the background image in the GUI
  background_image = ImageTk.PhotoImage(file =('image_thumb.jpg'))
  background_label = tk.Label(root, image= background_image)
  background_label.place( relwidth = 1, relheight = 1)

  #this label shows a header in the main menu
  headerLabel = tk.Label(root, text = "Choose any of the options below: ")
  headerLabel.place(relx = 0.1, rely =0.1, relwidth = 0.85, relheight = 0.1)

  #this frame is for the "StartNewGame" button
  restartframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  restartframe.place(relx = 0.5, rely = 0.25,relwidth = 0.3, relheight = 0.1,anchor = 'n')

  #this label is for the "StartNewGame" button
  restartlabel = tk.Label(restartframe)
  restartlabel.place(relx = 0.4, rely =0, relwidth = 0.5, relheight = 1)

  #this is the "StartnewGame" button
  restartbutton = tk.Button(restartframe,text = "Start New Game",font = 40,  fg =  'black', command = lambda: restart(root))
  restartbutton.place(relx = 0.5,rely = 0.5, relwidth = 0.9, relheight = 1, anchor = 'center')

  #this frame is for the "ViewHistory" button
  histframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  histframe.place(relx = 0.5, rely = 0.35,relwidth = 0.3, relheight = 0.1,anchor = 'n')

  #this label is for the "ViewHistory" button
  histlabel = tk.Label(histframe)
  histlabel.place(relx = 0.1, rely =0, relwidth = 0.8, relheight = 1)

  #this is the "ViewHistory" button
  histbutton = tk.Button(histframe,text = "View History",font = 40,  fg =  'black', command = lambda: history())
  histbutton.place(relx = 0.5,rely = 0.5, relwidth = 0.9, relheight = 1, anchor = 'center')

  #this frame is for the "ExitGame" button
  exitframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  exitframe.place(relx = 0.5, rely = 0.45,relwidth = 0.3, relheight = 0.1,anchor = 'n')

  #this label is for the "ExitGame" button
  exitlabel = tk.Label(exitframe)
  exitlabel.place(relx = 0.4, rely =0, relwidth = 0.5, relheight = 1)

  #this is the "ExitGame" button
  exitbutton = tk.Button(exitframe,text = "Exit Game",font = 40,  fg =  'black', command = lambda: exiting(root))
  exitbutton.place(relx = 0.5,rely = 0.5, relwidth = 0.9, relheight = 1, anchor = 'center')

  root.mainloop()
