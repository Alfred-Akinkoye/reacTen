
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
#from GameMode import GameMode

HEIGHT = 500
WIDTH = 600

global root


def show():
    tkinter.messagebox.showinfo("TKinterBox","Game will start soon...")
def WaitSingle():
  root = tk.Tk()
  root.title("WaitPage GUI")
  canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH)
  canvas.pack()

  background_image = ImageTk.PhotoImage(file =('image_400.jpg'))
  background_label = tk.Label(root, image= background_image)
  background_label.place( relwidth = 1, relheight = 1)
  # new_image = background_image.resize(HEIGHT,WIDTH)
  # new_image.save('image_new.jpg')
    
  #print(new_image.size)

  welabel = tk.Label(root, text = "You have selected Single Player Mode!")
  welabel.place(relx = 0.1, rely =0.1, relwidth = 0.85, relheight = 0.1)

  label1 = tk.Label(root,text = "Press continue to start!" )
  label1.place(relx = 0.1, rely =0.3, relwidth = 0.85, relheight = 0.1)
  
  messframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  messframe.place(relx = 0.5, rely = 0.5,relwidth = 0.15, relheight = 0.1,anchor = 'n')
  button3 = tk.Button(messframe,text = "Continue",font = 40,  fg =  'black',command = lambda: show())
  button3.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')

  root.mainloop()

if __name__ == "__main__":
    WaitSingle()
