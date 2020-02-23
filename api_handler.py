import flask 
from flask import Flask, redirect, request
import requests


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>EC500 HW#4t</h1><p>by Ruby Zaveri</p><p>Making a twitter video</p>"

@app.route('/tweets/', methods=['GET'])
def twitter_username():

    # default user name if none provided
    name = "NatGeo"

    if 'username' in request.args:
        name = request.args['username']
 
    call = {
        "user_name": name,
        "id": id,
        "status": "queued"
    }
    ident = str(id)
    id += 1

    # adds to dict of all process requests
    processes[ident] = call

    # adds to worker queue to be completed
    q.put(call)

    q.join()

    return send_completed_video(ident)
