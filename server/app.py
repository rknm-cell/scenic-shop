#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports


# Views go here!

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
            due_date = request.json['due_date']
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
        pass
    def post(self):
        pass

api.add_resource(Clients, "/clients")
