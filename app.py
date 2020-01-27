import os
from models import *
from validate import *
import flask
from flask import Flask, render_template, request, jsonify, redirect, session
from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)
app.secret_key = '|lil0o0^obBo0I%|\||l0oiL|Ioo0|li110|oi|I#!0oi!I\|!I1iKL11lLii|'
engine = create_engine("postgresql://postgres:postgres@localhost")
dbsession = scoped_session(sessionmaker(bind=engine))

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# Count queries
def get_count(q):
    count_q = q.statement.with_only_columns([func.count()]).order_by(None)
    count = q.session.execute(count_q).scalar()
    return count


# ver. 0.1.0
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/users/all", methods=["POST"])
def posts():
    # Get start and end point for posts to generate. set the 0 and 5 for the get request
    start = int(request.form.get("start"))
    quantity = int(request.form.get("quantity"))

    posts = Post.query

    # Fast: SELECT COUNT(*) FROM Posts
    posts_count = get_count(posts)

    if posts_count is None:
        return jsonify({"error": "There are no posts"}), 422


    post_query = Post.query \
        .order_by(Post.published.desc()) \
        .offset(start) \
        .limit(quantity)
    # Iterate posts and get a list of post objects
    all_posts = []
    for post in post_query:
        all_posts.append(post)
        print(f"the start and end and i: {start}, {posts_count} , the post is {post.id}")

    # Get a list of jason per post containing detail of the post
    jsList = []
    for post in all_posts:
        json = {
            "id": post.id,
            "aut_fav": post.aut_fav,
            "uptittle": post.uptittle,
            "tittle": post.tittle,
            "mainp": post.mainp,
            "mainimg": post.mainimg,
            "tittle2": post.tittle2,
            "secondp": post.secondp,
            "video": post.video,
            "galtittle": post.galtittle,
            "galtext": post.galtext,
            "galimg1": post.galimg1,
            "galimgtxt1": post.galimgtxt1,
            "galimg2": post.galimg2,
            "galimgtxt2": post.galimgtxt2,
            "galimg3": post.galimg3,
            "galimgtxt3": post.galimgtxt3,
            "galimg4": post.galimg4,
            "galimgtxt4": post.galimgtxt4,
            "galimg5": post.galimg5,
            "galimgtxt5": post.galimgtxt5,
            "galimg6": post.galimg6,
            "galimgtxt6": post.galimgtxt6,
            "tittle3": post.tittle3,
            "subtittle": post.subtittle,
            "thirdp": post.thirdp,
            'published': post.published,
            "duration": post.duration,
            "author_id": post.author_id,
            "author_name": post.user.name,
        }
        jsList.append(json)

    # Reverse the posts order and return
    # jsList.reverse()
    return jsonify(jsList)


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

    # email in db compare pass
    user = User.query.filter_by(email=input_email).first()
    dbpass = user.password
    if dbpass != input_password:
        return render_template('try_again.html')

    # if all good modify the flask session and go to panel
    session['logged_in'] = True
    session['user_id'] = user.id
    session['user_name'] = user.name

    return redirect('/panel')


@app.route('/logout', methods=['GET'])
def logout():

    session['logged_in'] = False
    return redirect('/login')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if flask.request.method == "GET":
        return render_template("register.html")

    input_name = request.form.get("name")
    input_lastname = request.form.get("lastname")
    input_email = request.form.get("email")
    input_pass = request.form.get("pswd")


    # validate
    document = {'name': input_name, 'lastname': input_lastname, 'email': input_email, 'password': input_pass}
    if not v.validate(document, schema):
        return print('Try again because:', v.errors)

    # check if the email already exists
    dbemail = User.query.filter_by(email=document['email']).first()
    if dbemail:
        return render_template("error.html", message="This Email has already registered!")

    # insert
    user = User(**document)  # unpack the document
    dbsession.add(user)
    dbsession.commit()
    return render_template("success.html")


@app.route('/panel', methods=['GET'])
def panel():
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        author_name = session['user_name']
        author_id = session['user_id']
        return render_template('panel.html', author_id=author_id)


