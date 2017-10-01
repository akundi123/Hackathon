
import os
import re

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


import duckduckgo


app = Flask(__name__)


@app.route('/sms', methods=['GET','POST'])
def sms():
	number = request.form['From']
	message_body = request.form['Body']
	
	query_extractor = r"^(!?[^\s]+)?\s{1}(.*)"

	matches = re.findall(query_extractor, message_body, re.MULTILINE)

	bang = matches[0][0]
	query = matches[0][1]
	print("Bang is {} & query is {}".format(bang, query))

	reply = ""

	resp = MessagingResponse()
	# resp.message('Hello {}, you said: {}'.format(number, message_body))
	resp.message("Bang is {} & query is {}".format(bang, query))
	# resp.message("THANKS FOR THE INFO!!")
	return str(resp)


if __name__ == '__main__':
	app.run(debug=True)


