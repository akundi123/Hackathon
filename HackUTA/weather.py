
import os
import re
import json

from datetime import datetime

import pydarksky
import googlemaps

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route('/sms', methods=['GET','POST'])
def weather():
	number = request.form['From']
	message_body = request.form['Body']
	
	query_extractor = r"From (.*)\nTo (.*)\nVia (.*)\nLeave (.*)?"

	matches = re.findall(query_extractor, message_body, re.MULTILINE | re.IGNORECASE)

	darksky_api_key = "d56b7934d5a491dcad4f0d22ef7e839b"

	darksky = pydarksky.DarkSky(darksky_api_key)
	
	location = get_location()
	darksky.latitude = location["lat"]
	darksky.longitude = location["lng"]
	
	weather = darksky.weather(latitude = location["lat"], longitude = location["lng"])

	reply = weather
	

	resp = MessagingResponse()
	resp.message(reply)
	
	return str(resp)


def get_location():
	maps_api_key = "AIzaSyCEMNKObdTlNK8zdDc2kalZ8y3bRpJo5A0"
	gmaps = googlemaps.Client(key = maps_api_key)
	
	location_geocode = gmaps.geocode(origin)
	
	return location_geocode[0]["geometry"]["location"]

if __name__ == '__main__':
	app.run(debug=True)


