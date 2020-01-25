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

    def add_post(self, aut_fav, uptittle, tittle, mainp, mainimg, tittle2, secondp, video, galtittle, galtext, galimg1,
                 galimgtxt1, galimg2, galimgtxt2, galimg3, galimgtxt3, galimg4, galimgtxt4, galimg5, galimgtxt5,
                 galimg6, galimgtxt6, tittle3, subtittle, thirdp, hashtags, duration):
        p = Post(aut_fav=aut_fav, uptittle=uptittle, tittle=tittle, mainp=mainp, mainimg=mainimg,
                 tittle2=tittle2, secondp=secondp, video=video, galtittle=galtittle, galtext=galtext,
                 galimg1=galimg1, galimgtxt1=galimgtxt1, galimg2=galimg2, galimgtxt2=galimgtxt2,
                 galimg3=galimg3, galimgtxt3=galimgtxt3, galimg4=galimg4, galimgtxt4=galimgtxt4,
                 galimg5=galimg5, galimgtxt5=galimgtxt5, galimg6=galimg6, galimgtxt6=galimgtxt6,
                 tittle3=tittle3, subtittle=subtittle, thirdp=thirdp, hashtags=hashtags, duration=duration, user=self)
                # instead of setting author_id=self.id we send the object to user

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
    aut_fav = sa.Column(sa.Boolean, nullable=False)
    uptittle = sa.Column(sa.String, nullable=False)
    tittle = sa.Column(sa.String, nullable=False)
    mainp = sa.Column(sa.String, nullable=False)
    mainimg = sa.Column(sa.String, nullable=False)
    tittle2 = sa.Column(sa.String, nullable=False)
    secondp = sa.Column(sa.String, nullable=False)
    video = sa.Column(sa.String)
    galtittle = sa.Column(sa.String)
    galtext = sa.Column(sa.String)
    galimg1 = sa.Column(sa.String)
    galimgtxt1 = sa.Column(sa.String)
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
    subtittle = sa.Column(sa.String, nullable=False)
    thirdp = sa.Column(sa.String, nullable=False)
    hashtags = sa.Column(sa.ARRAY(sa.String), nullable=False)
    published = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    edit_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    duration = sa.Column(sa.Integer, nullable=False)
    author_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=True)
    # foreign_keys could be empty if one foriegn key existed, we set uselist to Flase whenevever the relation is one
    user = sa.orm.relationship("User", back_populates="posts", lazy=True, foreign_keys=author_id, uselist=False)
    categories = sa.orm.relationship("Category", back_populates="posts", lazy=True, secondary='post_category')

    def add_cat(self, name):

        session = object_session(self)
        cat = session.query(Category).filter(Category.name == name).first()
        # cat = Category.query.filter(Category.name == name).first()
        print(f"this one {cat}")
        if cat is None:
            cat = Category(name=name)

        print('bye')
        return cat


class Category(db.Model):
    __versioned__ = {}
    __tablename__ = "categories"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    posts = sa.orm.relationship("Post", back_populates="categories", lazy=True, secondary='post_category')



# after you have defined all your models, call configure_mappers:
sa.orm.configure_mappers()
