from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Jokes:
    '''
    Jokes class to define the objects
    '''
    def __init__(self, name, title, joke):
        self.name = name
        self.title = title
        self.joke = joke


class Product:
    '''
    Product class to define the objects
    '''
    def __init__(self, name, title, product):
        self.name = name
        self.title = title
        self.product = product


class Vows:
    '''
    Vows class to define the objects
    '''
    def __init__(self, name, title, vow):
        self.name = name
        self.title = title
        self.vow = vow


class Comment:

    all_comments = []

    def __init__(self, title, comment):
        self.title = title
        self.comment = comment

    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'