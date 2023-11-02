from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html',marks=20)

@app.route('/about')
def about():
	return 'ABOUT PAGE asdasd'

if __name__ == '__main__':
    app.run(debug = True)
