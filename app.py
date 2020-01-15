import os

from flask import Flask, render_template, request, session, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

engine = create_engine("postgresql://postgres:postgres@localhost")
dbsession = scoped_session(sessionmaker(bind=engine))



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/logging', methods=["POST"])
def login_check():
    email = request.form.get("email", None)
    password = request.form.get("pswd", None)

    dbemail = dbsession.execute("Select email from users where email = :email", {"email": email}).fetchone()
    dbpassword = dbsession.execute("Select password from users where email = :email", {"email": email}).fetchone()

    print(dbpassword)
    if not dbemail:
        return redirect('/logging')

    # Unpack db password's tuple and compare
    thepass = dbpassword[0]
    if thepass != password :
        return redirect('this')





@app.route('/register', methods=['POST', 'GET'])
def register():
    return redirect('/')



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True, host='0.0.0.0', port=4000)

