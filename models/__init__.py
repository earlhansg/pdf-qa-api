from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import all models so they are registered with SQLAlchemy
from .knowledge import Knowledge

__all__ = ["db", "Knowledge"]
