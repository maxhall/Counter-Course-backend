# Imports
from flask import Flask
from flask.ext.restful import Api, Resource, fields, marshal_with
from flask.ext.sqlalchemy import SQLAlchemy

# Kick of the app, sort some things and load the configuration
app = Flask(__name__)
# app.config.from_pyfile(config.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
api = Api(app)
db = SQLAlchemy(app)

# Database Models

class Units(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8))
    name = db.Column(db.String(50))
    coordinator = db.Column(db.String(50))
    semester = db.Column(db.Integer)
    year = db.Column(db.Integer)
    official_information = db.Column(db.Text)
    official_link = db.Column(db.String(100))
    review = db.Column(db.Text)
    published = db.Column(db.Boolean)
    # Foreign Key column pointing to the Unit's Subjects Area
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id')
    # Relationship to the Notes that are intended for this Subject
    notes = db.relationship('Notes', backref='Unit', lazy='dynamic')

    def __init__(self, code, name, coordinator, semester, year, official_information, official_link, review, published, subject):
	self.code = code
	self.name = name
	self.coordinator = coordinator
	self.semester = semester
	self.year = year
	self.official_information = official_information
	self.official_link = official_link
	self.review = review
	self.published = published
	self.subject = subject

class Subjects(db.models):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    official_link = db.Column(db.String(100))
    review = db.Column(db.Text)
    published = db.Column(db.Boolean)
    # Relationship to the Units that comprise the Subject Area
    units = db.relationship('Units', backref='Subject', lazy='dynamic')


    def __init__(self, name, official_link, review, published)
	self.name = name
	self.official_link = official_link
	self.review = review
	self.published = published

class Notes(db.models):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    location = db.Column(db.String(80))
    published = db.Column(db.Boolean)
    # Foreign Key of the Unit that the notes are for
    unit = db.Column(db.Integer, db.ForeignKey('units.id')

    def __init__(title, author, location, published, unit)
	self.title = title
	self.author = author
	self.location = location
	self.published = published
	self.unit = unit

# create all three database tables
db.create_all()

# Put some entries into the database so we have something to look at
english = Units('ENGL1234', 'Western Theories of Language', 'Nick Riemer', '1', '2015', 'This subject traverses the history of grammar and drags with it a focused eye over the history of intellectual thought', 'http://www.google.com', 'this subjects is sensational in the way that you would want any subject to be-do it', True)
db.session.add(english)
db.session.commit()

# Serve the Client
@app.route('/')
def index():
    thing = Units.query.all()
    return str(thing.coordinator) 

# Request Parsers
#    Common Parser
#    Search Parser
#    File Upload Parser

# Define the fields returned in the JSON object
units_fields = {
    'code': fields.String,
    'name': fields.String,
    'coordinator': fields.String,
    'semester': fields.Integer,
    'year': fields.Integer,
    'official_information': fields.String,
    'official_link': fields.String,
    'review': fields.String
    }
units_fields['notes'] = {}

subjects_fields = {
    'name': fields.String,
    'official_link': field.String,
    'review': field.String,
    }
subjects_fields['units'] = {}

# Endpoint classes
class UnitsAPI(Resource):
    @marshal_with(units_fields)
    def get(self, id):
	unit = Units.query.get(id)
	return unit

class UnitsListAPI(Resource):
    @marshal_with(units_fields)
    def get(self):
	list = Units.query.all()
	return list 

class SubjectsAPI(Resource):
    @marshal_with(subjects_fields)
    def get(self, id):
	subject = Subjects.query.get(id)
	return subject

class SubjectsListAPI(Resource):
    @marshal_with(subjects_fields)
    def get(self):
	list = Subjects.query.all()
	return list

# Endpoint Routing
api.add_resource(UnitsAPI, '/api/units/<int:id>', endpoint='unit')
api.add_resource(UnitsListAPI, '/api/units/', endpoint='units') 
api.add_resource(SubjectsAPI, '/api/subjects/<int:id>', endpoint='subject')
api.add_resourve(SubjectsAPI, '/api/subjects/', endpoint='subjects')

# Start da App
if __name__ == '__main__':
	app.run(debug=True)
