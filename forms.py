from flask_wtf import FlaskForm
from wtforms.validators import URL, Optional, NumberRange
from wtforms import StringField, FloatField, TextAreaField, SelectField, BooleanField

class AddCupcake(FlaskForm):
    """ Form for adding a cupcake """

    name = StringField("Pet Name")
    species = SelectField("Species", choices=[('dog', 'dog'), ('cat', 'cat'), ('porcupine', 'porcupine')])
    photo_url = StringField("Photo Url", validators=[Optional(), URL(message="invalid url")])
    age = FloatField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="we dont believe you")])
    notes = TextAreaField("Notes")
    available = BooleanField("Available")