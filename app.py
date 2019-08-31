import os
from test import predict
from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
app = Flask(__name__)


@app.route('/')
def render_html():
	return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file'] 
		filename = secure_filename(f.filename) 
		f.save(filename)
		result = predict(filename)
		filename = f.filename
		return render_template('index.html', result=result, filename=filename)

@app.route('/api', methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file'] 
		filename = secure_filename(f.filename) 
		f.save(filename)
		result = predict(filename)
		filename = f.filename
		return jsonify(result=result, filename=filename)		
		
if __name__ == '__main__':
	app.run(debug = True)