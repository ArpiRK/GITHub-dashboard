
from tkinter import *
import tkinter
import csv
from PIL import ImageTk, Image

import numpy as np
import matplotlib.pyplot as plt

filepath = 'C:/Users/Arpitha/Downloads/userdata.csv'
File=open(filepath)
Reader = csv.reader(File)
Data = list(Reader)

#print(Data)

listofentries = []
for x in list(range(0, len(Data))):
  listofentries.append(Data[x][1])

root = Tk()
root.geometry('280x300')

listbox1 = Listbox(root)
var = StringVar(value=listofentries)
listbox1=Listbox(root, listvariable= var)

listbox1.grid(row=0, column=0)

def update():
  index = listbox1.curselection()[0]
  slno1.config(text = Data[index][0])
  gitusername1.config(text = Data[index][1])
  fullname1.config(text = Data[index][2])
  numberofrepos1.config(text = Data[index][3])
  followers1.config(text = Data[index][4])
  location1.config(text = Data[index][5])

  return None
  #print(index)
  #return None

button1 = Button(root, text="Update", command=update)
button1.grid (row=20, column=1)

slno = Label(root, text="SL no").grid(row=1, column=0, sticky="W")
gitusername = Label(root, text="GIT Username").grid(row=2, column=0, sticky="W")
fullname = Label(root, text="Fullname").grid(row=3, column=0, sticky="W")
numberofrepos = Label(root, text="NumberofRepos").grid(row=4, column=0, sticky="W")
followers = Label(root, text="Followers").grid(row=5, column=0, sticky="W")
location = Label(root, text="Location").grid(row=6, column=0, sticky="W")

slno1 = Label(root, text="")
slno1.grid(row=1, column=1, sticky="W")
gitusername1 = Label(root, text="")
gitusername1.grid(row=2, column=1, sticky="W")
fullname1 = Label(root, text="")
fullname1.grid(row=3, column=1, sticky="W")
numberofrepos1 = Label(root, text="")
numberofrepos1.grid(row=4, column=1, sticky="W")
followers1 = Label(root, text="")
followers1.grid(row=5, column=1, sticky="W")
location1 = Label(root, text="")
location1.grid(row=6, column=1, sticky="W")


root.mainloop()
