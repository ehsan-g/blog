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
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # will limit the maximum allowed payload -- 1 megabytes
db.init_app(app)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Count queries
def get_count(q):
    count_q = q.statement.with_only_columns([func.count()]).order_by(None)
    count = q.session.execute(count_q).scalar()
    return count


# ver. 0.2.9
@app.route("/")
def index():
    return render_template("index.html")


@app.route('/api/users/all')
def users():
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        user_query = dbsession.query(User).order_by(User.create_date.desc())
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
        print(jsList)
    return jsonify(jsList)


@app.route("/api/posts/all", methods=["POST"])
def all_posts():
    # Get start and end point for posts to generate. set the 0 and 5 for the get request
    start = int(request.form.get("start"))
    quantity = int(request.form.get("quantity"))

    posts = dbsession.query(Post)
    print(f"this is all the posts {posts}")

    # Fast: SELECT COUNT(*) FROM Posts
    posts_count = get_count(posts)
    print(f"all post count: {posts_count}")

    if posts_count == 0:
        return jsonify({
                       "error": "There are no posts",
                       "start": 0}
                       ), 422
    print("fuck")
    post_query = dbsession.query(Post) \
        .order_by(Post.published.desc()) \
        .offset(start) \
        .limit(quantity)
    # Iterate posts and get a list of post objects
    all_posts = []
    for post in post_query:
        for cat in post.categories:
            print(f"cat is {cat}")
        all_posts.append(post)




    # Get a list of jason per post containing detail of the post
    jsList = []
    for post in all_posts:
        json = {
            "id": post.id,
            'cats': [c.name for c in post.categories],
            'duration': post.duration,
            "aut_fav": post.aut_fav,
            "tittle": post.tittle,
            "uptittle": post.uptittle,
            "mainp": post.mainp,
            # "mainimg": post.mainimg.decode(),
            'mainalt': post.mainalt,
            "tittle2": post.tittle2,
            "video": post.video,
            "secondp": post.secondp,
            'subtittle': post.subtittle,
            'tittle3': post.tittle3,
            'thirdp': post.thirdp,
            # 'album': post.album.decode(),
            'albumtittle': post.albumtittle,
            'albump': post.albump,
            'albumimgalt': post.albumimgalt,
            'albumimgtxt': post.albumimgtxt,
            'published': post.published,
            "author_id": post.author_id,
            "author_name": post.user.name,
        }
        jsList.append(json)

    # Reverse the posts order and return
    # jsList.reverse()
    print(jsList)
    return jsonify(jsList)


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
    dbemail = dbsession.query(User).filter_by(email=document['email']).first()
    if dbemail:
        return render_template("error.html", message="This Email has already registered!")

    # insert
    user = User(**document)  # unpack the document
    dbsession.add(user)
    dbsession.commit()
    return render_template("success.html")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logging', methods=['POST'])
def login_check():
    input_email = request.form.get("email", None)
    input_password = request.form.get("pswd", None)

    dbemail = dbsession.query(User).filter_by(email=input_email).first()

    # check if email in db
    if not dbemail:
        return render_template('try_again.html')

    # email in db compare pass
    user = dbsession.query(User).filter_by(email=input_email).first()
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


@app.route('/panel', methods=['GET'])
def panel():
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        author_id = session['user_id']
        return render_template('panel.html', author_id=author_id)


# Render the addpanel first uses the loadposts() to receive user's posts
@app.route("/users/user/mypage", methods=["GET"])
def my_page():
    """add a post."""
    print("my_page")
    if not session.get('logged_in'):
        return redirect('/login')

    author_name = session['user_name']
    author_id = session['user_id']
    cats = dbsession.query(Category).all()

    published = datetime.utcnow()
    return render_template('paneladd.html', author_id=author_id, author_name=author_name, published=published, cats=cats)


@app.route("/myposts", methods=["POST", "GET"])
def my_posts():
    print("my_posts")
    if not session.get('logged_in'):
        return redirect('/login')
    author_id = session['user_id']

    # Get start and end point for posts to generate. set the 0 and 5 for the get request
    start = int(request.form.get("start"))
    quantity = int(request.form.get("quantity"))

    # Count posts
    user = dbsession.query(User).get(author_id)
    posts = user.posts
    if not posts:
        return jsonify({"error": "There are no posts"}), 422


    # Fast: SELECT COUNT(*) FROM Posts
    posts_count = dbsession.query(Post).filter_by(author_id=author_id).count()

    post_query = dbsession.query(Post) \
        .filter_by(author_id=author_id) \
        .order_by(Post.published.desc()) \
        .offset(start) \
        .limit(quantity)
    # Iterate posts and get a list of post objects
    all_posts = []
    for post in post_query:
        all_posts.append(post)
        print('sdddddddddd', post.albumimgtxt)

    # Get a list of jason per post containing detail of the post
    jsList = []
    for post in all_posts:
        json = {
            "id": post.id,
            'cats': [c.name for c in post.categories],
            'duration': post.duration,
            "aut_fav": post.aut_fav,
            "tittle": post.tittle,
            "uptittle": post.uptittle,
            "mainp": post.mainp,
            # "mainimg": post.mainimg.read(),
            'mainalt': post.mainalt,
            "tittle2": post.tittle2,
            "video": post.video,
            "secondp": post.secondp,
            'subtittle'  : post.subtittle,
            'tittle3': post.tittle3,
            'thirdp' : post.thirdp,
            # 'album' : post.album.decode(),
            'albumtittle': post.albumtittle,
            'albump'  : post.albump,
            'albumimgalt' : post.albumimgalt,
            'albumimgtxt' : post.albumimgtxt,
            'published': post.published,
            "author_id": post.author_id,
            "author_name": post.user.name,
        }
        jsList.append(json)
    print(jsList)
    return jsonify(jsList)


