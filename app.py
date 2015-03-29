from flask import Flask, render_template, request, redirect, jsonify
import requests, json

app = Flask(__name__)

@app.route('/test')
def test():
	return 'test'

@app.route('/')
def home():
	return render_template('index.html')



@app.route('/requests', methods=['GET'])
def bandsprice():
	print "here"
	r = requests.get("http://perelste.in:8001/api/bands/id/72")
	r = jsonify(results = r.json())
	return r
	

if __name__ == '__main__':
    app.run(debug=True)

		