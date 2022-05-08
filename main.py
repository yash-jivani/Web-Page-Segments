import email
from flask_mail import Mail, Message
import sqlite3
from flask import Flask, flash,render_template,request
from sqlite3 import Row
from backend import Database
import random
import math
import math, random

my_email = "venilkhunt3223@gmail.com"
my_password = "Vkhunt32g" 

def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP

otp_gen = generateOTP() 
database = Database("user.db")

app = Flask(__name__)
mail = Mail(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = my_email
app.config['MAIL_PASSWORD'] = my_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/',methods=['GET','POST'])
def index_html():

    if request.method=="POST":
        email_add = request.form["email"]
        password = request.form["password"]   
          
    return render_template('index.html')



@app.route('/forget-password.html',methods=["GET",'POST'])
def forgot():
    if request.method=="POST":
        name = request.form['last']
        msg = Message(
                         'Hello',
                         sender =my_email,
                         recipients = [name]
                     )
        msg.body = f'{otp_gen}'
        mail.send(msg)
        
    return render_template('forget-password.html')    

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

@app.route('/otp-verification.html',methods=['GET','POST'])
def otp():
    if request.method=="POST":
        first = request.form["first"]       
        second = request.form["sec"]
        three = request.form["the"]
        four = request.form["four"]
        five = request.form["five"]
        six = request.form["six"]
        final_otp = first+second+three+four+five+six
        print(final_otp)
        if final_otp!=otp_gen:
            flash("re enter otp")
           
    return render_template('otp-verification.html')

@app.route('/reset-password.html',methods=["GET","POST"])
def reset():
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
    
        with sqlite3.connect("user.db")as con:
            cur = con.cursor()
            cur.execute("UPDATE user SET password=? WHERE email=?",(password,email))
            con.commit()

    return render_template("reset-password.html")


if __name__==("__main__"):
    app.run(debug=1)