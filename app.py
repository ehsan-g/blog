from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://postgres:postgres@localhost")
dbsession = scoped_session(sessionmaker(bind=engine))





