from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    say_id = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    edit_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)




class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    passage = db.Column(db.String, nullable=False)
    published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)
    postlike = db.Column(db.Integer, nullable=False)



class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


