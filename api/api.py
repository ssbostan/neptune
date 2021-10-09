from flask import Flask

from api.config import Config

from api import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app
