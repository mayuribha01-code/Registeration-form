from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])

    email = StringField('Email',
                        validators=[
                            DataRequired(message="Email is required"),
                            Email(message="Please enter a valid email address")
                        ])

    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=6, message="Password must be at least 6 characters")])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', message="Passwords must match")])

    submit = SubmitField('Register')