#!/usr/bin/python3

# Copyright 2020 Patrick Warren

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import tkinter
import tkinter.filedialog as fd
from sys import argv
import os
from time import sleep
from platform import system

# linux users - this reads .Xresources file from your $HOME directory.
# this means your colors will restore to default if you run skedit as root.
# to fix this, copy your .Xresources to /root/
if system() == "Linux":
    home = os.environ["HOME"]
    # or, change 'home+"/.Xresources"' to '"yourusername/.Xresources"' in the follwing line
    try:
        Xresources = open(home+"/.Xresources")
        colors = Xresources.read()
        Xresources.close()
        print(colors)
    except FileNotFoundError:
        pass


filename = None

def newFile(self):
    global filename
    filename = "scratch document"
    text.delete(0.0, tkinter.END)
    root.title(filename+" - skedit")

def save(self):
    global filename
    t = text.get(0.0, tkinter.END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs(self):
    filename = fd.asksaveasfilename(initialdir="/gui/images", title="save as", defaultextension='.txt')
    f = open(filename, 'w')
    root.title(filename+" - skedit")
    t = text.get(0.0, tkinter.END)
    try:
        f.write(t.rstrip())
    except PermissionError:
        # messagebox.showinfo("skedit error", "Permission Denied")   
        text.delete(0.0, tkinter.END)

def openFile(self):
    global filename
    filename = fd.askopenfilename(initialdir="/gui/images", title="open file")
    f = open(filename, 'r')
    t = f.read()
    f.close()
    root.title(filename+" - skedit")
    text.delete(0.0, tkinter.END)
    text.insert(0.0, t)
    
#Tk
root = tkinter.Tk()
root.title("scratch document - skedit")

#bindings
root.bind('<Control-s>', save)
root.bind('<Control-n>', newFile)
root.bind('<Control-d>', saveAs)
root.bind('<Control-o>', openFile)

text = tkinter.Text(root)
root.update()
text.configure(background='white', height=root.winfo_height(), width=root.winfo_width())
root.maxsize(1500, 1000)
root.update()
text.focus_set()
print (root.winfo_geometry())

text.pack()
if system() == "Linux":
    root.iconphoto(False, tkinter.PhotoImage(file='/usr/share/skeditFiles/icon.png'))
elif system() == "Windows":
    root.iconphoto(False, tkinter.PhotoImage(file='C:\\Program Files\\skeditFiles\\icon.png'))
root.mainloop()