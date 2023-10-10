from flask import current_app, render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from blog import db, bcrypt
from users.utils import save_picture
from users.forms import RegistrationForm, LoginForm, UpdateAccountForm, ResetPasswordRequestForm, ResetPasswordForm
from users.models import User
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

users = Blueprint("users", __name__)

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        db.session.add(User(
            username=form.username.data,
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")))
        
        db.session.commit()
        
        flash("Your account has been created successfully. Please login now.", "success")
        
        return redirect(url_for("users.login"))
    
    return render_template("register.html", title="Register", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            
            return redirect(request.args.get("next") or url_for("main.home"))
        
        flash("Login Unsuccessful. Please check email and password", "danger")
    
    return render_template("login.html", title="Login", form=form)


@users.route("/logout")
def logout():
    logout_user()
    
    return redirect(url_for("main.home"))


@users.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = UpdateAccountForm()
    
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        
        if form.photo.data:
            image_filename = save_picture(form.photo.data)
            current_user.photo = image_filename
        
        db.session.commit()
        
        flash("Your account info has been updated successfully.", "success")
        
        return redirect(url_for("users.profile")) # POST-GET-Redirect pattern.
    
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    return render_template("account.html", form=form)


@users.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    """
    Description:
        Handles the reset password functionality.
        
        This route allows users to request a password reset by providing their email address. An email with instructions to reset the password is sent to the user's email address. If the user is already authenticated, they are redirected to the home page.
    
    ---
    Returns:
        If the form is submitted and valid, redirects to the login page after sending the password reset email.
        If the user is already authenticated, redirects to the home page.
        Otherwise, renders the reset password request form.
    """
    
    form = ResetPasswordRequestForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        token = user.get_password_reset_token()

        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo("Gmail")
        server.starttls()
        server.login(current_app.config["MAIL_ADDRESS"], current_app.config["MAIL_APPWORD"])

        Message = MIMEMultipart()
        Message["From"] = current_app.config["MAIL_ADDRESS"]
        Message["To"] = user.email
        Message["Subject"] = "Password Reset Request."
        
        messageText = MIMEText(f"To reset your password, visit the following link: {url_for('users.reset_password', token=token, _external=True)}","html")
        Message.attach(messageText)

        server.sendmail(current_app.config["MAIL_ADDRESS"], user.email, Message.as_string())
        server.quit()
        
        flash("An email has been sent with instructions to reset your password.", "info")
        
        if current_user.is_authenticated:
            return redirect(url_for("main.home"))
    
        return redirect(url_for("users.login"))
    
    return render_template("reset_password_request.html", form=form)


@users.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    user = User.verify_password_reset_token(token)
    
    if not user:
        flash("Token is invalid or expired.", "warning")
        
        return redirect(url_for("users.reset_password_request"))
    
    form = ResetPasswordForm()
    
    if form.validate_on_submit():
        user.password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        db.session.commit()
        
        flash("Your password has been updated successfully.", "success")
        
        return redirect(url_for("users.login"))
    
    return render_template("reset_password_form.html", form=form)
