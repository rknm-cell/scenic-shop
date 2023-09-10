from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    title = db.Column(db.String)
    email = db.Column(db.String)
    department = db.Column(db.String, db.ForeignKey('departments.name'), )

    @validates('department')
    def validates_department(self, key, department):
        departments = Department.query.all()
        department_name = [self.department for department in departments]
        if department not in department_name:
            raise ValueError('Must be a valid department')
        return department

class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    items = db.relationship('Item', backref='departments')

class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    # due_date = db.Column(db.DateTime)
    active = db.Column(db.Boolean)
class Paint(db.Model):
    __tablename__ = "paints"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    item_id = db.relationship('Item', backref='paints')

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    number = db.Column(db.Integer)
    description = db.Column(db.String)
    current_department = db.Column(db.Integer, db.ForeignKey('departments.id'))
    paint_id = db.Column(db.Integer, db.ForeignKey('paints.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    projects = db.relationship('Project', backref='clients', lazy=True)

