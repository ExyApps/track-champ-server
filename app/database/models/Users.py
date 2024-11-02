from . import db
from app.database.models.GenderEnum import GenderEnum

from datetime import datetime, timezone

class Users(db.Model):
    __tablename__ = 'acc_users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(110), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    salt = db.Column(db.String(30), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.Enum(GenderEnum), nullable=False)
    profile_image = db.Column(db.String(50), nullable=True)
    activated = db.Column(db.Boolean, nullable=False, default=False)

    created_in = db.Column(db.DateTime, default = datetime.now(timezone.utc))
    last_login = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<User {self.id} - {self.first_name} {self.last_name} - {self.username} - {self.email}>'

    def to_json(self, excuded_fields = []):
        """
        Transform the class information to a dictionary, and remove unwanted fields

        Returns:
            (dict): The user in dictionary format
        """
        info = {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'birthday': self.birthday,
            'gender': self.gender.value,
            'profile_image': self.profile_image,
            'activated': self.activated,
            'created_in': self.created_in,
            'last_login': self.last_login,
        }

        for field in excuded_fields:
            if field in info:
                del info[field]

        return info
