
from flask import Flask
from application import routes
from dotenv import dotenv_values
from application.models import init_database
from flask_bootstrap import Bootstrap
from application.authentication import create_jwt



def create_app():
    app = Flask(__name__)    
    config = dotenv_values()
    
    app.config.update(config)
    
    routes.init_routes(app)
    
    Bootstrap(app)
    
    init_database(app)
    
    create_jwt(app)

    return app