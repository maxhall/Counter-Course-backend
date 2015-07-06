from flask.ext.restful import Resource, fields, marshal_with
from app.models import Units, Subjects, Notes

notes_fields = {
    'title': fields.String,
    'author': fields.String,
    'location': fields.String
    }

class NotesAPI(Resource):
    @marshal_with(notes_fields)
    def get(self, id):
	note = Notes.query.get(id)
	return note

    def put(self):

class NotesListAPI(Resource):
    @marshal_with(notes_fields)
    def get(self):
	list = Notes.query.all()
	return list
