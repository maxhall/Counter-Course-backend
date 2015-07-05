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

    def __init__(self, code, name, coordinator, semester, year, official_information, official_link, review):
	self.code = code
	self.name = name
	self.coordinator = coordinator
	self.semester = semester
	self.year = year
	self.official_information = official_information
	self.official_link = official_link
	self.review = review

# class Subjects(db.model):

# class Notes(db.model):
db.create_all()

english = Units('ENGL1234', 'Western Theories of Language', 'Nick Riemer', '1', '2015', 'This subject traverses the history of grammar and drags with it a focused eye over the history of intellectual thought', 'http://www.google.com', 'this subjects is sensational in the way that you would want any subject to be-do it')
db.session.add(english)
db.session.commit()

# Serve the Client

@app.route('/')
def index():
    thing = Units.query.get(1)
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

# Endpoint classes
class UnitsAPI(Resource):
    @marshal_with(units_fields)
    def get(self, id):
	unit = Units.query.get(id)
	# return {'name': str(unit.name),
	#	'code': str(unit.code)}
	return unit

class UnitsListAPI(Resource):
    @marshal_with(units_fields)
    def get(self):
	list = Units.query.all()
	return list 

# Endpoint Routing
api.add_resource(UnitsAPI, '/api/units/<int:id>', endpoint='unit')
api.add_resource(UnitsListAPI, '/api/units/', endpoint='units') 

# Start da App
if __name__ == '__main__':
	app.run(debug=True)
