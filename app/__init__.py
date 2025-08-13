from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    # Import models so they are registered with SQLAlchemy
    from app.models.user_model import User
    from app.models.Applications_model import Application
    # from app.models.job import Job
    # from app.models.application import Application

    # Create tables without using migrations
    with app.app_context():
        db.create_all()

    # Optionally register blueprints
    # from app.routes.auth_routes import auth_bp
    # app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
