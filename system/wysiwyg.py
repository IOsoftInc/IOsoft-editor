import os
from tkinter import *
filename = input("filename ")
if filename = "":
    os.system("system/blank.vbs")
else:
	file = open(filename, "a")
	root = Tk()
	def addp():
	    text = input("text> ")
	    file.write("print('" + text + "')")
	def addi():
	    modual = input("from ")
	    function = input(" import ")
	    file.write("from " + modual + " import " + function)
	def ececute():
	    filee = input("filename ")
	    os.system(filee)
	Button(root, text='print()', command=addp).pack(side=TOP)
	Button(root, text='from _ import _', command=addi).pack(side=TOP)
	Button(root, text='ececute', command=ececute).pack(side=BOTTOM)
	root.mainloop()
	file.close()
