import sqlite3
from flask import Flask,render_template,request
from sqlite3 import Row
from backend import Database

database = Database("user.db")

app = Flask(__name__)

@app.route('/')

def index_html():
    return render_template('index.html')

@app.route('/forget-password.html')
def forgot():
    return render_template("forget-password.html")

@app.route('/signup.html',methods=['GET','POST'])
def sing_up():
    if request.method=='POST':
        first = request.form['first']
        last = request.form['last']
        email = request.form['email']
        password= request.form['password']
        conf = request.form['conf']
        if password==conf:
            
            with sqlite3.connect("user.db")as con:
                first_name = first
                last_name = last
                email_add = email
                password_add = password

                cur = con.cursor()
                cur.execute("INSERT INTO user VALUES (NULL,?,?,?,?)",(first,last,email,password))
                con.commit()
        else:
            print("Not ok")        
        

    return render_template('signup.html')

@app.route('/index.html')
def index():
    return render_template('index.html') 


if __name__==("__main__"):
    app.run(debug=1)