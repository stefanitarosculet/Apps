import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("App_bookStore.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text,author text, year integer, isbn integer)")
        self.conn.commit()

    def Insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))

    def View(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def Search(self,title = "", author = "", year = "", isbn = ""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def Delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id = ?",(id,))
        self.con.commit()

    def Update(self,id,title, author, year, isbn):
        self.cur.execute("UPDATE book SET title =?, author = ?, year =?, isbn =? WHERE id =?", (title, author, year, isbn, id))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
    #Connect()
#Insert("The mountains", "Stefan Rosculet", 2020, 9812674160)
#Search("Stefan Rosculet")
#print(View())
