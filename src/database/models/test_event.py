from . import db

from datetime import datetime, timezone

class TestEvent(db.Model):
    __tablename__ = 'test_event'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey('test_category.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('test_test.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('acc_user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)


    def __repr__(self):
        return f'<TestEvent {self.id} - {self.category_id} - {self.test_id} - {self.user_id} - {self.date}>'
    

    def to_json(self, *excluded_fields):
        """
        Transform the class information to a dictionary, and remove unwanted fields

        Returns:
            (dict): The user in dictionary format
        """
        info = {
            'id': self.id,
            'name': self.name,
            'category': self.category,
        }

        for field in excluded_fields:
            if field in info:
                del info[field]

        return info
