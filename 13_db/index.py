from flask import Flask 
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

# movies 

@app.route('/')
def movies():
	cursor.execute("select * from movies")
	result = cursor.fetchall()
	return result

if __name__ =="__main__":
	app.run(debug=True)