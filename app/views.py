from app import app
from models import Units, Subjects, Notes
from flask import render_template


# Set up the views
@app.route('/')
def index():
	unit = Units.query.filter_by(code='ENGL1234').first()
	notes = [{'title':'Samson', 'location':'www.lmgtfy.com'},
		    {'title':'Delilah', 'location':'www.google.com'}]
	return render_template('unit.html', unit=unit, notes=notes)

@app.route('/subjects')
def subjectListView():
    return render_template('subject.html')

@app.route('/subjects/<int:name>')
def subjectView(name):
    spaced_name = re.sub(r'[\W_]', ' ', spaced_name)
    return "I should put something here"
    
@app.route('/units/')
def unitListView():
    return "The list of units"

@app.route('/units/<string:code>')
def unitView(code):
    unit = Units.query.filter_by(code=code).first()
    notes = [{'title':'Samson', 'location':'www.lmgtfy.com'},
	    {'title':'Delilah', 'location':'www.google.com'}]
    return render_template('unit.html', unit=unit, notes=notes)


