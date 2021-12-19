from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
  cities = StringField('Enter City Name')
  submit = SubmitField('Search')