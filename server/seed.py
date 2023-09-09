#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Department, Project, ProjectItems, Client, ClientProjects

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        department1 = Department("Drafting", "Drafts designs and drawings projects")
        department2 = Department("Carpentry", "Builds and assembles pieces from designs and drawings")
        department3 = Department("Scenic", "Patches, sands, paints, and finishes pieces according to designs and drawings")
        department4 = Department("Install", "Packs, assembles, and installs any finished pieces for a project")
        department5 = Department("CNC", "Adjusts designs and drawings to be created with CNC or lasercutter")

        project1 = Project("NYFW popup", "Popup of various stores promoting launch of client's new product line", 1, True)

        client1 = Client("Jewelry store", "High end jewelry brand")
        # Seed code goes here!