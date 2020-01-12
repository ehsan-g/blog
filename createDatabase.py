from models import *
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://postgres:postgres@localhost")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
todo = ""


with app.app_context():
    while todo != "Exit":
        todo = ""
        db.session.commit()
        todo = input("Just say it: ")
        if todo == "Drop":
            db.drop_all()
            db.session.commit()
            print("Consider it Done")

        elif todo == "Create":

                db.session.commit()
                db.create_all()
                print("Done")

        elif todo != "Create" and todo != "Drop" and todo != "Exit":
            print("Do you even Know me?")

    print("Farewell Sir!")


