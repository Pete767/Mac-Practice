from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models for Blogly."""
class User(db.Model):
    __tablename__ = "users"

    id = db.Column (db.Integer, primary_key=True,
    autoincrement=True)
    first_name = db.Column (db.Text(25), nullable=False)
    last_name = db.Column (db.Text(30), nullable=False)
    image_url = db.Column (db.Text, nullable=False)

    posts = db.relationship("Post", backref="user")

    @property
    def full_name(self):
        """gives full name"""

        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    made = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeinKey('users.id'), nullable=False)

    @property
    def posted_date(self):
        return self.made.strftime("%c")

class Tag(db.Model):
    """tags for posts"""
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    posts = db.relationship('Post', secondary="posts_tags", backref="tags")

class PostTag(db.Model):
    """tags attached to post"""

    __tablename__ = "posts_tags"
    post_id = db.Column(db.Integer, db.ForeinKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeinKey('tags.id'), primary_key=True)

    


def connect_db(app):

    db.app = app
    db.init_app(app)