@app.route('/panelusers')
def users():
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        user_query = User.query.order_by(User.create_date.desc())
    # Iterate users and get a list of user objects
    all_users = []
    for user in user_query:
        all_users.append(user)

    # Get a list of jason per user containing detail of the user
    jsList = []
    for user in all_users:
        json = {
            "id": user.id,
            'name': user.name,
            'last_name': user.lastname,
            'email': user.email,
            "role": user.role,
        }
        jsList.append(json)

    return jsonify(jsList)


@app.route("/mypost", methods=["GET"])
def mypost():
    """add a post."""
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        author_name = session['user_name']
        author_id = session['user_id']
        print(f"author_id , author_name is {author_id}, {author_name}")
    #  Pass author_id to paneladd.js
    return render_template('paneladd.html', author_id=author_id, author_name=author_name)


@app.route("/api/user/theuser", methods=["GET", "POST"])
def loadposts():
    if not session.get('logged_in'):
        return redirect('/login')
    author_id = session['user_id']
    start = int(request.form.get("start"))
    quantity = int(request.form.get("quantity"))
    print(f"start is {start}")
    user = User.query.get(author_id)
    posts = user.posts
    print(posts)

    # Fast: SELECT COUNT(*) FROM Posts
    posts_count = Post.query.filter_by(author_id=author_id).count()
    print(f"post count: {posts_count}")
    if posts_count == 0:
        return jsonify({"error": "There are no posts"}), 422


    post_query = Post.query \
        .filter_by(author_id=author_id) \
        .order_by(Post.published.desc()) \
        .offset(start) \
        .limit(quantity)
    # Iterate posts and get a list of post objects
    all_posts = []
    for post in post_query:
        all_posts.append(post)

    # Get a list of jason per post containing detail of the post
    jsList = []
    for post in all_posts:
        json = {
            "id": post.id,
            "aut_fav": post.aut_fav,
            "uptittle": post.uptittle,
            "tittle": post.tittle,
            "mainp": post.mainp,
            "mainimg": post.mainimg,
            "tittle2": post.tittle2,
            "secondp": post.secondp,
            "video": post.video,
            "galtittle": post.galtittle,
            "galtext": post.galtext,
            "galimg1": post.galimg1,
            "galimgtxt1": post.galimgtxt1,
            "galimg2": post.galimg2,
            "galimgtxt2": post.galimgtxt2,
            "galimg3": post.galimg3,
            "galimgtxt3": post.galimgtxt3,
            "galimg4": post.galimg4,
            "galimgtxt4": post.galimgtxt4,
            "galimg5": post.galimg5,
            "galimgtxt5": post.galimgtxt5,
            "galimg6": post.galimg6,
            "galimgtxt6": post.galimgtxt6,
            "tittle3": post.tittle3,
            "subtittle": post.subtittle,
            "thirdp": post.thirdp,
            'published': post.published,
            "duration": post.duration,
            "author_id": post.author_id,
            "author_name": post.user.name,
        }
        jsList.append(json)

    return jsonify(jsList)


# @app.route("", methods=["POST", "GET"])
# def addpost(author_id):

    # Get the user and form information.
    # user = User.query.get(author_id)
    # req = request.form
    # for aut_fav, uptittle, tittle, mainp, mainimg, tittle2, secondp, video, galtittle, galtext, galimg1, \
    #     galimgtxt1, galimg2, galimgtxt2, galimg3, galimgtxt3, galimg4, galimgtxt4, galimg5, galimgtxt5, galimg6, \
    #     galimgtxt6, tittle3, subtittle, thirdp, hashtags, duration in req:
    #     user_post = user.add_post(aut_fav=aut_fav, uptittle=uptittle, tittle=tittle, mainp=mainp, mainimg=mainimg,
    #                               tittle2=tittle2, secondp=secondp, video=video, galtittle=galtittle, galtext=galtext,
    #                               galimg1=galimg1, galimgtxt1=galimgtxt1, galimg2=galimg2, galimgtxt2=galimgtxt2,
    #                               galimg3=galimg3, galimgtxt3=galimgtxt3, galimg4=galimg4, galimgtxt4=galimgtxt4,
    #                               galimg5=galimg5, galimgtxt5=galimgtxt5, galimg6=galimg6, galimgtxt6=galimgtxt6,
    #                               tittle3=tittle3, subtittle=subtittle, thirdp=thirdp, hashtags=hashtags,
    #                               duration=duration)



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
