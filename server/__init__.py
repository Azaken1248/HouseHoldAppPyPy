# server/__init__.py
from flask import Flask
from server.config import Config
from server.models import db, init_db
from server.routes import admin_routes, user_routes, professional_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(admin_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(professional_routes)

    init_db(app)
    return app
