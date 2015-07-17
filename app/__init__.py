# Import the basics
from flask import Flask, config
from flask.ext.sqlalchemy import SQLAlchemy

import os
import re

# Kick off the app
app = Flask(__name__)
# Do some config - this needs to be moved to a seperate file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'holybloodysecret'

# Start Flask-SQLAlchemy
db = SQLAlchemy(app)
# Import the Models and create the database tables
from models import Units, Subjects, Notes
db.create_all()

# Import the Views
import views

# Import the Administration Interface
import admin

# Optionally import the API endpoints. We're not going to.
