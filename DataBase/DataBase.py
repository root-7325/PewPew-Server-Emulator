import sqlite3

class DB:
    def __init__(self):
        self.con = sqlite3.connect("DataBase/Database.db")
        self.cur = self.con.cursor()
        try:
            self.cur.execute("CREATE TABLE main(nickName text, score integer, mapName text)")
        except Exception as e:
            print(e)
        
    def createRecord(self, nickName, score, mapName):
        self.cur.execute(f"SELECT * FROM main WHERE nickName = ? AND score = ? AND mapName = ?", (nickName, score, mapName,)) 
        if self.cur.fetchone() is None:
            self.cur.execute(f"INSERT INTO main (nickName, score, mapName) VALUES (?, ?, ?)", (nickName, score, mapName,))
            self.con.commit() #create entry
        elif self.cur.fetchone() is not None:
            pass #entry exist

    def loadSorted(self, mapName):
        self.cur.execute("SELECT * FROM main WHERE mapName=? ORDER BY score DESC", (mapName, ))
        return self.cur.fetchall()