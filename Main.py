import modules as mc
import time
import tkinter as tk
import tkinter.messagebox as tkm
import tkinter.simpledialog as tksd


def Add():
    mc.fileBrowser()

window = tk.Tk()
window.geometry("300x300")
window.title("AppC")

AddButton = tk.Button(text ="Add Application", command = Add)

AddButton.pack()

window.mainloop()



# while True:
#
#     time.sleep(10)
#
#     apps = mc.buildAppList()
#
#     for i in apps:
#         if mc.ifRunning(i):
#             mc.updateTime(i)
