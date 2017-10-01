
import os
import re
import json

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route('/sms', methods=['GET','POST'])
def duckduckgo():
	number = request.form['From']
	message_body = request.form['Body']
	
	query_extractor = r"^(!?[^\s]+)?\s{1}(.*)"

	matches = re.findall(query_extractor, message_body, re.MULTILINE)

	bang = matches[0][0]
	query = matches[0][1]
	print("Bang is {} & query is {}".format(bang, query))
	
	duckduckgo_url = "http://api.duckduckgo.com/"
	duckduckgo_params = {
        "q": message_body, # query,
        "format": "json",
        "pretty": "1",
        "no_redirect": "1",
        "no_html": "1",
        "skip_disambig": "1",
        }

	search_result = requests.get(duckduckgo_url, params = duckduckgo_params).content.decode("utf-8")
	duckduckgo_json = json.loads(search_result)
	
	
	
	print(reply)

	resp = MessagingResponse()
	# resp.message('Hello {}, you said: {}'.format(number, message_body))
	# resp.message("Bang is {} & query is {}".format(bang, query))
	resp.message(reply)
	# resp.message("THANKS FOR THE INFO!!")
	return str(resp)


if __name__ == '__main__':
	app.run(debug=True)


