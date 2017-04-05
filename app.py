from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class players(db.Model):
	__tablename__ = 'players'
	id = db.Column('player_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	age = db.Column(db.String(5))
	addr = db.Column(db.String(200)) 
	job = db.Column(db.String(10))

	def __init__(self, name, age, addr, job):
		self.name = name
		self.age = age
		self.addr = addr
		self.job = job

	
The_answers = [1364,463,16,0,160243,45478,202,41181,41719,2380]
The_Qestions = ['Berapakah jumlah pertambahan motor per-hari pada tahun 2014 di DKI Jakarta ?',
'Berapakah jumlah pertambahan mobil per-hari pada tahun 2014 di DKI Jakarta ?',
'Berapakah jumlah kematian penduduk laki-laki karena bunuh diri di daerah DKI Jakarta pada tahun 2015 ?',
'Berapakah jumlah kematian penduduk perempuan karena bunuh diri di daerah DKI Jakarta pada tahun 2015 ?',
'berapakah jumlah penduduk migrasi ke DKI Jakarta dari Luar DKI Jakarta pada tahun 2015 ?',
'Berapakah jumlah pendatang WNI Laki-laki dari luar wilayah DKI Jakarta pada tahun 2015 ?',
'Berapakah jumlah penduduk yang menganut aliran sesat di Daerah DKI Jakarta pada tahun 2014 ?',
'Berapakah jumlah penduduk DKI Jakarta yang berusia lebih dari 75 tahun berjenis kelamin laki-laki pada tahun 2014 ?',
'Berapakah jumlah penduduk DKI Jakarta yang pindah ke Luar wilayah DKI Jakarta pada tahun 2013 ?',
'Berapkah jumlah penduduk yang meninggal dari usia 0-4 tahun di daerah DKI Jakarta pada tahun 2014?']
player_answer = []
		
@app.route('/Dashboard')
def show_all():
	player_answer[:]=[]
	return render_template('show_all.html', players = players.query.all() )

@app.route('/', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		if not request.form['name'] or not request.form['age'] or not request.form['addr'] or not request.form['job']:
			flash('Please enter all the fields', 'error')
		else:
			player = players(request.form['name'], request.form['age'], request.form['addr'], request.form['job'])
         
			db.session.add(player)
			db.session.commit()
			flash('Record was successfully added')
			return redirect(url_for('Quiz1'))
	return render_template('login.html')
	
@app.route('/number1',methods = ['POST','GET'])
def Quiz1():
	i = 1
	m = 0
	if request.method == 'POST':
		if not request.form['answer']:
			flash('Silahkan masukan jawaban anda', 'error')
		else:
			answer = request.form['answer']
			player_answer.append(answer)
			return redirect(url_for('Quiz2'))
	return render_template('quiz.html',j = i,x=The_Qestions,n=m)

@app.route('/number2',methods = ['POST','GET'])
def Quiz2():
	i = 2
	m = 1
	if request.method == 'POST':
		if not request.form['answer']:
			flash('Silahkan masukan jawaban anda', 'error')
		else:
			answer = request.form['answer']
			player_answer.append(answer)
			return redirect(url_for('Quiz3'))
	return render_template('quiz.html',j = i,x=The_Qestions,n=m)

@app.route('/number3',methods=['POST','GET'])
def Quiz3():
	i = 3
	m = 2
	if request.method == 'POST':
		if not request.form['answer']:
			flash('Silahkan masukan jawaban anda', 'error')
		else:
			answer = request.form['answer']
			player_answer.append(answer)
			return redirect(url_for('Quiz4'))
	return render_template('quiz.html',j = i,x=The_Qestions,n=m)

@app.route('/number4',methods=['POST','GET'])
def Quiz4():
	i = 4
	m = 3
	if request.method == 'POST':
		if not request.form['answer']:
			flash('Silahkan masukan jawaban anda', 'error')
		else:
			answer = request.form['answer']
			player_answer.append(answer)
			return redirect(url_for('Quiz5'))
	return render_template('quiz.html',j = i,x=The_Qestions,n=m)

@app.route('/number5',methods=['POST','GET'])
def Quiz5():
	i = 5
	m = 4
	if request.method == 'POST':
		if not request.form['answer']:
			flash('Silahkan masukan jawaban anda', 'error')
		else:
			answer = request.form['answer']
			player_answer.append(answer)
			return redirect(url_for('Quiz6'))
	return render_template('quiz.html',j = i,x=The_Qestions,n=m)

@app.route('/number6',methods=['POST','GET'])
def Quiz6():
	i = 6
	m = 5
	if request.method == 'POST':
		if not request.form['answer']:
			flash('Silahkan masukan jawaban anda', 'error')
		else:
			answer = request.form['answer']
			player_answer.append(answer)
			return redirect(url_for('Quiz7'))
	return render_template('quiz.html',j = i,x=The_Qestions,n=m)

@app.route('/number7',methods=['POST','GET'])
def Quiz7():
	i = 7
	m = 6
	if request.method == 'POST':
		if not request.form['answer']:
			flash('Silahkan masukan jawaban anda', 'error')
		else:
			answer = request.form['answer']
			player_answer.append(answer)
			return redirect(url_for('Quiz8'))
	return render_template('quiz.html',j = i,x=The_Qestions,n=m)

@app.route('/number8',methods=['POST','GET'])
def Quiz8():
	i = 8
	m = 7
	if request.method == 'POST':
		if not request.form['answer']:
			flash('Silahkan masukan jawaban anda', 'error')
		else:
			answer = request.form['answer']
			player_answer.append(answer)
			return redirect(url_for('Quiz9'))
	return render_template('quiz.html',j = i,x=The_Qestions,n=m)

@app.route('/number9',methods=['POST','GET'])
def Quiz9():
	i = 9
	m = 8
	if request.method == 'POST':
		if not request.form['answer']:
			flash('Silahkan masukan jawaban anda', 'error')
		else:
			answer = request.form['answer']
			player_answer.append(answer)
			return redirect(url_for('Quiz10'))
	return render_template('quiz.html',j = i,x=The_Qestions,n=m)

@app.route('/number10',methods=['POST','GET'])
def Quiz10():
	i = 10
	m = 9
	if request.method == 'POST':
		if not request.form['answer']:
			flash('Silahkan masukan jawaban anda', 'error')
		else:
			answer = request.form['answer']
			player_answer.append(answer)
			return redirect(url_for('jawaban'))
	return render_template('quiz.html',j = i,x=The_Qestions,n=m)

@app.route('/jawaban',methods=['POST','GET'])
def jawaban():
	if request.method == 'POST':
		return redirect(url_for('show_all'))
	return render_template('kunci_jawaban.html',x=The_Qestions,y=The_answers,z=player_answer)
	
		
		
if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)