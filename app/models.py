from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='author',lazy=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

    
class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(255), index = True,nullable = False)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    comment =  db.relationship('Comment',backref='pitch',lazy='dynamic')
    upvotes =  db.relationship('Upvote',backref='pitch',lazy='dynamic')
    downvotes =  db.relationship('Downvote',backref='pitch',lazy='dynamic')

def __repr__(self):
      return f"User({self.content},{self.datePosted})"



class Comment(db.Model):

    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False) 
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'),nullable=False)
    comment = db.Column(db.String(100))

def __repr__(self):
    return f'User({self.comment})' 

class Upvote(db.Model):

    __tablename__ = 'upvotes'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'),nullable=False)
     
class Downvote(db.Model):

    __tablename__ = 'downvotes'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False) 
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'),nullable=False)
   
