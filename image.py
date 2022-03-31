import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


# from Tkinter import Label,Tk
# from PIL import Image, ImageTk
# import tkFileDialog
root = Tk()

path=fd.askopenfilename(filetypes=[("Image File",'.jpg')])
im = Image.open(path)
tkimage = PhotoImage(im)
myvar=Label(root,image = tkimage)
myvar.image = tkimage
myvar.pack()

root.mainloop()
