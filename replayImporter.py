from urllib2 import Request, urlopen, URLError
from Tkinter import *
from replayProcessor import ReplayProcessor
import tkFileDialog, json, sc2reader, os

class ReplayImporter():

    def __init__(self, TkHandler):
        self.parent = TkHandler
        # if matchID:
        #
        # else:
        #     try:
        #         url = 'http://api.ggtracker.com/api/v1/matches?category=Ladder&game_type=1v1&identity_id=' + userID
        #
        #         request = Request(url)
        #         self.lastTen = urlopen(request)
        #
        #     except URLError, e:
        #         print "Didn't load, error: ", e
        #         self.replay = sc2reader.load_replay('SC2Replay.SC2Replay')

    def loadReplay(self):
        file_opt = {'defaultextension': '.SC2Replay',
                    'filetypes': [('SC2Replay', '.SC2Replay')]} #add initial dir from config file

        fileDialog = tkFileDialog.askopenfilename(**file_opt)

        if fileDialog:
            self.replay = sc2reader.load_replay(fileDialog)

            self.replayProcessor = ReplayProcessor(self.parent, self.replay)

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
        self.promptID.transient(self.parent.myGUI)

        Label(self.promptID, text="Enter GGTracker user ID:").pack()

        self.userEntry = Entry(self.promptID)
        self.userEntry.pack(padx=5)

        Button(self.promptID, text="Ok", command=self.getUserID, default=ACTIVE).pack(pady=5)
        Button(self.promptID, text="Cancel", command=self.promptID.destroy).pack()

        self.promptID.bind("<Return>", self.getUserID)

        self.promptID.grab_set()

    def getUserID(self):
        self.userID = self.userEntry.get()
        self.promptID.destroy()
        self.getReplay()

    ## Updates player info panes, playerPID = ID of player, num is their player # for current replay
    def updatePlayerInfo(self):
        for player in self.replay.players:
            if player.team is self.replay.teams[0]:
                self.parent.playerOneInfo.config(text=player.name)
            elif player.team is self.replay.teams[1]:
                self.parent.playerTwoInfo.config(text=player.name)

    def getRecentMatch(self, page):
        page_json = json.loads(page.read())

        replayURL = page_json['collection'][0]['replays'][0]['url']

        self.replay = sc2reader.load_replay(urlopen(Request(replayURL)))

        self.replayProcessor = ReplayProcessor(self.parent, self.replay)