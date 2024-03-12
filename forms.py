"""Forms for our demo Flask app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, AnyOf, URL, NumberRange, Optional

class AddPetForm(FlaskForm):
    """Use for initially adding a pet to the DB"""
    name = StringField("Pet Name", validators=[InputRequired("Pet Name can't be blank")])
    species = StringField("Pet Species", validators=[AnyOf(["Dog", "dog", "Cat", "cat", "Porcupine", "porcupine"], "Species must be dog, cat, or porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL("Must be a valid URL")])
    age = IntegerField("Pet Age", validators=[NumberRange(0, 30, "Age must be between 0 and 30")])
    notes = TextAreaField("Any special notes?")
    available = BooleanField("Available")

class EditPetForm(FlaskForm):
    """Edit a pet that is in the DB"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL("Must be a valid URL")])
    notes = TextAreaField("Any special notes?")
    available = BooleanField("Available")
