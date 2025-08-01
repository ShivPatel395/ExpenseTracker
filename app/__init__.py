#Sets up your Flask app and brings everything together.
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('config.Config')

    # Import and register routes
    from .routes import main
    app.register_blueprint(main)

    return app
