from app import app, db
from app.models import Units, Subjects, Notes
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
import os
# Setup the Admin interface 
admin = Admin(app, name='Counter Course Admin')

# Add the model views
admin.add_view(ModelView(Units, db.session))
admin.add_view(ModelView(Subjects, db.session))
admin.add_view(ModelView(Notes, db.session))
static_path = os.path.join(os.path.dirname(__file__), 'app/static/notes')
admin.add_view(FileAdmin(static_path, '/static/', name='Notes Files'))

