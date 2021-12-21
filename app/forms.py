from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
  cities = StringField('Enter City Name', validators=[DataRequired()])
  submit = SubmitField('Search')


class SelectForm(FlaskForm):
  select_city = SelectField('Choose City', coerce=int, validators=[DataRequired()])