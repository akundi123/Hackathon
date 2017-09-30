import os

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

#THIS WORKS
@app.route('/', methods=['GET','POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    #resp.message("THANKS FOR THE INFO!!")
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)


