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

    def post(self):
#	file = Get the file from the request
#	if files_allowed(file):
#	     Give it an appropriate filename that includes something random
#	     Move the file to the right static folder
#	note = Notes()
#	note.title = 'NEW - User submitted title'
#	note.author = 'User Submitted Name'
#	note.location = NOTES_STATIC_DIRECTORY + the filename + the suffix
#	note.published = False
#	db.session.add(note)
#	db.session.commit()
	return {'Success: We did the thing'} 

class NotesListAPI(Resource):
    @marshal_with(notes_fields)
    def get(self):
	list = Notes.query.all()
	return list
