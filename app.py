from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__, static_folder='static')

@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')
connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS PARTICIPANTS (date TEXT, mood TEXT, headache TEXT, period TEXT, other TEXT)')
@app.route('/join', methods=['GET', 'POST'])
def join():
	if request.method == 'POST':
		date = request.form['date']
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
@app.route('/participants')
def participants():
	connect = sqlite3.connect('database.db')
	cursor = connect.cursor()
	cursor.execute('SELECT * FROM PARTICIPANTS')
	data = cursor.fetchall()
	return render_template("participants.html", data=data)
if __name__ == '__main__':
	app.run(debug=False)
