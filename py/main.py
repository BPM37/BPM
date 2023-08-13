# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app)
app.config["CORS_HEADERS"] = 'Content-Type'


import api
app.register_blueprint(api.bp)