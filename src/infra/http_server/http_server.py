from flask import Flask
from src.domain.routes.notion_routes import notion_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(notion_bp, url_prefix='/api/v1')
    return app
