from flask import Flask, render_template, url_for
from Main import Commit

app = Flask(__name__)
commit = Commit()


@app.route("/")
def index():
    ok = commit.onlyGitCommitAll()
    return render_template("github.html", ok=ok)


if __name__ == "__main__":
    app.run(debug=True)
