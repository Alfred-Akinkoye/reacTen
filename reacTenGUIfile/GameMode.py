from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


HEIGHT = 500
WIDTH = 600

root = tk.Tk()
#This function calls  functions " WaitPage2" and "WaitPage
#"WaitPage2" displays a waiting page for Single Player mode
#"WaitPage" displays a waiting page for Multi Player mode
def WaitPage(button1,button2):
    if(button2):
        from WaitPage2 import WaitSingle
        root.destroy()
        WaitSingle()
    elif(button1):
        from WaitPage import Wait
        root.destroy()
        Wait()

#This function disables the MultiPlayer button and enables the continue button
def disableSingle():
    button2.config(state = DISABLED)
    button3.config(state = ACTIVE)

#This function disables the SinglePlayer button and enables the continue button
def disableMulti():
    button1.config(state = DISABLED)
    button3.config(state = ACTIVE)

#This function displays the game mode GUI
def GameMode():
  #defines all three buttons to be used globally
  global button1
  global button2
  global button3
#makes a container that holds the button(used for initial screen size)
  root.title("GameMode GUI")
  canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH )
  canvas.pack()

  #displays the background image in the GUI
  background_image = ImageTk.PhotoImage(file =('image_400.jpg'))
  background_label = tk.Label(root, image= background_image)
  background_label.place( relwidth = 1, relheight = 1)
  
  #Displays a welcome label before the player chooses a button
  welabel = tk.Label(root, text = "What GameMode would you like to play? Please select either box: ")
  welabel.place(relx = 0.11, rely =0.1, relwidth = 0.85, relheight = 0.1)
  
  #Frame for Gamemode buttons:Single and Multi players
  modeframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  modeframe.place(relx = 0.5, rely = 0.25,relwidth = 0.55, relheight = 0.1,anchor = 'n')

  #Displays the single player button
  button2 = tk.Button(modeframe,text = " Single Player",font = 40,  fg =  'black',command = lambda: disableMulti())
  button2.place(relx = 0,rely = 0, relwidth = 0.3, relheight = 1)
  
  #Displays the Multiplayer button
  button1 = tk.Button(modeframe,text = "Multi Player",font = 40, command = lambda: disableSingle())
  button1.place(relx = 0.7, rely = 0,relwidth = 0.3, relheight = 1)

  #Frame for Continue button
  messframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  messframe.place(relx = 0.5, rely = 0.5,relwidth = 0.15, relheight = 0.1,anchor = 'n')

  #Displays the continue button
  button3 = tk.Button(messframe,text = " Continue",font = 40,  fg =  'black',state = DISABLED, command = lambda: WaitPage(button1.invoke(),button2.invoke()))
  button3.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')

  #Used to run the root application
  root.mainloop()


if __name__ == "__main__":
    #reg()
    GameMode()
    


