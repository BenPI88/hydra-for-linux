from tkinter import *
import time
import string
import random

def open2():
  i = 0
  while not i == 10:
    i += 1
    open()

def open():

  randomstring = ""
  i = 0
  while not i == 1000:
    i += 1
    randomstring = randomstring + string.ascii_uppercase[random.randint(0, 25)]
  window=Tk()
  # add widgets here
  lbl = Label(window, text=randomstring, fg='black', font=("Helvetica", 16))
  lbl.place(x=10, y=10)
  randomstring = ""
  i = 0
  while not i == 1000:
    i += 1
    randomstring = randomstring + string.ascii_uppercase[random.randint(0, 25)]
  window.title(randomstring)
  window.geometry("500x100+" + str(random.randint(10, 100)) + "+" + str(random.randint(10, 100)))
  
  window.protocol('WM_DELETE_WINDOW', open2)

window=Tk()
# add widgets here
lbl = Label(window, text="?????", fg='black', font=("Helvetica", 16))
lbl.place(x=10, y=10)
  
window.title("Hydra")
window.geometry("500x100+10+20")
  
window.protocol('WM_DELETE_WINDOW', open2)

window.mainloop()
