from flask import Flask
import os

app = Flask(__name__, template_folder="templates")

app.config["SECRET_KEY"] = os.environ["FLASK_SECRET_KEY"]

from playground import routes
