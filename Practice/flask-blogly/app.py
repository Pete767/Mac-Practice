"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag

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



@app.route('/users')
def users_index():
    """users"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('index.html', user=user)


@app.route('/users/new', methods=["GET"])
def users_new_form():
    """create new user"""

    return render_template('new.html')


@app.route("/users/new", methods=["POST"])
def users_new():
    """submission for new user"""

    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>')
def users_show(user_id):
    """info on user"""

    user = User.query.get_or_404(user_id)
    return render_template('user.html', user=user)


@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    """edit form"""

    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """submit edit"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route('/user/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """delete user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/posts/new')
def posts_new_form(user_id):
    """new post form"""

    user = User.query.get_or_404(user_id)
    tags.query.all()
    return render_template('new_posts.html', user=user, tags=tags)


@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def posts_new(user_id):
    """new post"""

    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'],
                    content=request.form['content'],
                    user=user, tags=tags)
    tag_id = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_id)).all()

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
    tags = Tag.query.all()
    return render_template('edit_post.html', post=post, tags=tags)


@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def posts_update(post_id):
    """submit post edits"""

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    tag_id = [int(num) for num in request.form.getlist("tags")]
    post.tags = Tag.query.filter(Tag.id.in_(tag_id)).all()

    db.session.add(post)
    db.session.commit()
    flash(f"Post edited.")

    return redirect(f"/users/{post.user_id}")


@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def posts_destroy(post_id):
    """delete an existing post"""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()
    flash(f"'{post.title} deleted.")

    return redirect(f"/user/{post.user_id}"

@app.route('/tags')
def all_tags():

    tags = Tag.query.all()
    return render_template('tags_index.html', tags=tags)

@app.route('/tags/new')
def new_tag():

    posts = Post.query.all()
    return render_template('new_tag.html', posts=posts)

@app.route("/tags/new", methods=["POST"])
def newer_tag():

    post_id = [int(num) for num in request.form.getlist("posts")]
    posts = Post.query.filter(Post.id.in_(post_id)).all()
    tag_new = Tag(name=request.form['name'], posts=posts)

    db.session.add(tag_new)
    db.session.commit()

    return redirect("/tags")

@app.route('/tags/<int:tag_id>')
def get_tags(tag_id):
    """get tag info"""

    tag = Tag.query.get_or_404(tag_id)
    return render_template('tags.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit')
def edit_tag_form(tag_id):
    """tag edit form"""

    tag = Tag.query.get_or_404(tag_id)
    posts = Post.query.all()
    return render_template('edit_tag.html', tag=tag, posts=posts)

@app.route('/tags/<int:tag_id>/edit', methods=["POST"])
def edit_tags(tag_id):
    """update tag"""

    tag = Tag.query.get_or_404(tag_id)
    tag.name =request.form['name']
    post_ids = [int(num) for num in request.form.getlist("posts")]
    tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()

    db.session.add(tag)
    db.session.commit()

    return redirect("/tags")

@app.route('/tags/<int:tag_id>/delete', methods=["POST"])
def tags_destroy(tag_id):
    """delete a tag"""

    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    flash(f"'{tag.name}' deleted.")

    return redirect("/tags")

    