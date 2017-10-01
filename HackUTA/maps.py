
import os
import re
import json

from datetime import datetime

import googlemaps

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

#PROD
@app.route('/sms', methods=['GET','POST'])
def maps():
	number = request.form['From']
	message_body = request.form['Body']

	query_extractor = r"From (.*)To (.*)"

	matches = re.findall(query_extractor, message_body, re.MULTILINE | re.IGNORECASE)

	origin = matches[0][0]
	destination = matches[0][1]
	via = "driving"
	print("Origin is {} & destination is {} & via is {}".format(origin, destination, via))
	#TODO env variable
	maps_api_key = "AIzaSyCEMNKObdTlNK8zdDc2kalZ8y3bRpJo5A0"
	# res = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key={}".format(maps_api_key)
	gmaps = googlemaps.Client(key = maps_api_key)

	time_to_leave = datetime.now()
	directions = gmaps.directions(origin = origin, destination = destination, mode = via, departure_time = time_to_leave)

	html_tags_remover = re.compile('<.*?>')

	html_steps = directions[0]["legs"][0]["steps"]
	steps = []
	for step in html_steps:
		steps.append(re.sub(html_tags_remover, '', step["html_instructions"]))

	reply = str("""
				-{}
				""".format("\n-".join(steps)))

	resp = MessagingResponse()
	resp.message(reply)

	return str(resp)


if __name__ == '__main__':
	app.run(debug=True)

