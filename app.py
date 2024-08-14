from flask import Flask, render_template, request
from datetime import date
import sqlite3
app = Flask(__name__, static_folder='static')

# if URL / or /home: 
@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')
connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS PARTICIPANTS (date TEXT, mood TEXT, headache TEXT, period TEXT, other TEXT)')
connect.execute('CREATE TABLE IF NOT EXISTS FOOD (date TEXT, breakfast TEXT, lunch TEXT, dinner TEXT, snacks TEXT)')
today = date.today()

#if URL /join:
@app.route('/join', methods=['GET', 'POST'])
def join():
	if request.method == 'POST':
		date = today #request.form['date']
		mood = request.form['mood']
		headache = request.form['headache']
		period = request.form['period']
		other = request.form['other']

		with sqlite3.connect("database.db") as users:
			cursor = users.cursor()
			cursor.execute('INSERT INTO PARTICIPANTS(date,mood,headache,period,other) VALUES (?,?,?,?,?)', (date, mood, headache, period, other))
			users.commit()
		return render_template("index.html")
	else:
		return render_template('join.html')

#if URL /food:
@app.route('/food', methods=['GET', 'POST'])
def food():
   if request.method == 'POST':
       date = today
       breakfast = request.form['breakfast']
       lunch = request.form['lunch']
       dinner = request.form['dinner']
       snacks = request.form['snacks']

       with sqlite3.connect("database.db") as users:
           cursor = users.cursor()
           cursor.execute('INSERT INTO FOOD(date,breakfast,lunch,dinner,snacks) VALUES (?,?,?,?,?)', (date,breakfast,lunch,dinner,snacks))
           users.commit()
       return render_template("index.html")
   else:
       return render_template('food.html')

#if URL /participants
@app.route('/participants')
def participants():
	connect = sqlite3.connect('database.db')
	cursor = connect.cursor()
	cursor.execute('SELECT * FROM PARTICIPANTS INNER JOIN FOOD on FOOD.date = PARTICIPANTS.date;') # lub ('SELECT * FROM PARTICIPANTS UNION SELECT * FROM FOOD;')
	data = cursor.fetchall()
	return render_template("participants.html", data=data)
if __name__ == '__main__':
	app.run(debug=False)
