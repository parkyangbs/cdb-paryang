from flask import Flask, request
from webexteamssdk import WebexTeamsAPI, Webhook

app = Flask(__name__)
api = WebexTeamsAPI(access_token="MjYwOGMxNzEtZTI4ZC00ZjYxLWI2MTAtMzNkOWExYTNmNzFlZTEzODZh NmMtYmEw_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f")

@app.route('/', methods=['POST', 'GET'])
def home():
return 'OK', 200

@app.route('/webhookreq', methods=['POST', 'GET']) 
def webhookreq():
   if request.method == 'POST': req = request.get_json()
   data_personId = req['data']['personId']

   #Loop prevention VERY IMPORTNAT!
   me = api.people.me()

   if data_personId == me.id:
       return 'OK', 200 else:
   if api.messages.create(roomId="Y2lzY29zcGFyazovL3VzL1JPT00vNzZmYzJkOTAtY2VkYi0 xMWViLThjNTQtYmZjODU2MWE4N2I2", text='Hello World!!!'):
       return "OK"
   elif request.method == 'GET':
   return "Yes, this is working." return 'OK', 200

@app.route('/cardsubmitted', methods=['POST']) 
def cardsubmitted():
return 'OK', 200

if __name__=='__main__': app.debug = True app.run(host= "0.0.0.0")
