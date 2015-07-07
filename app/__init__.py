# Import the basics
from flask import Flask, config
from flask.ext.restful import Api, fields
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

import os

# Kick of the app
app = Flask(__name__)
# Do some config - this needs to be moved to a seperate file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'holybloodysecret'
# Start Flask-Restless
api = Api(app)
# Start Flask-SQLAlchemy
db = SQLAlchemy(app)

# Import the Models
from app.models import Units, Subjects, Notes
# create all three database tables
db.create_all()

# Put some entries into the database so we have something to look at
# english = Units()
# english.name = 'frank'
# english.code = 'ENGL1234'
# english.coordinator = 'Kanye West'
# english.official_information = 'This is the first thing that you need to know begore you attend the heth the thing thing tihng thing ithng thing thing thing thing'
# english.official_link = 'http://www.google.com'
# db.session.add(english)
# db.session.commit()

# Setup the Admin interface and add the model views
admin = Admin(app, name='Counter Course Admin')
admin.add_view(ModelView(Units, db.session))
admin.add_view(ModelView(Subjects, db.session))
admin.add_view(ModelView(Notes, db.session))
static_path = os.path.join(os.path.dirname(__file__), 'static/notes')
admin.add_view(FileAdmin(static_path, '/static/', name='Notes Files'))

# Serve the Client
# Will either serve the client-side app from here or directly from Nginx

# Import the API resources (the endpoints)
from app.resources.units import UnitsAPI
from app.resources.units import UnitsListAPI
from app.resources.subjects import SubjectsAPI
from app.resources.subjects import SubjectsListAPI

# Endpoint Routing
api.add_resource(UnitsAPI, '/api/units/<int:id>', endpoint='unit')
api.add_resource(UnitsListAPI, '/api/units/', endpoint='units') 
api.add_resource(SubjectsAPI, '/api/subjects/<int:id>', endpoint='subject')
api.add_resource(SubjectsAPI, '/api/subjects/', endpoint='subjects')
