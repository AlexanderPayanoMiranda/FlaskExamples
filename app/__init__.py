from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    SQLAlchemy(app)

    return app
