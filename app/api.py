from flask.ext.restful import Api, fields

# Start Flask-Restless
api = Api(app)

# Import the API resources (the endpoints)
from app.resources.units import UnitsAPI
from app.resources.units import UnitsListAPI
from app.resources.subjects import SubjectsAPI
from app.resources.subjects import SubjectsListAPI

# Endpoint Routing
api.add_resource(UnitsAPI, '/api/units/<int:id>', endpoint='unit')
api.add_resource(UnitsListAPI, '/api/units/', endpoint='units') 
api.add_resource(SubjectsAPI, '/api/subjects/<int:id>', endpoint='subject')
api.add_resource(SubjectsListAPI, '/api/subjects/', endpoint='subjects')
