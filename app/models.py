# Add any model classes for Flask-SQLAlchemy here
from flask import Flask
from . import db
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime






class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id, title, description, poster, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at