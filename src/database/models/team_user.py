from . import db

from datetime import datetime, timezone

class TeamUser(db.Model):
    __tablename__ = 'acc_team_user'

    user_id = db.Column(db.Integer, db.ForeignKey('acc_user.id'), primary_key=True, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('acc_team.id'), primary_key=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    joined_in = db.Column(db.DateTime, default=datetime.now(timezone.utc))


    def __repr__(self):
        return f'<TeamUser {self.user_id} - {self.team_id} - {self.admin}>'
    

    def to_json(self, excluded_fields = []):
        """
        Transform the class information to a dictionary, and remove unwanted fields

        Returns:
            (dict): The user in dictionary format
        """
        info = {
            'user_id': self.user_id,
            'team_id': self.team_id,
            'is_admin': self.is_admin,
            'joined_in': self.joined_in,
        }

        for field in excluded_fields:
            if field in info:
                del info[field]

        return info
