
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
global my_tree
global dbconnect
root = tk.Tk()

# Connect to SQLite database
dbconnect = sqlite3.connect("testdata.db" )
dbconnect.row_factory = sqlite3.Row;

# Create a cursor and initialize it
cursor = dbconnect.cursor();

# Create database
try:
    cursor.execute(
        """CREATE TABLE gamedata
           (ShotNo integer, TargetForce integer, ShooterSpeed integer,
            HitorMiss integer,User text)""")
except Exception as E:
    print('Error: ', E)
else:
    print('table created')
def main():
    root.destroy()
    from MainMenuPage import MainMenu
    MainMenu()

def gameData():
    global datapage
    data = tkinter.messagebox.askyesno('Game Data','Are you sure you would like to view game data?')
    if data:
        datapage = Tk()
        datapage.title("Data Tab")
        datapage.geometry("1000x400")
        my_tree = ttk.Treeview(datapage)
        my_tree['columns'] = ("ShotNo","TargetForce", "ShooterSpeed", "Hit/Miss", "User")
    #my_tree.column("#0",width = 120, minwidth = 25)
        my_tree.column("ShotNo",width = 120,minwidth = 25)
        my_tree.column("TargetForce",anchor = CENTER,width = 120)
        my_tree.column("ShooterSpeed",anchor = W,width = 120)
        my_tree.column("Hit/Miss",anchor = W,width = 120)
        my_tree.column("User",anchor = W,width = 120)
        
        #my_tree.heading("#0", text = "Label", anchor = W)
        my_tree.heading("ShotNo", text = "ShotNo", anchor = W)
        my_tree.heading("TargetForce", text = "TargetForce", anchor = CENTER)
        my_tree.heading("ShooterSpeed", text = "ShooterSpeed", anchor = W)
        my_tree.heading("Hit/Miss", text = "HitorMiss", anchor = W)
        my_tree.heading("User", text = "Username", anchor = W)
    
#         sql_command = "INSERT INTO gamedata(ShotNo, TargetForce , ShooterSpeed,HitorMiss,User) VALUES (1,2,3,4,'Mister')"
#         cursor.execute(sql_command)
#     
#     dbconnect.commit()
        
        ans = cursor.execute("SELECT * FROM gamedata")
        #for row in cursor:
            #print("ShotNo: ",row['ShotNo'],"\nTargetForce: ",row['TargetForce'],"\nshooter: ",row['ShooterSpeed'],"\nHitorMiss: ",row['HitorMiss'],"\nUser: ",row['User'])
        list1 = cursor.fetchall()
        for n in range(len(list1)):
            p = list1[n]
            for i in p:
            
             #print(row['ShotNo'])
                my_tree.insert(parent= '',index = 'end',text = "Parent",values =i)
                n +=1
            my_tree.pack(pady = 20)
    
 
    #print(ans)
#     lst = [("Force at Target","Force from shooter","HIT/MISS","Shot #", "Username"),
#            ('','','','','',''),('','','','',''),('','','','','',''),('','','','','')]
#     total_rows = list1
#     total_columns = len(list1)
#     for row in cursor:
#         data_entry = Entry(datapage)
#         data_entry.grid(ipadx = 10, ipady = 10)
#         data_entry.insert(END,row['ShotNo'],row['TargetForce'],row['ShooterSpeed'], row['HitorMiss'],row['User'])
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
  button2 = tk.Button(dataframe,text = "GameData",font = 40,  fg =  'black',command = lambda: gameData())
  button2.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')
  
  
  messframe = tk.Frame(root,bg = '#ff99cc',bd = 5)
  messframe.place(relx = 0.5, rely = 0.5,relwidth = 0.4, relheight = 0.1,anchor = 'n')
  button3 = tk.Button(messframe,text = "Proceed to Main Menu",font = 40,  fg =  'black',command = lambda: main())
  button3.place(relx = 0.5,rely = 0.5, relwidth = 1, relheight = 1, anchor = 'center')

  root.mainloop()

if __name__ == "__main__":
    GameOver()
