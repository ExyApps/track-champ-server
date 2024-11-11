from . import db

from datetime import datetime, timezone

class Team(db.Model):
    __tablename__ = 'acc_team'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    public = db.Column(db.Boolean, default=False)
    profile_image = db.Column(db.String(50), nullable=True)

    created_in = db.Column(db.DateTime, default=datetime.now(timezone.utc))


    def __repr__(self):
        return f'<Team {self.id} - {self.name} - {self.public}>'
    

    def to_json(self, *excluded_fields):
        """
        Transform the class information to a dictionary, and remove unwanted fields

        Returns:
            (dict): The user in dictionary format
        """
        info = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'public': self.public,
            'profile_image': self.profile_image,
            'created_in': self.created_in,
        }

        for field in excluded_fields:
            if field in info:
                del info[field]

        return info
