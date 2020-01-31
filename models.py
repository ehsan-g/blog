from datetime import datetime
import sqlalchemy as sa
from sqlalchemy_continuum import make_versioned
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, object_session
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
    lastname = sa.Column(sa.String, nullable=False)
    email = sa.Column(EmailType, nullable=False, unique=True)
    role = sa.Column(sa.String, default='Nakama')
    password = sa.Column(PasswordType(schemes=['pbkdf2_sha512', 'md5_crypt'], deprecated=['md5_crypt']))
    create_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    edit_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    posts = sa.orm.relationship("Post", back_populates="user", lazy=True)

    def add_post(self, aut_fav, duration, uptittle, tittle, mainp,
                 mainimg, mainalt, tittle2, secondp, video,
                 tittle3, subtittle, thirdp, hashtags,
                 album, albumtittle, albump,
                 albumimgalt, albumimgtxt
                 ):

        p = Post( aut_fav=aut_fav, duration=duration, uptittle=uptittle, tittle=tittle, mainp=mainp,
                  mainimg=mainimg, mainalt=mainalt, tittle2=tittle2, secondp=secondp, video=video,
                  tittle3=tittle3, subtittle=subtittle, thirdp=thirdp, hashtags=hashtags,
                  album=album, albumtittle=albumtittle, albump=albump,
                  albumimgalt=albumimgalt, albumimgtxt=albumimgtxt, user=self)


        return p


class PostCategory(db.Model):
    __tablename__ = "post_category"
    # id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)  #any other column cause null problem
    cat_id = sa.Column(sa.Integer, sa.ForeignKey("categories.id"), nullable=True, primary_key=True)
    post_id = sa.Column(sa.Integer, sa.ForeignKey("posts.id"), nullable=True, primary_key=True)


class Post(db.Model):
    __versioned__ = {}
    __tablename__ = "posts"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    aut_fav = sa.Column(sa.String, nullable=False)
    uptittle = sa.Column(sa.String, nullable=False)
    tittle = sa.Column(sa.String, nullable=False)
    mainp = sa.Column(sa.String, nullable=False)
    mainimg = sa.Column(sa.LargeBinary, nullable=False)
    mainalt = sa.Column(sa.String)
    tittle2 = sa.Column(sa.String)
    secondp = sa.Column(sa.String)
    video = sa.Column(sa.String)
    tittle3 = sa.Column(sa.String)
    subtittle = sa.Column(sa.String)
    thirdp = sa.Column(sa.String)
    hashtags = sa.Column(sa.ARRAY(sa.String))
    albumtittle = sa.Column(sa.String)
    album = sa.Column(sa.ARRAY(sa.LargeBinary))
    albump = sa.Column(sa.String)
    albumimgtxt = sa.Column(sa.ARRAY(sa.String))
    albumimgalt = sa.Column(sa.ARRAY(sa.String))
    published = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    edit_date = sa.Column(sa.DateTime)
    duration = sa.Column(sa.Integer, nullable=False)
    author_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=True)
    # foreign_keys could be empty if one foriegn key existed, we set uselist to Flase whenevever the relation is one
    user = sa.orm.relationship("User", back_populates="posts", lazy=True, foreign_keys=author_id, uselist=False)
    categories = sa.orm.relationship("Category", back_populates="posts", lazy=True, secondary='post_category')

    def add_cats(self, cats):
        print(f"this one {cats}")
        for cat in cats:
            self.categories.append(cat)

        print('bye')
        return cats


class Category(db.Model):
    __versioned__ = {}
    __tablename__ = "categories"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    posts = sa.orm.relationship("Post", back_populates="categories", lazy=True, secondary='post_category')

    #  check out class method, instance method and static method
    @classmethod
    def create_cat(cls, name):
        newcat = cls(name=name)
        return newcat


# after you have defined all your models, call configure_mappers:
sa.orm.configure_mappers()
