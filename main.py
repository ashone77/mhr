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
    global file
    file = fd.askopenfilename(initialdir='/', title="select file", filetypes = (("jpeg files", "*.jpg"),("all files", "*.*")))


appName.pack()

file_open = Button(root, text="Open file", command= openf)
file_open.pack(pady=20)


# img = PhotoImage(file)
# label = Label(root, image=img).pack()

recognize = Button(root, text="Recognize", command= openf)
recognize.pack(pady=20)
root.mainloop()