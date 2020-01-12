from models import *

todo = ""

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


