from flask import Flask,url_for,render_template

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return "login page"

if __name__=="__main__":
	app.run(debug=True)
