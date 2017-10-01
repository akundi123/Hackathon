import os
from flask import Flask, request

import maps
import wolfram_alpha
import weather

app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def sms():
	number = request.form['From']
	msg = request.form['Body']

	if msg.lower().startswith('from'):
		return maps.maps()
	elif msg.lower().startswith('weather'):
		return weather.weather()
		#return weather()
	else:
		return wolfram_alpha.wolfram()

#TODO temporary
def weather():
	wolfram_alpha.wolfram()


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

