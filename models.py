from datetime import datetime
import sqlalchemy as sa
from sqlalchemy_continuum import make_versioned
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session
from sqlalchemy_utils import EmailType
from sqlalchemy_utils import PasswordType, force_auto_coercion

force_auto_coercion()

"""
    All tables are defined here and sqlalchemy_continuum will be used 
    for further versioning.
    """

db = SQLAlchemy()
make_versioned()


class User(db.Model):
    __versioned__ = {}  # In order to make your models versioned
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    email = sa.Column(EmailType, nullable=False, unique=True)
    role = sa.Column(sa.String, default='Nakama')
    password = sa.Column(PasswordType(schemes=['pbkdf2_sha512', 'md5_crypt'], deprecated=['md5_crypt']))
    create_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    edit_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship("Post", backref="user", lazy=True)

    def add_post(self, aut_fav, uptitle, title, mainp, mainimg, title2, secondp, video, galtitle, galtext, galimg1,
                 galimgtxt1, galimg2, galimgtxt2, galimg3, galimgtxt3, galimg4, galimgtxt4, galimg5, galimgtxt5,
                 galimg6, galimgtxt6, tittle3, subtitle, thirdp, duration):
        p = Post(aut_fav=aut_fav, uptitle=uptitle, title=title, mainp=mainp, mainimg=mainimg,
                 title2=title2, secondp=secondp, video=video, galtitle=galtitle, galtext=galtext,
                 galimg1=galimg1, galimgtxt1=galimgtxt1, galimg2=galimg2, galimgtxt2=galimgtxt2,
                 galimg3=galimg3, galimgtxt3=galimgtxt3, galimg4=galimg4, galimgtxt4=galimgtxt4,
                 galimg5=galimg5, galimgtxt5=galimgtxt5, galimg6=galimg6, galimgtxt6=galimgtxt6,
                 tittle3=tittle3, subtitle=subtitle, thirdp=thirdp, duration=duration, author_id=self.id)
               
        return p


class Post(db.Model):
    __versioned__ = {}
    __tablename__ = "posts"
    id = sa.Column(sa.Integer, primary_key=True)
    aut_fav = sa.Column(sa.String, nullable=False)
    uptitle = sa.Column(sa.String, nullable=False)
    title = sa.Column(sa.String, nullable=False)
    mainp = sa.Column(sa.String, nullable=False)
    mainimg = sa.Column(sa.String)
    title2 = sa.Column(sa.String, nullable=False)
    secondp = sa.Column(sa.String, nullable=False)
    video = sa.Column(sa.String, nullable=False)
    galtitle = sa.Column(sa.String, nullable=False)
    galtext = sa.Column(sa.String, nullable=False)
    galimg1 = sa.Column(sa.String, nullable=False)
    galimgtxt1 = sa.Column(sa.String, nullable=False)
    galimg2 = sa.Column(sa.String)
    galimgtxt2 = sa.Column(sa.String)
    galimg3 = sa.Column(sa.String)
    galimgtxt3 = sa.Column(sa.String)
    galimg4 = sa.Column(sa.String)
    galimgtxt4 = sa.Column(sa.String)
    galimg5 = sa.Column(sa.String)
    galimgtxt5 = sa.Column(sa.String)
    galimg6 = sa.Column(sa.String)
    galimgtxt6 = sa.Column(sa.String)
    tittle3 = sa.Column(sa.String, nullable=False)
    subtitle = sa.Column(sa.String, nullable=False)
    thirdp = sa.Column(sa.String, nullable=False)
    published = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    duration = sa.Column(sa.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))



# after you have defined all your models, call configure_mappers:
sa.orm.configure_mappers()
