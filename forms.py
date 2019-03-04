
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SearchForm(FlaskForm):

    query = StringField('Username',
                           validators=[DataRequired(), Length(min=1, max=2000)])

    submit = SubmitField('Search')