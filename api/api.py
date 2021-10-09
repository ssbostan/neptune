from flask import Flask, Blueprint
from flask.cli import AppGroup as AppCLIGroup
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from api.config import Config

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()

app_cli = AppCLIGroup("app", help="Application commands.") # Create "flask app" cli command.

apiv1_bp = Blueprint("apiv1", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

from api import command
from api import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)
    app.cli.add_command(app_cli) # Adding "flask app" to the application.
    app.register_blueprint(apiv1_bp) # Register APIv1 blueprint to application.
    return app
