from flask import Flask
from config import Config
from models import db
from routes import all_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    for bp in all_blueprints:  # now we loop over blueprint objects
        app.register_blueprint(bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)