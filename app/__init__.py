# Import the basics
from flask import Flask, config
from flask.ext.restful import Api, fields
from flask.ext.sqlalchemy import SQLAlchemy

# Kick of the app, load the configuration file, start Flask-Restful and the Database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
api = Api(app)
db = SQLAlchemy(app)

# Import the Models
from app.models import Units, Subjects, Notes
# create all three database tables
db.create_all()

# Put some entries into the database so we have something to look at
english = Units('ENGL1234', 'Western Theories of Language', 'Nick Riemer', '1', '2015', 'This subject traverses the history of grammar and drags with it a focused eye over the history of intellectual thought', 'http://www.google.com', 'this subjects is sensational in the way that you would want any subject to be-do it', True, '1')
db.session.add(english)
db.session.commit()

# Serve the Client
@app.route('/')
def index():
    Units('1','1','1','1','1','1','1','1',True,'1')
    return 'doom' 

# Request Parsers
#    Common Parser
#    Search Parser
#    File Upload Parser

# Define the fields returned in the JSON

notes_fields = {
    'title': fields.String,
    'author': fields.String,
    'location': fields.String
    }

# Import Resources

from app.resources.units import UnitsAPI
from app.resources.units import UnitsListAPI
from app.resources.subjects import SubjectsAPI
from app.resources.subjects import SubjectsListAPI

# Endpoint Routing
api.add_resource(UnitsAPI, '/api/units/<int:id>', endpoint='unit')
api.add_resource(UnitsListAPI, '/api/units/', endpoint='units') 
api.add_resource(SubjectsAPI, '/api/subjects/<int:id>', endpoint='subject')
api.add_resource(SubjectsAPI, '/api/subjects/', endpoint='subjects')
