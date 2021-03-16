from flask import Flask
from website.config import Config


app = Flask(__name__, static_folder='static')
app.config.from_object(Config)

from website import route