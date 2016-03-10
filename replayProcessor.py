import sc2reader

class ReplayProcessor():
    def __init__(self, TkHandler, replayFile):
        self.replay = replayFile
        self.TkHandler = TkHandler

        self.initReplayInfo()

    def initReplayInfo(self):
        self.updatePlayerInfo()

    ## Updates player info panes
    def updatePlayerInfo(self):
        for player in self.replay.players:
            if player.team is self.replay.teams[0]:
                self.TkHandler.playerOneInfo.config(text=player.name)
            elif player.team is self.replay.teams[1]:
                self.TkHandler.playerTwoInfo.config(text=player.name)

