import os
import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def sms():
	wolfram()

def default():
	number = request.form['From']
	msg = request.form['Body']

	if msg.startswith('directions'):
		maps()
	elif msg.startswith('weather') or msg.startswith('temperature'):
		weather()
	else:
		wolfram()

@app.route('/', methods=['GET', 'POST'])
def static():
	#TODO static web page
	pass


def wolfram():
	msg = request.form['Body']
	# EX: https://api.wolframalpha.com/v1/result?i=What+is+the+stock+price+of+Twitter%3F&appid=DEMO
	# TODO env variable
	appid = "KLEJ7L-X4Y9P4KLV5" #

	wolfram_url = "http://api.wolframalpha.com/v1/result"
	response = requests.get(wolfram_url, params={"appid": appid, "i": msg}).content.decode("utf-8")

	print(response)
	out = MessagingResponse()
	out.message(response)
	return str(out)


def maps():
	#TODO temporary
	wolfram()

def weather():
	#TODO temporary
	wolfram()


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

