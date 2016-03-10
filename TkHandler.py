from urllib2 import URLError, urlopen
from Tkinter import *
from replayImporter import ReplayImporter
import time
import json

# Main Backend Handler
class TkHandler():

    def __init__(self):
        self.myGUI = Tk()
        self.myGUI.geometry('1024x768')

        self.replayImporter = ReplayImporter(self)
        self.createFrames()

        self.initFrames()

        #self.splashScreen.tkraise()
        self.myGUI.config(menu=self.menubar)

    def createFrames(self):
        self.splashScreen = Frame(self.myGUI)
        self.userSelection = Frame(self.myGUI)
        self.matchReview = Frame(self.myGUI)
        self.playerProfile = Frame(self.myGUI)

    def initFrames(self):
        self.initMatchReview()

    def initSplashScreen(self):
        self.splashTime = 4

        print "HI"

        self.splashLabel = Label(self.splashScreen, text="Splash")
        self.splashLabel.pack()

        timeNow = time.time()

        if timeNow < self.splashTime:
            time.sleep (self.splashTime - timeNow)

        self.matchReview.tkraise()

    def initMatchReview(self):
        self.menubar = Menu(self.myGUI)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.header = Frame(self.myGUI)
        self.header.pack(side=TOP, fill=X)

        self.initMenubar()
        self.initHeader()
        self.initGraph()
        self.initStats()

    def initPlayerInfo(self):
        self.playerInfo = Frame(self.header)
        self.playerInfo.pack(side=RIGHT, fill=BOTH, expand=YES)

        self.playerOneInfo = Label(self.playerInfo, text="Player One Info")
        self.playerOneInfo.pack(side=LEFT, fill=BOTH, expand=YES)

        self.playerTwoInfo = Label(self.playerInfo, text="Player Two Info")
        self.playerTwoInfo.pack(side=RIGHT, fill=BOTH, expand=YES)


    def initGameInfo(self):
        self.gameInfoFrame = Frame(self.header)
        self.gameInfoFrame.pack(side=LEFT)

        self.minimapImage = PhotoImage(file='./sc2map.gif')
        self.mapLabel = Label(self.gameInfoFrame, image=self.minimapImage, height=200)
        self.mapLabel.pack(side=TOP)

        self.gameInfo = Label(self.gameInfoFrame, text="Game Info", fg="white", bg="red")
        self.gameInfo.pack(side=BOTTOM, fill=Y, expand=YES)

    def initHeader(self):
        self.initGameInfo()
        self.initPlayerInfo()

    def initMenubar(self):
        self.filemenu.add_command(label="Load Replay", command=self.replayImporter.loadReplay)
        self.filemenu.add_command(label="Import From GGTracker", command=self.replayImporter.promptUserID)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.myGUI.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

    def initGraph(self):
        self.graph = Label(self.myGUI, text="graph", fg="white", bg="blue")
        self.graph.pack(side=LEFT, fill=BOTH, expand=YES)

    def initStats(self):
        scrollbar = Scrollbar(self.myGUI)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.scrollStats = Listbox(self.myGUI, activestyle='none', fg="white", bg="brown", yscrollcommand=scrollbar.set, width = 50)
        self.scrollStats.insert(END, "APM = 55")
        self.scrollStats.pack(side=RIGHT, fill=Y)