from datetime import datetime
import sqlalchemy as sa
from sqlalchemy_continuum import make_versioned
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker


"""  
    All tables are defined here and sqlalchemy_continuum will be used 
    for further versioning.
    """

db = SQLAlchemy()

make_versioned()

class User(db.Model):
    __versioned__ = {}  # In order to make your models versioned
    __tablename__ = "users"
    id = sa.Column(sa.Integer,  primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String(120), index=True, unique=True)
    password = sa.Column(sa.String(128), nullable=False)
    create_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    edit_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)


class Post(db.Model):
    __versioned__ = {}  # In order to make your models versioned
    __tablename__ = "posts"
    id = sa.Column(sa.Integer, primary_key=True)
    author = sa.Column(sa.String, nullable=False)
    title = sa.Column(sa.String, nullable=False)
    passage = sa.Column(sa.String, nullable=False)
    published = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    duration = sa.Column(sa.Integer, nullable=False)
    postlike = sa.Column(sa.Integer, nullable=False)



class Comment(db.Model):
    __versioned__ = {}  # In order to make your models versioned
    __tablename__ = "comments"
    id = sa.Column(sa.Integer, primary_key=True)
    content = sa.Column(sa.String, nullable=False)
    author = sa.Column(sa.String, nullable=False)
    create_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)



# after you have defined all your models, call configure_mappers:
sa.orm.configure_mappers()