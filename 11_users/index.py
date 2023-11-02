from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
	return 'home'

@app.route('/users')
def users():
	users = ['ab','cd','de']
	return render_template('user.html',users=users)

@app.route('/places')
def places():
	data = ['https://upload.wikimedia.org/wikipedia/commons/6/61/Pokhara-valley-nepal.jpg',
	'https://uploads-ssl.webflow.com/576fd5a8f192527e50a4b95c/5c337a21121342bd3505299a_top%20things%20to%20do%20in%20Chitwan.jpg',
	'https://images.thrillophilia.com/image/upload/s--XmU0CINq--/c_fill,g_auto,h_600,q_auto,w_975/f_auto,fl_strip_profile/v1/images/photos/000/146/987/original/1595503023_shutterstock_266064224.jpg.jpg',
	'https://cdn.britannica.com/36/154236-050-8127D19C/Durbar-Square-Lalitpur-Nepal.jpg',
	'https://www.landnepal.com/wp-content/uploads/2021/08/bhaktapur.jpeg']

	return render_template('place.html',places=data)


if __name__ == '__main__':
	app.run(debug = True)