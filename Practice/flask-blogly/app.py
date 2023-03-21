"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def root():
    """Homepage"""

   posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template("posts/homepage.html", posts=posts)


@app.errorhandler(404)
def page_not_found(e):
    """404 page"""

    return render_template('404.html'), 404



@app.route('/user')
def users_index():
    """users"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('index.html', users=users)


@app.route('/user/new', methods=["GET"])
def users_new_form():
    """create new user"""

    return render_template('new.html')


@app.route("/user/new", methods=["POST"])
def users_new():
    """submission for new user"""

    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/user")


@app.route('/user/<int:user_id>')
def users_show(user_id):
    """info on user"""

    user = User.query.get_or_404(user_id)
    return render_template('user.html', user=user)


@app.route('/user/<int:user_id>/edit')
def users_edit(user_id):
    """edit form"""

    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)


@app.route('/user/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """submit edit"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/user")


@app.route('/user/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """delete user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/user")

@app.route('/user/<int:user_id>/posts/new')
def posts_new_form(user_id):
    """new post form"""

    user = User.query.get_or_404(user_id)
    return render_template('new_posts.html', user=user)


@app.route('/user/<int:user_id>/posts/new', methods=["POST"])
def posts_new(user_id):
    """new post"""

    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'],
                    content=request.form['content'],
                    user=user)

    db.session.add(new_post)
    db.session.commit()
    flash(f"'{new_post.title}' added.")

    return redirect(f"/users/{user_id}")


@app.route('/posts/<int:post_id>')
def posts_show(post_id):
    """show a specific post"""

    post = Post.query.get_or_404(post_id)
    return render_template('posts.html', post=post)


@app.route('/posts/<int:post_id>/edit')
def posts_edit(post_id):
    """edit a post"""

    post = Post.query.get_or_404(post_id)
    return render_template('edit_post.html', post=post)


@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def posts_update(post_id):
    """submit post edits"""

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.add(post)
    db.session.commit()
    flash(f"Post edited.")

    return redirect(f"/user/{post.user_id}")


@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def posts_destroy(post_id):
    """delete an existing post"""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()
    flash(f"'{post.title} deleted.")

    return redirect(f"/user/{post.user_id}"
