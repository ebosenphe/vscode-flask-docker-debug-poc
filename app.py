from flask import Flask
from datetime import datetime
import re
from debugger import initialize_flask_server_debugger_if_needed


initialize_flask_server_debugger_if_needed()

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/bye")
def bye():
    return "Goodbyw"

@app.route("/hello/<name>")
def hello_there(name):
    try:
        now = datetime.now()
        formatted_now = now.strftime("%A, %d %B, %Y at %X")

        # Filter the name argument to letters only using regular expressions. URL arguments
        # can contain arbitrary text, so we restrict to safe characters only.
        match_object = re.match("[a-zA-Z]+", name)

        if match_object:
            clean_name = match_object.group(0)
        else:
            clean_name = "My Friend!"

        # raise ValueError('Represents a hidden bug, do not catch this')

        # try:
            
        #     raise Exception('This is the exception you expect to handle')
        # except Exception as error:
        #     print('Caught this error: ' + repr(error))

        content = "Yo there, " + clean_name + "! It's " + formatted_now
        return content
    except:
        print ('No idea')
