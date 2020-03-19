from flask import Flask,request
from flask import json
from json import JSONEncoder
from urlparse import parse_qs

#http://0.0.0.0:5000/destinations?arg1=hello&arg2=world
#http://82.251.99.85:80/destinations?arg1=hello&arg2=world

app = Flask(__name__)
@app.route('/conn_info', methods=['GET'])
def connInf():
	
	return json.dumps(request.args)
	

@app.route('/devices', methods=['GET'])
def dev():
	
	return json.dumps(request.args)

@app.route('/id_device', methods=['GET'])
def iddev():
	
	return json.dumps(request.args)
	
	
if __name__=='__main__':
	app.run(debug=True, host= '0.0.0.0')
