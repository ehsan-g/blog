from models import *
from app import app


app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://postgres:postgres@localhost")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():

    todo = ""

    while todo != "Exit":
        todo = ""
        db.session.commit()
        todo = input("Just say it: ")
        if todo == "d":
            db.drop_all()
            db.session.commit()
            print("Consider it Done")

        elif todo == "c":
            try:
                user = User.query.geCt(2)
            except:
                user = None
            if user:
                print("Shit it exists!")
            else:
                db.session.commit()
                db.create_all()
                print("Done")

        elif todo != "Create" and todo != "Drop" and todo != "Exit":
            print("Do you even Know me?")

    print("Farewell Sir!")
