from urllib2 import Request, urlopen, URLError
import json
import sc2reader

class ReplayImporter():

    def __init__(self, userID):
        if matchID:

        else:
            try:
                url = 'http://api.ggtracker.com/api/v1/matches?category=Ladder&game_type=1v1&identity_id=' + userID

                request = Request(url)
                self.lastTen = urlopen(request)

            except URLError, e:
                print "Didn't load, error: ", e
                self.replay = sc2reader.load_replay('SC2Replay.SC2Replay')
