from bottle import route, request, run, static_file
#This can be really shitty and there's still a lot of work, but this is practice so yes
@route("/GetScores_v5_5")
def getScore():
    return static_file('WebScores.txt', root='')
@route("/UploadScore_5", method='POST')
def do_Upload():
    return 'Beep. Boop.' #returning something so it's not Failed to connect to server

run(host='0.0.0.0', port=80, debug=True)
