from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
import sqlite3
#from GameMode import GameMode

HEIGHT = 500
WIDTH = 600
#global root
def main(root):
    root.destroy()
    root = None
    from GameEngine import Game
    temp = True
    Game(temp)

def callTable():
    data = tkinter.messagebox.askyesno('Game Data','Are you sure you would like to view game data?')
    if data:
        from GameTable import table
        table()


#     return
def GameOver():
  root = Tk()
  root.title("GameOver GUI")
  canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH)
  canvas.pack()

  background_image = ImageTk.PhotoImage(file = ('image_400.jpg'))
  background_label = tk.Label(root, image= background_image)
  background_label.place( relwidth = 1, relheight = 1)

  #print(new_image.size)
  welabel = tk.Label(root, text = "Game is over!")
  welabel.place(relx = 0.1, rely =0.1, relwidth = 0.85, relheight = 0.1)

  dataframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  dataframe.place(relx = 0.5, rely = 0.3,relwidth = 0.4, relheight = 0.1,anchor = 'n')
  button2 = tk.Button(dataframe,text = "GameData",font = 40,  fg =  'black',command = lambda: callTable())
  button2.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')


  messframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  messframe.place(relx = 0.5, rely = 0.5,relwidth = 0.4, relheight = 0.1,anchor = 'n')
  button3 = tk.Button(messframe,text = "Proceed to Main Menu",font = 40,  fg =  'black',command = lambda: main(root))
  button3.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')

  root.mainloop()
