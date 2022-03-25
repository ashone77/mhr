import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Malayalam Handwriting Recognition")
root.geometry("500x500")

appName = tk.Label(text="Malayalam Handwriting Recognition", font=("Helvetica", 20))

def openf():
    file = filedialog.askopenfilename(initialdir='/', title="select file")

file_open = Button(root, text="Open file", command= openf)
file_open.pack(pady=20)


appName.pack()


recognize = Button(root, text="Recognize", command= openf)
recognize.pack(pady=20)
root.mainloop()