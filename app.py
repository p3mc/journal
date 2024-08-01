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

# Test

""" def index():
        return render_template('index.html')
connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS FOOD (breakfast TEXT, lunch TEXT, dinner TEXT, snacks TEXT)')
@app.route('/join', methods=['GET', 'POST'])
def join():
        if request.method == 'POST':
                breakfast = request.form['breakfast']
                lunch = request.form['lunch']
                dinner = request.form['dinnner']
                snacks = request.form['snacks']

                with sqlite3.connect("database.db") as users:
                        cursor = users.cursor()
                        cursor.execute('INSERT INTO FOOD(breakfast,lunch,dinner,snacks) VALUES (?,?,?,?,?)', (breakfast,lunch,dinner,snacks))
                        users.commit()
                return render_template("index.html")
        else:
                return render_template('join.html') """

# End test

@app.route('/participants')
def participants():
	connect = sqlite3.connect('database.db')
	cursor = connect.cursor()
	cursor.execute('SELECT * FROM PARTICIPANTS')
	data = cursor.fetchall()
	return render_template("participants.html", data=data)
if __name__ == '__main__':
	app.run(debug=False)

# Test

""" def meals():
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM FOOD')
        meal = cursor.fetchall()
        return render_template("participants.html", meal=meal)
if __name__ == '__main__':
        app.run(debug=False) """



# Ends test 
