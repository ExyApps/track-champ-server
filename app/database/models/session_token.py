from . import db

from datetime import datetime, timezone

class SessionToken(db.Model):
    __tablename__ = 'acc_session_token'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('acc_user.id'), nullable=False)
    token = db.Column(db.String(32), nullable=False)

    used_in = db.Column(db.DateTime, default=datetime.now(timezone.utc))


    def __repr__(self):
        return f'<SessionToken {self.user_id} - {self.token}>'
    

    def to_json(self, excuded_fields = []):
        """
        Transform the class information to a dictionary, and remove unwanted fields

        Returns:
            (dict): The user in dictionary format
        """
        info = {
            'id': self.id,
            'user_id': self.user_id,
            'token': self.token,
            'used_in': self.used_in,
        }

        for field in excuded_fields:
            if field in info:
                del info[field]

        return info
