#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Department, Project, Client

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Clearing database")
        Department.query.delete()
        Client.query.delete()
        Project.query.delete()
        print("Starting seed...")
        print("Seeding departments...")
        department1 = Department(name="Drafting", description="Drafts designs and drawings projects")
        department2 = Department(name="Carpentry", description="Builds and assembles pieces from designs and drawings")
        department3 = Department(name="Scenic", description="Patches, sands, paints, and finishes pieces according to designs and drawings")
        department4 = Department(name="Install", description="Packs, assembles, and installs any finished pieces for a project")
        department5 = Department(name="CNC", description="Adjusts designs and drawings to be created with CNC or lasercutter")
        departments = [department1, department2, department3, department4, department5]
        db.session.add_all(departments)
        db.session.commit()

        print("Seeding clients")
        client1 = Client(name="Jewelry store", description="High end jewelry brand")
        client2 = Client(name="Animation company", description="Feature film animation studio")
        clients = [client1, client2]
        db.session.add_all(clients)
        db.session.commit()
        
        print("Seeding projects")
        project1 = Project(name="NYFW popup", description="Popup of various stores promoting launch of client's new product line", client_id=1, active=True)
        projects = [project1]
        db.session.add_all(projects)
        db.session.commit()

        print("Seeding ProjectItems")
        # Seed code goes here!