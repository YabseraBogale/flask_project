import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/media/yabsera/New Volume/github/flask_project/upload/user_folder'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png','docx'}

app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload',methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('download_file', name=filename))
	return "falied"
if __name__=="__main__":
	app.run(debug=True)
