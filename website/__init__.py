from flask import Flask
from website.config import Config


app = Flask(__name__)
app.config.from_object(Config)