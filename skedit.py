from tkinter import *
import tkinter.filedialog as fd
from sys import argv

filename = None
# filetoopen = argv[1]

def newFile(self):
    global filename
    filename = "scratch document"
    text.delete(0.0, END)

def save(self):
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs(self):
    f = fd.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except PermissionError:
        # messagebox.showinfo("Title", "a Tk MessageBox")
        print("permission denied!!! cringe")
        
def openFile(self):
    f = fd.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

#Tk
root = Tk()
root.title("skedit")

#bindings
root.bind('<Control-s>', save)
root.bind('<Control-n>', newFile)
root.bind('<Control-d>', saveAs)
root.bind('<Control-o>', openFile)

text = Text(root)
root.update()
text.configure(background='white', height=root.winfo_height(), width=root.winfo_width())
print (root.winfo_geometry())

text.pack()
root.mainloop()