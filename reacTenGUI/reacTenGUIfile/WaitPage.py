from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
#from GameMode import GameMode

HEIGHT = 500
WIDTH = 600
global root

def Wait():
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
  #background_label.place( relwidth = 1, relheight = 1)

  welabel = tk.Label(root, text = "You have selected Multi Player Mode!")
  welabel.place(relx = 0.1, rely =0.1, relwidth = 0.85, relheight = 0.1)

  label1 = tk.Label(root,text = "We are waiting for the other player to finish set up! Waiting..." )
  label1.place(relx = 0.1, rely =0.3, relwidth = 0.85, relheight = 0.1)

  root.mainloop()

if __name__ == "__main__":
    Wait()
