from tkinter import *
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image
#import requests

HEIGHT = 500
WIDTH = 600
#root window of GUI

# Connect to SQLite database
dbconnect = sqlite3.connect("testdata.db" )
dbconnect.row_factory = sqlite3.Row;

# Create a cursor and initialize it
cursor = dbconnect.cursor();

# Create database
try:
    cursor.execute("CREATE TABLE testingdata (username TEXT, password TEXT)")
except Exception as E:
    print('Error: ', E)
else:
    print('table created')
    
def testLogin(entry1,entry2):
    if(entry1 and entry2):
        add_customer(entry1,entry2)
        print("0")
        #entry1.delete(0,END)
    else:
        print("invalid entry")

root = tk.Tk()

# Submit Customer To Database
def add_customer(entry1,entry2):
    sql_command = "INSERT INTO testingdata (username, password) VALUES (?, ?)"
    values = (entry1, entry2)
    cursor.execute(sql_command, values)

    # Commit the changes to the database
    dbconnect.commit()
    cursor.execute("SELECT * FROM testingdata")
    for row in cursor:
        print("Username: ",row['username'],"\nPassword: ",row['password'],"\n")
    dbconnect.close()
    
def Entry():
#makes a container that holds the button( used for initial screen size)

  root.title("Python GUI")
  canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH )
  canvas.pack()

  background_image = ImageTk.PhotoImage(file = ('image_thumb.jpg'))
  background_label = tk.Label(root, image= background_image)
  background_label.place( relwidth = 1, relheight = 1)


  welabel = tk.Label(root, text = "Welcome to REACTEN! Please fill the login details below: ")
  welabel.place(relx = 0.13, rely =0.1, relwidth = 0.75, relheight = 0.1)
#USERNAME FRAME
  userframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  userframe.place(relx = 0.5, rely = 0.25,relwidth = 0.75, relheight = 0.1,anchor = 'n')

#USERNAME ENTRY
  entry1 = tk.Entry(userframe,font = 40)
  entry1.place(relx = 0.35, rely = 0,relwidth = 0.65, relheight = 1)
  #entry.grid(row = 2, column = 2)

  label1 = tk.Label(userframe, text = "Username: ")
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


  label2 = tk.Label(passframe, text = "Password: ")
  label2.place(relx = 0, rely =0, relwidth = 0.3, relheight = 1)

  #creates a button
#PASSWORD BUTTON
  # button2 = tk.Button(passframe,text = " Enterpass",font = 40,  fg =  'black',command =lambda :testpass(entry2.get()))
  # button2.place(relx = 0.7,relwidth = 0.3, relheight = 1)

#MESSAGE FRAME
  messframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  messframe.place(relx = 0.5, rely = 0.5,relwidth = 0.15, relheight = 0.1,anchor = 'n')

#Login BUTTON
  button3 = tk.Button(messframe,text = " Login",font = 40,  fg =  'black',command = lambda: testLogin(entry1.get(),entry2.get()))
  button3.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')

  

#creates a label
#MESSAGE LABEL
  # label = tk.Label(messframe)
  # label.place(relwidth = 1, relheight = 1)
#label.grid(row = 1, column = 1)
#label.pack(side = 'right', fill = 'both')





#entry.pack(side = 'left', fill = 'both')
#to run the root application
  root.mainloop()


if __name__ == "__main__":
    Entry()
    



