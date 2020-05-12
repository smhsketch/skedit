#    Copyright 2020 Patrick Warren

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
from sys import argv, exit
import os
from platform import system
from math import floor
from time import sleep

colorWheel = []
colorWheel2 = []

# Logging functions
def log(n):
    print("[#]", n)
def warn(n):
    print("[!]", n)
def die(n):
    print("[XX]", n)
    sleep(5)
    exit(1)


# define config file path
if system() == "Windows":
    configPath = "C:\\Program Files\\skedit\\skeditFiles\\skeditConf.txt"
else: # Assuming other operating systems are UNIX-like
    configPath = "/usr/share/skeditFiles/skeditConf.txt"

# Checks if the config file exists
try:
    configFile = open(configPath)
except FileNotFoundError:
    die("skedit configuration missing.")

config = configFile.readlines()
configFile.close()

# get info from config file
try:
    fontSize = config[config.index("fontSize:\n") + 1] 
except:
    fontSize = 15
try:
    defSize = config[config.index("defaultSize:\n") + 1]
    defSize = defSize[:-1]
except:
    defSize = "500x500"
try:
    useDefSize = config[config.index("applyDefaultSizeAtStartup:\n") + 1]
except:
    useDefSize = "true"
try:
    # get resources preference from config file
    ignoreRes = config[config.index("ignoreResources:\n") + 1]
except:
    ignoreRes = "false"
if ignoreRes != "true":
    # windows users -  this reads the skedit resources file.
    # the formatting for this file mimics the formatting of a *nix .Xresources file.
    if system() == "Windows":
        try:
            Xresources = open("C:\\Program Files\\skedit\\skeditFiles\\skeditResources.txt")
            colors = Xresources.readlines()
            Xresources.close()
        except FileNotFoundError:
            pass
    # linux users - this reads .Xresources file from your $HOME directory.
    # this means your colors will restore to default if you run skedit as root.
    # to fix this, copy your .Xresources to /root/
    else:
        home = os.environ["HOME"]
        # or, change 'home+"/.Xresources"' to '"yourusername/.Xresources"' in the follwing line
        try:
            Xresources = open(home+"/.Xresources")
            colors = Xresources.readlines()
            Xresources.close()
        except FileNotFoundError:
            pass
    try:
        for i in range(16):
                colorWheel.append([x for x in colors if ("*.color" + str(i) + ":") in x])
                # the worst line of code ever written
                colorWheel2.append((str(colorWheel[i]).replace("*.color" + str(i) + ":", "")).replace(" ", "").replace("\\n", "").replace("['", "").replace("']", ""))
        foreground = str([a for a in colors if ("*.foreground:") in a]).replace(" ", "")
        foreground = foreground.replace("['*.foreground:", "").replace("\\n']", "")
        background = str([a for a in colors if ("*.background:") in a]).replace(" ", "")
        background = background.replace("['*.background:", "").replace("\\n']", "")
        cursor = str([a for a in colors if ("*.cursorColor:") in a])
        cursor = cursor.replace("['*.cursorColor:", "").replace("\\n']", "").replace(" ", "")
    except:
        background = '#1c1c1c'
        foreground='#d6d6d6'
        cursor='#d6d6d6'
        pass
else:
    print("ignoring resources file")

filename = "scratch document"

# main functions for using editor

def get_text():
    t = text.get(0.0, tkinter.END).rstrip()
    return t

def newFile(self):
    global filename
    filename = "scratch document"
    text.delete(0.0, tkinter.END)
    root.title(filename+" - skedit")

def save(self):
    global t
    t = get_text()
    with open(filename, 'w') as f:
        f.write(t)

def saveAs(self):
    global filename
    fn = fd.asksaveasfilename(initialdir="~", title="save as", defaultextension='.txt')
    with open(fn, 'w') as f:
        root.title(fn+" - skedit")
        t = get_text()
        try:
            f.write(t)
        except:
            warn("unable to save file.")
        else:
            filename = fn

def openFile(self):
    global filename
    fn = fd.askopenfilename(title="open file")
    
    try:
        t = open(fn, 'r').read()
    except:
        return
    else:
        filename = fn
    root.title(filename+" - skedit")
    text.delete(0.0, tkinter.END)
    text.insert(0.0, t)

def gotoTop(self):
    text.mark_set("insert", "%d.%d" % (0, 0))

def removeLine(self):
    curLine = float(floor(float(text.index(tkinter.INSERT))))
    text.delete(curLine, curLine+1)

def helpMenu(self):
    global t
    if root.title() != "scratch document":
        save(None)
    t = get_text()
    root.title("help - skedit")
    text.delete(0.0, tkinter.END)
    helpText =  """Welcome to skedit, the cross-platform, dark-mode by default, simple text editor.

skedit is built with python, and tkinter. source code is available at https://github.com/smhsketch/skedit.

bindings:
    ctrl-o: open a new file
    ctrl-s: save current file
    ctrl-d: save current buffer as
    ctrl-n: new blank buffer
    ctrl-t: go to top of buffer
    ctrl-r: remove current line of buffer
    ctrl-e: exit this help menu and return to your document"""
    text.insert(0.0, helpText)

def exitHelp(self):
    if root.title() == "help - skedit":
        text.delete(0.0, tkinter.END)
        text.insert(0.0, t)
        root.title(filename+" - skedit")

#Tk
root = tkinter.Tk()
root.title("scratch document - skedit")

#bindings
root.bind('<Control-s>', save)
root.bind('<Control-n>', newFile)
root.bind('<Control-d>', saveAs)
root.bind('<Control-o>', openFile)
root.bind('<Control-t>', gotoTop)
root.bind('<Control-r>', removeLine)
root.bind('<Control-h>', helpMenu)
root.bind('<Control-e>', exitHelp)

text = tkinter.Text(root)
root.update()
text.configure(background=background, fg=foreground, insertbackground=cursor, height=root.winfo_height(), width=root.winfo_width(), bd=0, font=("monospace", fontSize))
if useDefSize == "true\n":
    root.geometry(defSize)
root.maxsize(1500, 1000)
root.update()
text.focus_set()

text.pack()
try:
    if system() == "Windows":
        root.iconphoto(False, tkinter.PhotoImage(file='C:\\Program Files\\skedit\\skeditFiles\\icon.png'))
    else:
        root.iconphoto(False, tkinter.PhotoImage(file='/usr/share/skeditFiles/icon.png'))
except:
    pass

root.mainloop()