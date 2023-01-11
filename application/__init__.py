
from flask import Flask
from application import routes
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy
from application.models import init_database

db = SQLAlchemy


def create_app():
    app = Flask(__name__)    
    config = dotenv_values()
    
    app.config.update(config)
    
    routes.init_routes(app)
    
    init_database(app)

    return app