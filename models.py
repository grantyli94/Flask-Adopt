"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """A table of pet instances"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(20),
                   nullable=False)
    species = db.Column(db.String(20),
                   nullable=False)
    photo_url = db.Column(db.String,
                   nullable=False,
                   default='')
    age = db.Column(db.String,
                   nullable=False)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
    
    def __repr__(self):
        """Displays info about the pet"""
        
        return (f'<Pet {self.id} {self.name} {self.species} {self.age}>')
