from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
return 'OK', 200

@app.route('/webhookreq', methods=['POST', 'GET']) 
def webhookreq():
return "Yes, this is working." return 'OK', 200

@app.route('/cardsubmitted', methods=['POST']) 
def cardsubmitted():
return 'OK', 200

if __name__=='__main__': app.debug = True app.run(host= "0.0.0.0")
