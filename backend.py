import sqlite3

class Database:

    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,first text,last text,email integer,password integer)")
        self.con.commit()
        

    def insert(self,first,last,email,password):
        # conn = sqlite3.connect("books.db")
        # curr = conn.cursor()
        self.cur.execute("INSERT INTO user VALUES (NULL,?,?,?,?)",(first,last,email,password))
        self.con.commit()
        

    # def viwe(self):
    #     # conn = sqlite3.connect("books.db")
    #     # curr = conn.cursor()
    #     self.cur.execute("SELECT * FROM book")
    #     row = self.cur.fetchall()
       
    #     return row

    # def search(self,title="",author="",year="",isbn=""):
    #     # conn = sqlite3.connect("books.db")
    #     # curr = conn.cursor()
    #     self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))   
    #     row = self.cur.fetchall()
        
    #     return row

    # def delete(self,id):
    #     # conn = sqlite3.connect("books.db")
    #     # curr = conn.cursor()
    #     self.cur.execute("DELETE FROM book WHERE id=?",(id,))
    #     self.con.commit()
        

    # def update(self,id,title,author,year,isbn):
    #     # conn = sqlite3.connect("books.db")
    #     # curr = conn.cursor()
    #     self.cur.execute("UPDATE book SET title=? , author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    #     self.con.commit()
        

