from tkinter import *
import tkinter.filedialog
from sys import argv

filename = None
# filetoopen = argv[1]

def new():
    global filename
    filename = "scratch document"
    text.delete(0.0, END)

def save():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Error Occurred", message="Couldn't save the file.")

def open():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("skedit")

text = Text(root)
text.configure(background='white')
text.pack()

root.mainloop()