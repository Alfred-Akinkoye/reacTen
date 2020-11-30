from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
#from GameEngine import *

#dbconn = create_connection(r"C:\sqlite\db\pythonsqlite.db")
HEIGHT = 500
WIDTH = 600
#history = pullFromHistory(dbconn)
root = tk.Tk()

def showHistory(self,root):
    for i in range(len(history)):
        for j in range(len(history[0])):
            self.e = Entry(root, width=20, fg='blue',
                           font=('Arial',16,'bold'))
            self.e.grid(row=i, column=j)
            self.e.insert(END, lst[i][j])


def restart():
    ans = tkinter.messagebox.askyesno('Starting New Game','Are you sure?')
    if ans:
        root.destroy()
        from GameMode import GameMode
        GameMode()
def history():
    hist = tkinter.messagebox.askyesno('View History','Are you sure you would like to view history?')
    if hist:
        root.destroy()

def exiting():
    exiting = tkinter.messagebox.askyesno('Exit','Are you sure you would like to exit?')
    if exiting:
        root.destroy()

def MainMenu():
  root.title("Main Menu Page GUI")
  canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH)
  canvas.pack()

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
  restartbutton = tk.Button(restartframe,text = "Start New Game",font = 40,  fg =  'black', command = lambda: restart())
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

  #this label is for the "StartNewGame" button
  exitlabel = tk.Label(exitframe)
  exitlabel.place(relx = 0.4, rely =0, relwidth = 0.5, relheight = 1)

  #this is the "StartnewGame" button
  exitbutton = tk.Button(exitframe,text = "Exit Game",font = 40,  fg =  'black', command = lambda: exiting())
  exitbutton.place(relx = 0.5,rely = 0.5, relwidth = 0.9, relheight = 1, anchor = 'center')
  root.mainloop()
