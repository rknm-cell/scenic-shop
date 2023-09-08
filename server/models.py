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
    name = db.Column(db.String, unique=True, nullable=false)

class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    due_date = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

class ProjectItems(db.Model):
    __tablename__ = "projectitems"
    id = db.Column(db.Integer)
    name = db.Column(db.String)
    description = db.Column(db.String)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)


class Client(db.Model):
    __tablename__ = "clients"
    projects = db.relationshiop('Projects', backref='clients')

class ClientProjects(db.Model):
    __tablename__ = "clientprojects"    