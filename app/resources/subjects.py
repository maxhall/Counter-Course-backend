# The resources for the Subjects endpoint

from flask.ext.restful import Resource, fields, marshal_with
from app.models import Units, Subjects, Notes
from app.resources.units import units_fields

subjects_fields = {
    'name': fields.String,
    'official_link': fields.String,
    'review': fields.String,
    'units': fields.Nested(units_fields)
    }

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
