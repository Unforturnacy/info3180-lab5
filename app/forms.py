from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from flask_wtf.file import FileRequired, FileAllowed


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=255)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=1000)])
    poster = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'avif'], 'Images only!')
    ])