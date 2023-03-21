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
    


def connect_db(app):

    db.app = app
    db.init_app(app)
