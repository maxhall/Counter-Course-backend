# Database tables for the Counter Course Backend

from app import db
from app import app

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
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
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

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    official_link = db.Column(db.String(100))
    review = db.Column(db.Text)
    published = db.Column(db.Boolean)
    # Relationship to the Units that comprise the Subject Area
    units = db.relationship('Units', backref='Subject', lazy='dynamic')

    def __init__(self, name, official_link, review, published):
	self.name = name
	self.official_link = official_link
	self.review = review
	self.published = published

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    location = db.Column(db.String(80))
    published = db.Column(db.Boolean)
    # Foreign Key of the Unit that the notes are for
    unit = db.Column(db.Integer, db.ForeignKey('units.id'))

    def __init__(self, title, author, location, published, unit):
	self.title = title
	self.author = author
	self.location = location
	self.published = published
	self.unit = unit


