from DataBase.DataBase import DB
from Utils import Utils
import bottle
from bottle import request, run, static_file
#This can be really shitty and there's still a lot of work, but this is practice so yes

class Server(object):
    def __init__(self):
        self.db = DB()

    def getScore(self):
        return static_file('WebScores.txt', root='')

    def getReplay(self):
        #replayID = request.query.ID < this handles replayID
        #return static_file(f'{replayID}' + '.txt', root='Scores/') #it's working but useless without replay data, so return Failed to connect
        return None

    def do_Upload(self):
        for x in request.body:
            Utils.createLBEntry(self.db, request.body.readlines())
        Utils.updateLB(self.db)
        return 'Uploaded'

handler = Server()
bottle.route("/GetScores_v5_5")(handler.getScore)
bottle.route("/GetReplay_5")(handler.getReplay)
bottle.route("/UploadScore_5", method='POST')(handler.do_Upload)
run(host='0.0.0.0', port=80, debug=True)
