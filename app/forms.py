from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired

class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    img = StringField('img', validators=[InputRequired()])
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    gender = StringField('gender', validators=[InputRequired()])
    age = IntegerField('age', validators=[InputRequired()])
    bio = StringField('bio', validators=[InputRequired()])
    