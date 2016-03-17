from urllib2 import Request, urlopen, URLError
from Tkinter import *
from replayProcessor import ReplayProcessor
import tkFileDialog, json, sc2reader, os

class ReplayImporter():

    def __init__(self, TkHandler):
        self.parent = TkHandler

    def loadReplay(self):
        file_opt = {'defaultextension': '.SC2Replay',
                    'filetypes': [('SC2Replay', '.SC2Replay')]} #add initial dir from config file

        fileDialog = tkFileDialog.askopenfilename(**file_opt)

        if fileDialog:
            self.replay = sc2reader.load_replay(fileDialog)

            self.replayProcessor = ReplayProcessor(self.parent, self.replay)

    # TODO: Add get replay from matchID
    def getReplay(self):
        try:
            url = Request('http://api.ggtracker.com/api/v1/matches?category=Ladder&game_type=1v1&identity_id=' + self.userID +
                          '&replay=true&filter=-graphs,match(replays,-map,-map_url),entity(-summary,-minutes,-armies)')

            page = urlopen(url)

            self.getRecentMatch(page)
        except URLError, e:
            print "Could not load player data, error: ", e


    def promptUserID(self):
        self.promptID = Toplevel(self.parent.myGUI)

        Label(self.promptID, text="Enter GGTracker user ID:").pack()

        self.userEntry = Entry(self.promptID)
        self.userEntry.pack(padx=5)

        Button(self.promptID, text="Ok", command=self.getUserID, default=ACTIVE).pack(pady=5)
        Button(self.promptID, text="Cancel", command=self.promptID.destroy).pack()

        self.promptID.bind("<Return>", self.getUserID)

        self.promptID.grab_set() #not sure if  this does anything

    def getUserID(self, event=0):   #bind passes key as a second argument, event used as placeholder
        self.userID = self.userEntry.get()
        self.promptID.destroy()
        self.getReplay()

    def getRecentMatch(self, page): #processes the most recent 1v1 ranked match
        page_json = json.loads(page.read())

        replayURL = page_json['collection'][0]['replays'][0]['url']

        self.replay = sc2reader.load_replay(urlopen(Request(replayURL)))

        self.replayProcessor = ReplayProcessor(self.parent, self.replay)