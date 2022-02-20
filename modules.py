import psutil
import tkinter as tk
from tkinter import filedialog
import os
import time
import winapps


class Application:

    def __init__(self, name, path):

        self.name = name
        self.path = path



def fileBrowser():
    filename = tk.filedialog.askopenfilename(
        title = 'Select Game',
        initialdir=os.path.normpath("C:/"),
        filetypes = ''
    )

    newApplication = Application("Test",filename)

    print(newApplication.path, "\n", newApplication.name)

    return newApplication



root = tk.Tk()
root.title("Game Clock")
root.geometry('600x400+50+50')
root.configure(background=("#384a5a"))


menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)

filemenu.add_command(label="Add game", command=fileBrowser)
filemenu.add_separator()
filemenu.add_command(label="Open GameTime Folder")
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

for i in range(3):
    for j in range(3):
        e = tk.Entry(root, width=20, fg='blue',
                       font=('Arial', 16, 'bold'))

        e.grid(row=i, column=j)
        # e.insert(END, lst[i][j])



root.config(menu=menubar)

root.mainloop()
