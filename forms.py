import recs
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, TextField, TextAreaField
from wtforms.validators import (
    DataRequired,
    ValidationError,
    Email,
    Length,
    EqualTo,
    Regexp,
)
from models import User


def name_exist(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError("User with that name already exists.")


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidatationError("User with that email already exists")


class RegisterForm(Form):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Regexp(
                r"^[a-zA-Z0-9_]+$",
                message=(
                    "Username should be one word consiting of letters, numbers and underscores only"
                ),
            ),
            name_exist,
        ],
    )
    email = StringField("Email", validators=[DataRequired(), Email(), email_exists])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo("password2", message="Passwords must match"),
        ],
    )
    password2 = PasswordField("Confirm Password", validators=[DataRequired()])


class LoginForm(Form):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class PostForm(Form):

    book = TextField("Book Name", validators = [DataRequired()])
    content = TextAreaField("Message", validators=[DataRequired()])    
    
