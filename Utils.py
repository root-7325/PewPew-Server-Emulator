import json
#CAUTION: CODE BELOW IS VERYx7325 BAD! IT WILL BE REWRITED IN FUTURE
class Utils():
    def createLBEntry(db, data):
        nickName = ""
        score = 0
        mapName = ""
        if "nickName" in str(data[2]):
            toSlice = str(data[3])
            nickName = toSlice[2: -5 :]
        if "score" in str(data[5]):
            toSlice = str(data[6])
            score = toSlice[2: -5 :]
        if "mapName" in str(data[20]):
            toSlice = str(data[21])
            mapName = toSlice[2: -5 :]
        db.createRecord(nickName, score, mapName)

    def updateLB(db):
        open('WebScores.txt', 'w').close() #clearing file to regenerate it
        modeData = json.loads(open("Modes.json", 'r').read())
        megagore = db.loadSorted(modeData[0]["Megagore"])
        dodgethis = db.loadSorted(modeData[1]["DodgeThis"])
        assault = db.loadSorted(modeData[2]["Assault"])
        asteroids = db.loadSorted(modeData[3]["Asteroids"])
        chromaticconflict = db.loadSorted(modeData[4]["ChromaticConflict"])
        highway = db.loadSorted(modeData[5]["Highway"])
        amalgam = db.loadSorted(modeData[6]["Amalgam"])
        symbiosis = db.loadSorted(modeData[7]["Symbiosis"])
        pacifism = db.loadSorted(modeData[8]["Pacifism"])
        with open('WebScores.txt', 'a') as entry:
                entry.write('pewpew2\n')
                entry.write('v5\n')
                entry.write("/data/levels/infinity/megagore/megagore.lua\n")
                entry.write(f"{len(megagore)}\n")
                for player in megagore:
                    entry.write(f"{player[0]}\n")
                    entry.write(f"{str(player[1])}\n")
                    entry.write("1\n") #hardcoding replayID
                    entry.write("0\n") #uknown
                entry.write("/data/levels/infinity/dodge this/dodge this.lua\n")
                entry.write(f"{len(dodgethis)}\n")
                for player in dodgethis:
                    entry.write(f"{player[0]}\n")
                    entry.write(f"{str(player[1])}\n")
                    entry.write("1\n") #hardcoding replayID
                    entry.write("0\n") #uknown
                entry.write("/data/levels/infinity/assault/assault.lua\n")
                entry.write(f"{len(assault)}\n")
                for player in assault:
                    entry.write(f"{player[0]}\n")
                    entry.write(f"{str(player[1])}\n")
                    entry.write("1\n") #hardcoding replayID
                    entry.write("0\n") #uknown
                entry.write("/data/levels/infinity/asteroids/asteroids.lua\n")
                entry.write(f"{len(asteroids)}\n")
                for player in asteroids:
                    entry.write(f"{player[0]}\n")
                    entry.write(f"{str(player[1])}\n")
                    entry.write("1\n") #hardcoding replayID
                    entry.write("0\n") #uknown
                entry.write("/data/levels/infinity/chromatic conflict/chromatic conflict.lua\n")
                entry.write(f"{len(chromaticconflict)}\n")
                for player in chromaticconflict:
                    entry.write(f"{player[0]}\n")
                    entry.write(f"{str(player[1])}\n")
                    entry.write("1\n") #hardcoding replayID
                    entry.write("0\n") #uknown
                entry.write("/data/levels/infinity/highway/highway.lua\n")
                entry.write(f"{len(highway)}\n")
                for player in highway:
                    entry.write(f"{player[0]}\n")
                    entry.write(f"{str(player[1])}\n")
                    entry.write("1\n") #hardcoding replayID
                    entry.write("0\n") #uknown
                entry.write("/data/levels/infinity/amalgam/amalgam.lua\n")
                entry.write(f"{len(amalgam)}\n")
                for player in amalgam:
                    entry.write(f"{player[0]}\n")
                    entry.write(f"{str(player[1])}\n")
                    entry.write("1\n") #hardcoding replayID
                    entry.write("0\n") #uknown
                entry.write("/data/levels/infinity/symbiosis/symbiosis.lua\n")
                entry.write(f"{len(symbiosis)}\n")
                for player in symbiosis:
                    entry.write(f"{player[0]}\n")
                    entry.write(f"{str(player[1])}\n")
                    entry.write("1\n") #hardcoding replayID
                    entry.write("0\n") #uknown
                entry.write("/data/levels/infinity/pacifism/pacifism.lua\n")
                entry.write(f"{len(pacifism)}\n")
                for player in pacifism:
                    entry.write(f"{player[0]}\n")
                    entry.write(f"{str(player[1])}\n")
                    entry.write("1\n") #hardcoding replayID
                    entry.write("0\n") #uknown