from tkinter import *
from tkinter import filedialog
#setting up parent window
root = Tk()

#function definition for opening file dialog
def openf():
    file = filedialog.askopenfilename(initialdir='/', title="select file")

file_open = Button(root, text="Open file", command= openf)
file_open.pack(pady=20)

root.geometry("350x200")
root.title("PythonLobby.com")
root.mainloop()