import os
import re
import json
import requests
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/sms', methods=['GET', 'POST'])
def weather():
	msg = request.form['Body']
	#queryextractor =
	loc = msg.split()[-1]
	print(loc)

if __name__ == '__main__':
	app.run(debug=True)



