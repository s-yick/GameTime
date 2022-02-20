from tkinter import *
import psutil
import tkinter as tk
import os
import time
import winapps


def buildAppList():
    """
    Takes all logged programs and places their name in a list
    :return: a list of program name strings
    """

    apps = []

    f = open("LogHours.txt", "r")

    next(f)

    for line in f:
        apps.append(line.split(" ")[0])


    f.close()
    return apps






def updateTime(AppName):
    """
    Updates time for given application, overwriting old file
    :param AppName: Name of running application
    :return: None
    """

    f = open("LogHours.txt", "r")
    open("LogTemp.txt", "x")
    f2 = open("LogTemp.txt", "r+")
    next(f)

    f2.write("\n")

    AppName = AppName.replace(" ", "_")
    for line in f:
        lineList = line.split()

        minutes = int(lineList[1])

        if(lineList[0] == AppName.lower()):
            minutes += 1

            foundAppUpdateString = AppName.lower() + " " + str(minutes)+"\n"
            f2.write(foundAppUpdateString)
        else:
            reWrite = lineList[0] + " " + lineList[1]
            f2.write(reWrite+"\n")

    f.close()
    f2.close()

    os.remove("LogHours.txt")
    os.rename("LogTemp.txt", "LogHours.txt")







def ifRunning(procname):
    """
    checks if given application is running
    :param procname: name of an application
    :return: boolean if application running
    """


    for i in psutil.process_iter():
        if procname.lower() in i.name().lower():
            return True

    return False






def addApplication(AppName):
    """
    Add an application to the list of applications
    :param AppName: Name of an application
    :return: None
    """

    file = open("LogHours.txt", "r")

    AppName = AppName.replace(" ", "_")

    if(AppName in file.read()):
        file.close()
        return

    else:

        file = open("LogHours.txt", "a")
        newAppLine = [AppName.lower(), " 0\n"]

        for i in newAppLine:
            file.write(i)

        print("Added", AppName, "to log")

        file.close()







def testSpotify():

    while ifRunning("Spotify"):
        time.sleep(10)
        updateTime("spotify")
        print("Spotify now at", getTime("spotify"))




def getTime(AppName):


    f = open("LogHours.txt", "r")
    next(f)
    for line in f:
        lineList = line.split()

        minutes = int(lineList[1])

        if(lineList[0] == AppName.lower()):
            f.close()
            return minutes

    f.close()
    return


def fileBrowser():
    filename = tk.filedialog.askopenfilename(initialdir="/System/Applications",
                                          title="Select a File",
                                          filetypes=(("Apps",
                                                      "*.app"),
                                                     ("all files",
                                                      "*.*"),))

    return filename


def listApps():
    f = open("applicationsRunning.txt", "a")

    for i in psutil.process_iter():
        f.write(str(i))
        f.write("\n")

    f.close()

root = tk.Tk()
root.title("Game Clock")
root.geometry('600x400+50+50')


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Add game")
filemenu.add_command(label="Add game manually")
filemenu.add_separator()
filemenu.add_command(label="Open GameTime Folder")
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)



root.config(menu=menubar)

root.mainloop()
