#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

# Local imports
from config import app, db, api
# Add your model imports
from models import Project, Client, Item, User, Department




class Projects(Resource):
    def get(self):
        projects_dict = [projects.to_dict(only = ("id", "name", "description", "client_id")) for projects in Project.query.all()]

        response = make_response(
            projects_dict,
            200
        )

        return response
    
    def post(self):
        
        new_project = Projects(
            name = request.json['name'],
            description = request.json['description'],
            client_id = request.json['client_id'],
            
        )

        db.session.add(new_project)
        db.session.commit()

        new_project_dict = new_project.to_dict()
        
        response = make_response(
            new_project_dict,
            201
        )
        return response

api.add_resource(Projects, "/projects")

class Clients(Resource):
    def get(self):
        projects_dict = [projects.to_dict(only = ("id", "name", "description", "projects")) for projects in Project.query.all()]

        response = make_response(
            projects_dict,
            200
        )

        return response
    
    def post(self):
        
        new_project = Client(
            name = request.json['name'],
            description = request.json['description'],
            
            
        )

        db.session.add(new_project)
        db.session.commit()

        new_project_dict = new_project.to_dict()
        
        response = make_response(
            new_project_dict,
            201
        )
        return response
    
    def delete(self, parent_id):
        parent = Client.query.get(parent_id)
        if parent:
            db.session.delete(parent)
            db.session.commit()
            return {"message": "Client and associated records deleted successfully."}
        else:
            return {"message": "Parent not found."}, 404

api.add_resource(Clients, "/clients")

if __name__ == '__main__':
    app.run(port=5555, debug=True)