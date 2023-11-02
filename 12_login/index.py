from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
	data = ((1,'admin','admin'),(2,'abc','abc'),(3,'xyz','xyz'))


	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		for i in data:
			if username == i[1] and password == i[2]:
				return redirect(url_for('home'))

		
		# else:
		return redirect(url_for('login'))
		# return f"post req here {username} {password}"

	else:	
		return render_template('login.html')


if __name__ == '__main__':
	app.run(debug = True)