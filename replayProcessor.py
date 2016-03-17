from Tkinter import END

class ReplayProcessor():
    def __init__(self, TkHandler, replayFile):
        self.replay = replayFile
        self.TkHandler = TkHandler

        self.initReplayInfo()

    def initReplayInfo(self):
        self.getArmy()
        self.updatePlayerInfo()
        self.updateGameInfo()

    ## Updates player info panes
    def updatePlayerInfo(self):
        for player in self.replay.players:
            if player.team is self.replay.teams[0]:
                #TODO: make scroll stats or list to hold armies

                for unitName in self.army_map[player]:
                    self.TkHandler.playerOneDetails.insert(END, unitName)

                self.TkHandler.playerOneInfo.config(text=player.name, bg="#" + player.color.hex, fg="white")
                self.TkHandler.playerOneDetails.config(bg="#" + player.color.hex, fg="white")
                self.TkHandler.playerOneDetailsHeader.config(text=player.name + " Army")

            elif player.team is self.replay.teams[1]:

                for unitName in self.army_map[player]:
                    self.TkHandler.playerTwoDetails.insert(END, unitName)

                self.TkHandler.playerTwoInfo.config(text=player.name, bg="#" + player.color.hex, fg="white")
                self.TkHandler.playerTwoDetails.config(bg="#" + player.color.hex, fg="white")
                self.TkHandler.playerTwoDetailsHeader.config(text=player.name + " Army")
    def updateGameInfo(self):

        #TODO: Grab map image from internet
        timeSecs = self.replay.game_length.seconds #gives game time, not real time
        formattedTime = "Match Duration {}:{}".format(str(timeSecs/60), str(timeSecs%60))

        self.TkHandler.gameInfo.config(text=formattedTime)

    #TODO: Get unit create/killed times
    def getArmy(self):
        self.army_map = dict()

        for player in self.replay.players:
            playerArmy = list()
            for unit in player.units:
                if unit.name.startswith("Beacon"):
                    continue
                playerArmy.append(unit.name)

            self.army_map[player] = playerArmy