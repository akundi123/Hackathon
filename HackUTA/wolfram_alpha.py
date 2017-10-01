
import os
import re
import json
import requests
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


#PROD
@app.route('/sms', methods=['GET','POST'])
def wolfram():
	number = request.form['From']
	msg = request.form['Body']
	#EX: https://api.wolframalpha.com/v1/result?i=What+is+the+stock+price+of+Twitter%3F&appid=DEMO
	#TODO env variable
	appid = "KLEJ7L-X4Y9P4KLV5"
	
	wolfram_url = "http://api.wolframalpha.com/v1/result"
	response = requests.get(wolfram_url, params = {"appid" : appid, "i" : msg}).content.decode("utf-8")
	
	print(response)
	out = MessagingResponse()
	out.message(response)
	return str(out)

if __name__ == '__main__':
	app.run(debug=True)

