import tkinter
from tkinter import *
filename = input("filename")
file = open(filename, "a")
root = Tk()
root.title('IOsoft')
Label(text='Edit').pack(side=TOP,padx=10,pady=10)

entry = Entry(root, width=100)
entry.pack(side=TOP,padx=10,pady=10)

def onok():
    writedata = entry.get()
    file.write(writedata)

def rekd():
    root.destroy()
    file.close()
Button(root, text='OK', command=onok).pack(side=LEFT)
Button(root, text='CLOSE', command=rekd).pack(side= RIGHT)

root.mainloop()
