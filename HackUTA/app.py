
from flask import Flask, request, redirect

from twilio import twiml


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    resp = twiml.Response()

    resp.message("Hello World!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug = True)
    pass


