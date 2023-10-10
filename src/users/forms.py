from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from users.models import User


class RegistrationForm(FlaskForm):
    """This class defines the registration form."""
    
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=10, max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=40)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")
    
    def validate_username(self, username):
        """This method validates the username."""
        
        username.data = username.data.strip()
        
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("The username is already taken. Please choose a different one.")
    
    def validate_email(self, email):
        """This method validates the email."""
        
        email.data = email.data.strip()
        
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("An account has already been created with this email. Please login instead.")


class LoginForm(FlaskForm):
    """This class defines the login form."""
    
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=10, max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=40)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    """This class defines the update Account form."""
    
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=10, max=100)])
    photo = FileField("Upload A New Profile Picture", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Update")
    
    def validate_username(self, username):
        """This method validates the username."""
        
        username.data = username.data.strip()
        
        if username.data != current_user.username and User.query.filter_by(username=username.data).first():
            raise ValidationError("The username is already taken. Please choose a different one.")
    
    def validate_email(self, email):
        """This method validates the email."""
        
        email.data = email.data.strip()
        
        if email.data != current_user.email and User.query.filter_by(email=email.data).first():
            raise ValidationError("An account has already been created with this email. Please login instead.")

class ResetPasswordRequestForm(FlaskForm):
    """This class defines the request reset form."""
    
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=10, max=100)])
    submit = SubmitField("Request Password Reset")
    
    def validate_email(self, email):
        """This method validates the email."""
        
        email.data = email.data.strip()
        
        if not User.query.filter_by(email=email.data).first():
            raise ValidationError("No account has been created with this email. Please register instead.")


class ResetPasswordForm(FlaskForm):
    """This class defines the reset password form."""
    
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=40)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Reset Password")
