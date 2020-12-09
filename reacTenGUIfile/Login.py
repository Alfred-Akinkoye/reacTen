from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
#import requests

HEIGHT = 500
WIDTH = 600


# def clear():
#   global username
#   global password
#   username = StringVar()
#   password = StringVar()

#   username_info = username.get()
#   password_info = password.get()

#   file = open(username_info+ ".txt", "w")
#   file.write(username_info)
#   file.write(password_info)
#   file.close()

#   entry1.delete(0,END)
#   entry2.delete(0,END)

#   Label(text = 'Registration succesful')
#root window of GUI

def testLogin(entry1,entry2):
    if(entry1 and entry2):
        print("0")
#         print("Username: ",entry1)
#         print("Password: ",entry2)
    else:
        print("invalid entry")

root = tk.Tk()



def Login():
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

#done BUTTON
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
    #reg()
    Login()
    


