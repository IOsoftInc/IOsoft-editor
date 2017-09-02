from tkinter import *
import os
root = Tk()
def regular(file):
    os.system(file)
Button(root, text='Regular Edit', command=regular("start.py")).pack(side=LEFT)
Button(root, text='WYSIWYG', command=regular("startw.py")).pack(side= RIGHT)

root.mainloop()
