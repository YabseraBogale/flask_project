import pandas as pd
from time import sleep
from database import Software
import json
from flask import Flask,render_template,url_for
list_of_stack=["mysql","go","python","c++","javascript",
				"js","sql","nodejs","react","vue","php",
				"c#",".net","django","flask","reactjs",
				"larvel","postgres","dart","flutter",
				"durple","java","spring","spring boot",
				"boot","css","bootstrap","tailwind","html"
				"html5","saas","node"]


table=Software()

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


if __name__=="__main__":
	app.run(debug=True)
