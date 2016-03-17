from urllib2 import URLError, urlopen
from Tkinter import *
import tkFont
from replayImporter import ReplayImporter
import time
import json

# Main Backend Handler
class TkHandler():

    def __init__(self):
        self.myGUI = Tk()
        self.myGUI.title('Sc2ReplayAnalyzer')
        self.myGUI.geometry('1024x768')

        self.replayImporter = ReplayImporter(self)
        self.createFrames()

        self.initFrames()

        #self.splashScreen.tkraise()
        self.myGUI.config(menu=self.menubar)

    def createFrames(self):
        #self.splashScreen = Frame(self.myGUI)
        self.userSelection = Frame(self.myGUI)
        self.matchReview = Frame(self.myGUI)
        self.playerProfile = Frame(self.myGUI)

    def initFrames(self):
        self.initMatchReview()

    def initStartScreen(self):
        self.startLabel = Label(self.splashScreen, text="Splash")
        self.startLabel.pack()

    def initMatchReview(self):
        self.menubar = Menu(self.myGUI)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.header = Frame(self.myGUI)
        self.header.pack(side=TOP, fill=X)

        self.initMenubar()
        self.initHeader()
        self.initStats()
        self.initGameDetails()


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

        self.gameInfo = Label(self.gameInfoFrame, text="Game Info")
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

    def initGameDetails(self):
        self.gameDetails = Frame(self.myGUI)
        self.gameDetails.pack(side=LEFT, fill=BOTH, expand=YES)

        detailsFont = tkFont.Font(family='Helvetica', size=18, weight='bold')

        self.playerOneDetailsFrame = Frame(self.gameDetails)
        self.playerOneDetailsFrame.pack(side=LEFT, fill=BOTH, expand=YES)

        self.playerOneDetailsHeader = Label(self.playerOneDetailsFrame, text="Player One Army", font=detailsFont)
        self.playerOneDetailsHeader.pack(side=TOP, fill=X)

        playerOneScrollbar = Scrollbar(self.playerOneDetailsFrame)
        playerOneScrollbar.pack(side=RIGHT, fill=Y)

        self.playerOneDetails = Listbox(self.playerOneDetailsFrame, font=detailsFont, yscrollcommand=playerOneScrollbar.set)
        self.playerOneDetails.pack(side=BOTTOM, fill=BOTH, expand=YES)

        playerOneScrollbar.config(command=self.playerOneDetails.yview)

        self.playerTwoDetailsFrame = Frame(self.gameDetails)
        self.playerTwoDetailsFrame.pack(side=LEFT, fill=BOTH, expand=YES)

        self.playerTwoDetailsHeader = Label(self.playerTwoDetailsFrame, text="Player Two Army", font=detailsFont)
        self.playerTwoDetailsHeader.pack(side=TOP, fill=X)

        playerTwoScrollbar = Scrollbar(self.playerTwoDetailsFrame)
        playerTwoScrollbar.pack(side=RIGHT, fill=Y)

        self.playerTwoDetails = Listbox(self.playerTwoDetailsFrame, font=detailsFont, yscrollcommand=playerTwoScrollbar.set)
        self.playerTwoDetails.pack(side=BOTTOM, fill=BOTH, expand=YES)

        playerTwoScrollbar.config(command=self.playerTwoDetails.yview)

    def initStats(self):
        self.statsFrame = Frame(self.myGUI)
        self.statsFrame.pack(side=RIGHT, fill=Y)

        Label(self.statsFrame, text="Game Stats", font=('Helvetica', '18', 'bold')).pack(side=TOP, fill=X)

        scrollbar = Scrollbar(self.statsFrame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.scrollStats = Listbox(self.statsFrame, yscrollcommand=scrollbar.set, width = 50)
        self.scrollStats.pack(side=BOTTOM, fill=Y, expand=YES)