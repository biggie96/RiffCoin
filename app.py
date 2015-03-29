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
	r = requests.get("http://perelste.in:8001/api/bands/id/72")
	mr = jsonify(results = r.json())
	r = r.json()


	print r[0]['country']

	for i in range(len(r[0]['related_links'])):
		print r[0]['related_links'][0]['category']
		if(r[0]['related_links'][i]['category'] == "Official_Merchandise"):
			print "yes!"
			break

	allMerch = requests.get(r[0]['related_links'][i]['url'])
	allMerch = allMerch.text
	print allMerch







	return mr


	

if __name__ == '__main__':
    app.run(debug=True)

		