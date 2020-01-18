import os
import time
from models import *
from validate import *
import flask
from flask import Flask, render_template, request,jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)
engine = create_engine("postgresql://postgres:postgres@localhost")
dbsession = scoped_session(sessionmaker(bind=engine))

app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://postgres:postgres@localhost")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/users/<int:author_id>")
def posts(author_id):
    # Make sure author_id exists.
    user = User.query.get(author_id)
    if user is None:
        return jsonify({"error": "Invalid author_id"}), 422

    # Get all posts of the user
    posts = user.posts

    # Get number of available posts.
    posts_count = Post.query.count()


    authors = []
    for post in posts:
        authors.append(post.author_id)

    # Artificially delay speed of response.
    time.sleep(1)

    # Return list of posts' values.
    return jsonify({
        'uptitle': post.uptitle,
        'title': post.title,
        'mainp': post.mainp,
        'mainimg': post.mainimg,
        'title2': post.title2,
        'secondp': post.secondp,
        'video': post.video,
        'galtitle': post.galtitle,
        'galtext': post.galtext,
        'galimg1': post.galimg1,
        'galimgtxt1': post.galimgtxt1,
        'galimg2': post.galimg2,
        'galimgtxt2': post.galimgtxt2,
        'galimg3': post.galimg3,
        'galimgtxt3': post.galimgtxt3,
        'galimg4': post.galimg4,
        'galimgtxt4': post.galimgtxt4,
        'galimg5': post.galimg5,
        'galimgtxt5': post.galimgtxt5,
        'galimg6': post.galimg6,
        'galimgtxt6': post.galimgtxt6,
        'tittle3': post.tittle3,
        'subtitle': post.subtitle,
        'thirdp': post.thirdp,
        'duration': post.duration,
        'author': authors
    })











@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logging', methods=['POST', 'GET'])
def login_check():
    input_email = request.form.get("email", None)
    input_password = request.form.get("pswd", None)

    dbemail = User.query.filter_by(email=input_email).first()

    # check if email in db
    if not dbemail:
        return render_template('try_again.html')

    # if email in db compare pass
    user = User.query.filter_by(email=input_email).first()
    dbpass = user.password
    if dbpass != input_password:
        return render_template('try_again.html')

    # if all good go to panel
    return render_template('')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if flask.request.method == "GET":
        return render_template("register.html")

    input_name = request.form.get("name")
    input_email = request.form.get("email")
    input_pass = request.form.get("pswd")


    # validate
    document = {'name': input_name, 'email': input_email, 'password': input_pass}
    if not v.validate(document, schema):
        return print('Try again because:', v.errors)

    # check if the email already exists
    dbemail = User.query.filter_by(email=document['email']).first()
    if dbemail is not None:
        return render_template("error.html", message="This Email has already registered!")

    # insert
    user = User(**document)  # unpack the document
    dbsession.add(user)
    dbsession.commit()
    return render_template("success.html")

# @app.route("/addpost", methods=["POST"])
# def addpost():
#     """add a post."""
#
#     # Get form information.
#     name = request.form.get("name")
#     author = int(request.form.get("author"))
#
#     # Add post.
#     user = User.query.get(id)
#
#     user.add_post(name)
#     user = User.query.get(author)
#     return render_template("success.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4400)
