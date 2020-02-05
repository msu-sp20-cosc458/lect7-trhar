import flask
import os


app = flask.Flask(__name__)
@app.route('/') 

def index(): 
    print("This is a debug statement")
    return "<b>Hello, Trustin!</b>"

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )