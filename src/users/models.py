import datetime, jwt
from flask import current_app
from flask_login import UserMixin
from blog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    photo = db.Column(db.String(20), nullable=False, default="default-image.png")
    posts = db.relationship("Post", backref="author", lazy=True)
    
    def get_password_reset_token(self, expires_sec=1800):
        return jwt.encode(
            payload={"reset_password": self.id,
                     "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_sec)},
            key=current_app.config["SECRET_KEY"],
            algorithm="HS256"
        )
    
    @staticmethod
    def verify_password_reset_token(token):
        try:
            user_id = jwt.decode(
                jwt=token,
                key=current_app.config["SECRET_KEY"],
                algorithms=["HS256"],
                verify=True
            )["reset_password"]
        except Exception:
            return None
        
        return User.query.get(user_id)
    
    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.photo})"
