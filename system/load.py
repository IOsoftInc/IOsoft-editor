from tkinter import *
import os
root = Tk()
def regular(file):
    os.system(file)
Button(root, text='Regular Edit', command=regular("nonWysiwyg.py")).pack(side=LEFT)
Button(root, text='WYSIWYG', command=regular("wysiwyg.py")).pack(side= RIGHT)

root.mainloop()
