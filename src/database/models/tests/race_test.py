from src.database.models import db

class RaceTest(db.Model):
    __tablename__ = 'test_track_race'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Float(3), nullable=False)
    test_event_id = db.Column(db.Integer, db.ForeignKey('test_event.id'), nullable=False)

    def __repr__(self):
        return f'<RaceTest {self.user_id} - {self.distance} - {self.time} - {self.test_event_id}>'
    

    def to_json(self, *excluded_fields):
        """
        Transform the class information to a dictionary, and remove unwanted fields

        Returns:
            (dict): The user in dictionary format
        """
        info = {
            'id': self.id,
            'distace': self.distance,
            'time': self.time,
            'test_event_id': self.test_event_id,
        }

        for field in excluded_fields:
            if field in info:
                del info[field]

        return info