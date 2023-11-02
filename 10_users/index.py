from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/users')
def users():
	users = ["ab","cd","de"]

	return render_template('user.html',users=users)


if __name__ == '__main__':
	app.run()