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
        department1 = Department("Drafting", "Drafts designs and drawings projects")
        department2 = Department("Carpentry", "Builds and assembles pieces from designs and drawings")
        department3 = Department("Scenic", "Patches, sands, paints, and finishes pieces according to designs and drawings")
        department4 = Department("Install", "Packs, assembles, and installs any finished pieces for a project")
        department5 = Department("CNC", "Adjusts designs and drawings to be created with CNC or lasercutter")
        departments = [department1, department2, department3, department4, department5]
        db.session.add_all(departments)
        db.session.commit()

        print("Seeding clients")
        client1 = Client("Jewelry store", "High end jewelry brand")
        client2 = Client("Animation company", "Feature film animation studio")
        clients = [client1, client2]
        db.session.add_all(clients)
        db.session.commit()
        
        print("Seeding projects")
        project1 = Project("NYFW popup", "Popup of various stores promoting launch of client's new product line", 1, True)
        projects = [project1]
        db.session.add_all(projects)
        db.session.commit()

        print("Seeding ProjectItems")
        # Seed code goes here!