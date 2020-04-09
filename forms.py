from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    categories = [('1', 'Cooking & Health'), ('2', 'Beauty & Fashion'), ('3', 'Music'), ('4', 'Pets & Animals'),
               ('5', 'Sports'), ('6', 'Short Movies'), ('7', 'Comedy'), ('8', 'Entertainment'),
               ('9', 'News & Politics'), ('10', 'Education'), ('11', 'Tech'),
               ('12', 'Travel & Events'), ('13', 'Videoblogging')]
    category = MultiCheckboxField('Category', choices=categories)
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')