from tkinter import *
import tkinter
import csv
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#filepath = 'C:/Users/Arpitha/Downloads/userdata.csv'
#File=open(filepath)
#Reader = csv.reader(File)
#Data = list(Reader)

#print(Data)

plt.style.use('bmh')
data = pd.read_csv('userdata.csv')

x = data['git username']
y = data['no of repositories']

# bar chart

plt.xlabel('Username', fontsize=18)
plt.ylabel('Followers', fontsize=16)
plt.bar(x,y)
plt.show()

data = pd.read_csv('repositorydata.csv')

a = data['repository name']
b = data['commit frequency']

plt.xlabel('Repository', fontsize=18)
plt.ylabel('Commit freq', fontsize=16)
#plt.scatter(x,y)
plt.plot(a,b)
plt.show()



