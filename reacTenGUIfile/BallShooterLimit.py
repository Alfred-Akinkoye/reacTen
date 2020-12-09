from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
#import requests

HEIGHT = 500
WIDTH = 600

low=0
high = 0
def testLimit(root,entry1,entry2):
    global low
    global high
    try:
        if(int(entry1)< 101 and int(entry1)> 0 and entry1.isdigit() and int(entry2)> 0 and int(entry2)< 101 and entry2.isdigit()):
            print("0")
            #entry1.delete(0,END)
            print("LowLimit: ",int(entry1))
            print("HighLimit: ",int(entry2))
            low = int(entry1)
            high = int(entry2)
            root.destroy()
            root = None
        else:
            print("invalid entry")
    except:
        print("Invalid input")



def getLimit():
    temp = [low,high]
    return temp


def Limit():
#makes a container that holds the button( used for initial screen size)
  root = tk.Tk()
  root.title("BallLimit GUI")
  canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH )
  canvas.pack()

  background_image = ImageTk.PhotoImage(file = ('image_thumb.jpg'))
  background_label = tk.Label(root, image= background_image)
  background_label.place( relwidth = 1, relheight = 1)


  welabel = tk.Label(root, text = "Welcome to REACTEN! Please fill the following details below: ")
  welabel.place(relx = 0.13, rely =0.1, relwidth = 0.75, relheight = 0.1)
#USERNAME FRAME
  userframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  userframe.place(relx = 0.5, rely = 0.25,relwidth = 0.75, relheight = 0.1,anchor = 'n')

#USERNAME ENTRY
  entry1 = tk.Entry(userframe,font = 40)
  entry1.place(relx = 0.35, rely = 0,relwidth = 0.65, relheight = 1)
  #entry.grid(row = 2, column = 2)

  label1 = tk.Label(userframe, text = "LowLimit: ")
  label1.place(relx = 0, rely =0, relwidth = 0.3, relheight = 1)

  #creates a button
#USERNAME BUTTON
  # button1 = tk.Button(userframe,text = "",font = 40, command =lambda :testuser(entry1.get()))
  # button1.place(relx = 0.7, rely = 0,relwidth = 0.3, relheight = 1)
#button.grid(row = 0, column = 0)
#button.pack(side = 'left', fill = 'x', expand = True)

#PASSWORD FRAME
  passframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  passframe.place(relx = 0.5, rely = 0.35,relwidth = 0.75, relheight = 0.1,anchor = 'n')

#PASSWORD ENTRY
  entry2 = tk.Entry(passframe,font = 40)
  entry2.place(relx = 0.35, rely = 0,relwidth = 0.65, relheight = 1)


  label2 = tk.Label(passframe, text = "HighLimit: ")
  label2.place(relx = 0, rely =0, relwidth = 0.3, relheight = 1)

  #creates a button
#PASSWORD BUTTON
  # button2 = tk.Button(passframe,text = " Enterpass",font = 40,  fg =  'black',command =lambda :testpass(entry2.get()))
  # button2.place(relx = 0.7,relwidth = 0.3, relheight = 1)

#MESSAGE FRAME
  messframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  messframe.place(relx = 0.5, rely = 0.5,relwidth = 0.15, relheight = 0.1,anchor = 'n')

#done BUTTON
  button3 = tk.Button(messframe,text = " Continue",font = 40,  fg =  'black',command = lambda: testLimit(root,entry1.get(),entry2.get()))
  button3.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')

  root.mainloop()
