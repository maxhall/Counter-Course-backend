# The resources for the Units endpoint

from flask.ext.restful import Resource, fields, marshal_with
from app.models import Units, Subjects, Notes
from app.resources.notes import notes_fields

units_fields = {
    'code': fields.String,
    'name': fields.String,
    'coordinator': fields.String,
    'semester': fields.Integer,
    'year': fields.Integer,
    'official_information': fields.String,
    'official_link': fields.String,
    'review': fields.String,
    'notes': fields.Nested(notes_fields)
    }

units_name_fields = {
    'name': fields.String,
    'code': fields.String
    }

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
