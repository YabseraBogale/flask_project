from flask import Flask,url_for,render_template
from main import Commit
app=Flask(__name__)


@app.route('/')
def index():
	git=Commit()
	ok=git.onlyGitCommit()
	return render_template('github.html',ok=ok)



if __name__=="__main__":
	app.run(debug=True)
