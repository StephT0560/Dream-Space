from recs import book_recs
import models
import forms
from flask import Flask, g, render_template, flash, redirect, url_for, abort
from flask_bcrypt import Bcrypt, check_password_hash
from flask_login import (
    LoginManager,
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)

DEBUG = True
HOST = "0.0.0.0"


app = Flask(__name__)
# import secerts and run secrets.token_hex(16) in terminal
app.config["SECRET_KEY"] = "get your own"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """connect to database before connecting"""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the database connection after each request"""
    g.db.close()
    return response


@app.route("/register", methods=("GET", "POST"))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Yay, you registered!", "success")
        models.User.create_user(username=form.username.data,email=form.email.data, password=form.password.data)
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/login", methods=("GET", "POST"))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Email is incompatible", "error")

        if check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("You are logged in", "success")
            return redirect(url_for("index"))
        else:
            flash("Password does not match", "error")
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You've been logged out! Come back soon!", "success")
    return redirect(url_for("home"))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/index")
def index():
    stream = models.Post.select().limit(100)
    for post in stream:
        books = book_recs(post.book)
        for i in range(len(books)-1):
            if len(books[i]) > 50:
                remove = books.pop(i)
        post.recommendations = books

    return render_template("stream.html", stream=stream)


@app.route("/stream")
@app.route("/stream/<username>")
@login_required
def stream(username=None):

    template = "stream.html"
    if username and username != current_user.username:
        try:
            user = models.User.select().where(models.User.username**username).get()
        except models.DoesNotExist:
            abort(404)
        else:
            stream = user.get_post().limit(100)
    else:
        stream = current_user.get_stream().limit(100)
        user = current_user
    if username:
        template = "user_stream.html"
    return render_template(template, stream = stream, user = user)


@app.route('/post/<int:post_id>')
def view_post(post_id):
    posts = models.Post.select().where(models.Post.id == post_id)
    if posts.count() == 0:
        abort(404)
    return render_template('stream.html', stream=posts)



@app.route("/follow/<username>")
@login_required
def follow(username):
    try:
        to_user = models.User.get(models.User.username**username)
    except models.DoesNotExist:
        abort(404)
    else:
        try:
            models.Relationship.create(
                from_user=g.user._get_current_object(), to_user=to_user
            )
        except models.IntegrityError:
            abort(404)
        else:
            flash("You're now following {}!".format(to_user.username), "success")
    return redirect(url_for("stream", username=to_user.username))


@app.route("/unfollow/<username>")
@login_required
def unfollow(username):
    try:
        to_user = models.User.get(models.User.username**username)
    except models.DoesNotExist:
        pass
    else:
        try:
            models.Relationship.get(
                from_user=g.user._get_current_object(), to_user=to_user
            ).delete_instance()
        except models.IntegrityError:
            pass
        else:
            flash("You've unfollowed {}!".format(to_user.username), "success")
    return redirect(url_for("stream", username=to_user.username))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


@app.route("/new_post", methods=("GET", "POST"))
@login_required
def post():
    form = forms.PostForm()
    if form.validate_on_submit():
        models.Post.create(
            user=g.user._get_current_object(), content=form.content.data.strip(), book = form.book.data.strip()
        )
        flash("Message posted! Thanks!", "success")
        return redirect(url_for("index"))
    return render_template("post.html", form=form)


if __name__ == "__main__":
    models.initialize()
    try:
        models.User.create_user(
            username="stephen",
            email="stisselin216@gmail.com",
            password="123",
            admin=True,
        )
    except ValueError:
        pass

    app.run(host = HOST, debug=DEBUG)
