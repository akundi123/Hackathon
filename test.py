import os
import re
import json
import requests
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
"""
@app.route('/sms', methods=['GET','POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    print("Got this far")
    query_extractor = r"^(!?[^\s]+)?\s{1}(.*)"
    print(query_extractor)
    matches = re.findall(query_extractor, message_body, re.MULTILINE)
    
    bang = matches[0][0]
    query = matches[0][1]

    print("Bang is {} & query is {}".format(bang, query))

    resp = MessagingResponse()

    resp.message("Bang is {} & query is {}".format(bang, query))
    #resp.message("THANKS FOR THE INFO!!")
    return str(resp)

"""
@app.route('/sms', methods=['GET','POST'])
def wolfram():
    #Interact with simple api from wolframalpha
    number = request.form['From']
    msg = request.form['Body']
    #EX: https://api.wolframalpha.com/v1/result?i=What+is+the+stock+price+of+Twitter%3F&appid=DEMO
    #TODO env variable
    appid = "KLEJ7L-X4Y9P4KLV5"
    r = "http://api.wolframalpha.com/v1/result?appid={}&i={}%3f".format(appid,msg.replace(' ','+'))
    response = requests.get(r).content.decode('utf-8')

    print(response)
    out = MessagingResponse()
    out.message(response)
    return str(out)

if __name__ == '__main__':
    app.run(debug=True)


