
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask


app = Flask(__name__)

engine = create_engine("postgresql://postgres:postgres@localhost")
sess = scoped_session(sessionmaker(bind=engine))
