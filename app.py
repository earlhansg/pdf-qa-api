import os
from flask import Flask
from db import db
from routes.todo_routes import todo_bp
from routes.chat_routes import chat_bp
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database
    db.init_app(app)

    # Register blueprints (routes)
    app.register_blueprint(todo_bp, url_prefix="/todos")
    app.register_blueprint(chat_bp, url_prefix="/chat")

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
