from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)

class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    # due_date = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

class Item(db.Model):
    __tablename__ = "projectitems"
    id = db.Column(db.Integer)
    name = db.Column(db.String)
    description = db.Column(db.String)
    paint_id = db.ForeignKey(db.Integer, db.ForeignKey('paint.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

class Paint(db.Model):
    __tablename__ = "paints"
    id = db.Column(db.Integer)
    name = db.Column(db.String)
    color = db.Column(db.String)
    item_id = db.relationship('Item', backref='paint')
class Client(db.Model):
    __tablename__ = "clients"
    name = db.Column(db.String, unique=True, nullable=False)
    projects = db.relationship('Project', backref='client', lazy=True)

