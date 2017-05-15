"""
Simple Yelp with Python and Flask
"""

from flask import Flask, session, redirect, url_for, escape, request, render_template, abort
import sqlite3

# conn = sqlite3.connect('database.db')
# print "opened db success!"
#
# conn.execute('CREATE TABLE students (name TEST, addr TEXT, city TEST, pint TEST)')
# print "table good"
# conn.close()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template("list.html", rows = rows)

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin - request.form['pin']

            with sql.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin)\
                    VALUES(?, ?, ?, ?)",(nm,addr,city,pin))

                con.commit()
                msg = "successfully added!"
        except:
            con.rollback()
            msg = "error in insert"
        finally:
            return render_template('result.html', msg = msg)
            con.close()

@app.route('/enternew')
def new_user():
    return render_template('user.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))
@app.route('/success')
def success():
    return 'logged in successfully'

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

# @app.route('/setcookie', methods=['POST', 'GET'])
# def setcookie():
#     if request.method == 'POST':
#         user = request.form['nm']
#
#     resp = make_response(render_template('readcookie.html'))
#     resp.set_cookie('userID', user)
#
#     return resp
#
# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)