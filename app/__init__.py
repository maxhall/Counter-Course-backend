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

english = Units()
english.name = 'frank'
english.code = 'ENGL1234'
english.coordinator = 'Kanye West'
english.official_information = 'This is the first thing that you need to know begore you attend the heth the thing thing tihng thing ithng thing thing thing thing'
english.official_link = 'http://www.google.com'
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
