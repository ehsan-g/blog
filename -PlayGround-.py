from app import app
from models import *



with app.app_context():

    email = 'ehsan@say.company'
    # user = User.query.get(1)
    user = User.query.filter_by(email=email).first()
    print(user.email)