from typing import List, Dict
from flask import Flask
from flask import Flask, render_template
#import mysql.connector
import json

app = Flask(__name__)
'''
config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
    }
con = mysql.connector.connect(**config)
c = connection.cursor()
    
def test_table() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
    }
    con = mysql.connector.connect(**config)
    c = con.cursor()
    c.execute('SELECT * FROM test_table')
    results = [{name: color} for (name, color) in cursor]
    c.close()
    con.close()

    return results

@app.route('/')
def index() -> str:
    return json.dumps({'test_table': test_table()})

@app.route('/login', methods =['GET', 'POST']) 
def login(): 
    msg = '' 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form: 
        username = request.form['username'] 
        password = request.form['password'] 
        
        c.execute("""SELECT * FROM accounts WHERE username = %s and password = %s""",(username, password))

        #conn.commit()
        account = c.fetchone()
        
         
        if account: 
            #session['loggedin'] = True 
            #session['username'] = account['username'] 
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg) 
        else: 
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg) 
'''
@app.route('/') 
@app.route('/home', methods =['GET', 'POST'])
#@app.route('/home', methods =['GET', 'POST']) 
def home(): 
    #msg=''
    return render_template('home.html')

@app.route('/portfolio') 
def portfolio(): 
    #msg=''
    return render_template('portfolio.html')

@app.route('/resume') 
def resume(): 
    #msg=''
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)
