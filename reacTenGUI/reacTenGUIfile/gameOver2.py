
#https://github.com/Alfred-Akinkoye/reacTen.git

from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
import sqlite3
#from GameMode import GameMode

HEIGHT = 500
WIDTH = 600

global root
root = tk.Tk()

hasenteredtable = False

def main():
    root.destroy()
    if hasenteredtable:
        from MainMenuPage import MainMenu
        MainMenu()
    else:
        from MainMenuPage import MainMenu
        MainMenu()

def table():
    global hasenteredtable
    hasenteredtable = True
    
    data = tkinter.messagebox.askyesno('Game Data','Are you sure you would like to view game data?')
    if data:
        
        from gameengine import dbconn
        from gameengine import match_id

        temp = tk.Tk()
        temp.title('GAME DATA')
        cursor = dbconn.cursor();
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

#     return
def GameOver():
    
  root.title("GameOver GUI")
  canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH)
  canvas.pack()

  background_image = ImageTk.PhotoImage(file =('image_400.jpg'))
  background_label = tk.Label(root, image= background_image)
  background_label.place( relwidth = 1, relheight = 1)
  # new_image = background_image.resize(HEIGHT,WIDTH)
  # new_image.save('image_new.jpg')

  #print(new_image.size)
  global button2
  welabel = tk.Label(root, text = "Game is over!")
  welabel.place(relx = 0.1, rely =0.1, relwidth = 0.85, relheight = 0.1)

  dataframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  dataframe.place(relx = 0.5, rely = 0.3,relwidth = 0.4, relheight = 0.1,anchor = 'n')
  button2 = tk.Button(dataframe,text = "GameData",font = 40,  fg =  'black',command = lambda: table())
  button2.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')


  messframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  messframe.place(relx = 0.5, rely = 0.5,relwidth = 0.4, relheight = 0.1,anchor = 'n')
  button3 = tk.Button(messframe,text = "Proceed to Main Menu",font = 40,  fg =  'black',command = lambda: main())
  button3.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')

  root.mainloop()

if __name__ == "__main__":
    GameOver()
