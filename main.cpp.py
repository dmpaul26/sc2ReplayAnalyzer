import sys
from Tkinter import *

def initPlayerInfo(frame):
    playerInfo = Frame(frame)
    playerInfo.pack(side=RIGHT, fill=BOTH, expand=YES)

    playerOneInfo = Label(playerInfo, text="Player One Info", fg="white", bg="brown")
    playerOneInfo.pack(side=LEFT, fill=BOTH, expand=YES)

    playerTwoInfo = Label(playerInfo, text="Player Two Info", fg="white", bg="brown")
    playerTwoInfo.pack(side=RIGHT, fill=BOTH, expand=YES)

def initGameInfo(frame):
    minimapImage = PhotoImage(file='./sc2map.gif')
    mapLabel = Label(gameInfoFrame, image=minimapImage, height=200)
    mapLabel.image = minimapImage
    mapLabel.pack(side=TOP)

    gameInfo = Label(gameInfoFrame, text="Game Info", fg="white", bg="red")
    gameInfo.pack(side=BOTTOM, fill=Y, expand=YES)

def initHeader(frame):
    initMapView(frame)

myGUI = Tk()
myGUI.geometry('1024x768')

menubar = Menu(myGUI)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open Replay")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=myGUI.quit)
menubar.add_cascade(label="File", menu=filemenu)

header=Frame(myGUI)
header.pack(side=TOP, fill=X)

gameInfoFrame = Frame(header)
gameInfoFrame.pack(side=LEFT)

minimapImage = PhotoImage(file='./sc2map.gif')
mapLabel = Label(gameInfoFrame, image=minimapImage, height=200)
mapLabel.image = minimapImage
mapLabel.pack(side=TOP)

gameInfo = Label(gameInfoFrame, text="Game Info", fg="white", bg="red")
gameInfo.pack(side=BOTTOM, fill=Y, expand=YES)

initPlayerInfo(header)

graph = Label(myGUI, text="graph", fg="white", bg="blue")
graph.pack(side=LEFT, fill=BOTH, expand=YES)

scrollbar = Scrollbar(myGUI)
scrollbar.pack(side=RIGHT, fill=Y)

scrollStats = Listbox(myGUI, activestyle='none', fg="white", bg="brown", yscrollcommand=scrollbar.set, width = 50)
scrollStats.insert(END, "APM = 55")
scrollStats.pack(side=RIGHT, fill=Y)
myGUI.config(menu=menubar)

myGUI.mainloop()

