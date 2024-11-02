from . import db

from datetime import datetime, timezone

class Teams(db.Model):
    __tablename__ = 'acc_teams'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    public = db.Column(db.Boolean, default=False)
    profile_image = db.Column(db.String(50), nullable=True)

    created_in = db.Column(db.DateTime, default=datetime.now(timezone.utc))


    def __repr__(self):
        return f'<Team {self.id} - {self.name} - {self.public}>'
    

    def to_json(self, excuded_fields = []):
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

        for field in excuded_fields:
            if field in info:
                del info[field]

        return info
