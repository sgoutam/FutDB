__author__ = 'Rahul'
from flask_wtf import Form
from wtforms import StringField,RadioField
from wtforms.validators import DataRequired


class SearchForm(Form):
    searchQuery = StringField('searchQuery', validators=[DataRequired()])
    searchChoice = RadioField('searchChoice', choices=[('player','Players'),('team','Teams')])
