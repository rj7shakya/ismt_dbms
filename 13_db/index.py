from flask import Flask,render_template,request,redirect,url_for 
app = Flask(__name__)

import psycopg2

con = psycopg2.connect(
	database='ismt', # created database
	user='postgres', #  install username
	password='inspiron', # install password
	host='localhost', 
	port='5432'
)
cursor = con.cursor()

#add movie
@app.route('/add',methods=['GET','POST'])
def add_movie():
	if request.method == 'POST':
		id = request.form['id']
		name = request.form['name']
		rating = request.form['rating']

		i_query = f""" insert into movies values 
							({id},'{name}',{rating}) 
							"""
		cursor.execute(i_query)
		con.commit()
		return redirect(url_for('movies'))

	return render_template('add.html')


# movies display
@app.route('/')
def movies():
	cursor.execute("select * from movies")
	result = cursor.fetchall()
	return render_template('mv.html',result=result)

if __name__ =="__main__":
	app.run(debug=True)