"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name",
                        validators=[InputRequired()])
    species = SelectField("Species",
                           validators=[InputRequired()],
                           choices=[('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    age = SelectField('Age',
        choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')])
    notes = TextAreaField("Notes")
    
class EditPetForm(FlaskForm):
    """Form for Editing pets"""

    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    notes = TextAreaField("Notes")
    available = BooleanField(default="checked")