@app.route("/api/user/addpost", methods=["POST", "GET"])
def add_post():
    print("add_post")
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        author_id = session['user_id']
    user = dbsession.query(User).get(author_id)
    req = request.form
    print(request.files)

    catsform = request.form.getlist('theselect')
    duration = request.form['duration']
    aut_fav = request.form.get('aut_fav')
    tittle = request.form['tittle']
    uptittle = request.form['uptittle']
    mainp = request.form['mainp']
    mainimg = request.files['mainimg'].read()
    mainalt = request.form['mainalt']
    tittle2 = request.form['tittle2']
    video = request.form['video']
    secondp = request.form['secondp']
    subtittle = request.form['subtitle']
    tittle3 = request.form['duration']
    thirdp = request.form['thirdp']
    hashtags = request.form.get('tags')
    album = request.form['album'].encode()
    albumtittle = request.form['albumtiitle']
    albump = request.form['albump']
    albumalt1 = request.form['albumalt1']
    albumtxt1 = request.form['albumtxt1']
    albumalt2 = request.form['albumalt2']
    albumtxt2 = request.form['albumtxt2']
    albumalt3 = request.form['albumalt3']
    albumtxt3 = request.form['albumtxt3']
    albumalt4 = request.form['albumalt4']
    albumtxt4 = request.form['albumtxt4']
    albumalt5 = request.form['albumalt5']
    albumtxt5 = request.form['albumtxt5']
    albumalt6 = request.form['albumalt6']
    albumtxt6 = request.form['albumtxt6']


    if aut_fav is None:
        aut_fav = 'off'
    # catnames = cats.split(';')
    # # hashtags = hashtags.split(';')
    albumimgalt = [albumalt1, albumalt2, albumalt3, albumalt4, albumalt5, albumalt6]
    albumimgtxt = [albumtxt1, albumtxt2, albumtxt3, albumtxt4, albumtxt5, albumtxt6]

    user_post = user.add_post(
        aut_fav=aut_fav, duration=duration, uptittle=uptittle, tittle=tittle, mainp=mainp,
        mainimg=mainimg, mainalt=mainalt, tittle2=tittle2, secondp=secondp, video=video,
        tittle3=tittle3, subtittle=subtittle, thirdp=thirdp, hashtags=hashtags,
        album=album, albumtittle=albumtittle, albump=albump,
        albumimgalt=albumimgalt, albumimgtxt=albumimgtxt
    )
    print("vfdvfdvfd", type(catsform[0]))
    # Finds the cats which we received from front dropdown
    cats = dbsession.query(Category).filter(Category.name.in_(catsform)).all()
    print(cats)
    user_post.add_cats(cats)

    print(user.name, user_post)
   # dbsession.add(user_post)
    #
    #     for name in catnames:
    #         cat = user_post.add_cat(name)
    #         user_post.categories.append(cat)
    #
    #     dbsession.add(user_post)
    dbsession.commit()
    #     dbsession.close()
    return redirect('/users/user/mypage')


@app.route("/posts/categories", methods=["GET"])
def categories():
    if not session.get('logged_in'):
        return redirect('/login')

    author_id = session['user_id']
    cats = dbsession.query(Category).all()
    print(cats)
    return render_template('categories.html', author_id=author_id, cats=cats)


@app.route("/api/posts/categories/all", methods=["GET"])
def all_cats():
    cats = dbsession.query(Category)

    # Iterate posts and get a list of post objects
    all_posts = []
    for cat in cats:
        all_posts.append(cat)
        print(cat)



    # Get a list of jason per post containing detail of the post
    jsList = []
    for cat in cats:
        json = {
            "id": cat.id,
            "name": cat.name,
        }
        jsList.append(json)

    return jsonify(jsList)



@app.route("/posts/categories/add", methods=["POST"])
def create_cat():
    if not session.get('logged_in'):
        return redirect('/login')

    cat_name = request.form.get("catname")
    print(cat_name)
    new_cat = Category.create_cat(cat_name)
    print(new_cat)
    dbsession.add(new_cat)
    dbsession.commit()
    dbsession.close()

    return redirect('/posts/categories')


@app.route("/remove/cat/<int:cat_id>", methods=["POST"])
def remove_cat(cat_id):
    if not session.get('logged_in'):
        return redirect('/login')

    cat = dbsession.query(Category).get(cat_id)
    print(dbsession)
    dbsession.delete(cat)
    dbsession.commit()

    return redirect('/posts/categories')


if __name__ == "__main__":
    app.secret_key = os.urandom(1)
    app.run(debug=True, host='0.0.0.0', port=4090)
