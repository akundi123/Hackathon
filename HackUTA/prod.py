import os
from flask import Flask, request

from HackUTA.maps import maps
from HackUTA.wolfram_alpha import wolfram

app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def sms():
	number = request.form['From']
	msg = request.form['Body']

	if msg.lower().startswith('from'):
		maps()
	elif msg.lower().startswith('weather') or msg.lower().startswith('temp'):
		weather()
	else:
		wolfram()

@app.route('/', methods=['GET', 'POST'])
def static():
	#TODO static web page
	pass

#TODO temporary
def weather():
	wolfram()


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

