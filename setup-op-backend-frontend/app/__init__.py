from flask import Flask
from .routes import app_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config') # Load config from config.py
    app.register_blueprint(app_routes)
    return app
