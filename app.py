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
	#Demo
	r = requests.get("http://perelste.in:8001/api/bands/id/72")
	mr = jsonify(results = r.json())
	r = r.json()


	print r[0]['country']

	merch = False
	for i in range(len(r[0]['related_links'])):
		print r[0]['related_links'][0]['category']
		if(r[0]['related_links'][i]['category'] == "Official_Merchandise"):
			merch = True
			break

	if(merch):
		allMerch = requests.get(r[0]['related_links'][i]['url'])
		allMerch = allMerch.text

		dollas = allMerch.find("$")

		if(dollas != -1):
			price = 0
			if(allMerch[dollas + 1].isdigit()):
				price = price + (10 * int(allMerch[dollas + 1]))
				print price
			if(allMerch[dollas + 2].isdigit()):
				price = price + int(allMerch[dollas + 2])
				print price

	theCost = json.dumps({"price": price}, sort_keys=True)

	return theCost

	#Experimental









	

if __name__ == '__main__':
    app.run(debug=True)

		